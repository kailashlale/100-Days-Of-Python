import logging
from zxcvbn import zxcvbn
from typing import Dict, Any, List, Tuple

logging.basicConfig(format="%(message)s", level=logging.INFO)

SEPARATOR = "=" * 50

LARGE_NUMBERS: List[Tuple[float, str]] = [
    (1e12, "trillion"),
    (1e15, "quadrillion"),
    (1e18, "quintillion"),
    (1e21, "sextillion"),
    (1e24, "septillion"),
    (1e27, "octillion"),
    (1e30, "nonillion"),
    (1e33, "decillion"),
    (1e36, "undecillion"),
    (1e39, "duodecillion"),
    (1e42, "tredecillion"),
    (1e45, "quattuordecillion"),
    (1e48, "quindecillion"),
    (1e51, "sexdecillion"),
    (1e54, "septendecillion"),
    (1e57, "octodecillion"),
    (1e60, "novemdecillion"),
    (1e63, "vigintillion"),
]

ATTACK_TYPES = {
    "online_throttling_100_per_hour": "Online Attack (Rate-Limited)",
    "online_no_throttling_10_per_second": "Online Attack (No/Weak Limits)",
    "offline_slow_hashing_1e4_per_second": "Offline Attack (Single Computer)",
    "offline_fast_hashing_1e10_per_second": "Offline Attack (Powerful GPUs)",
}

STRENGTH_MAP = {0: "Very Weak", 1: "Weak", 2: "Medium", 3: "Strong", 4: "Very Strong"}


def format_crack_time(seconds: float) -> str:
    if seconds < 1:
        return "Instant"

    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365.25

    if seconds < minute:
        return f"{seconds:.2f} seconds"
    elif seconds < hour:
        return f"{seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"{seconds / hour:.2f} hours"
    elif seconds < year:
        return f"{seconds / day:.2f} days"

    years = seconds / year

    for scale, name in reversed(LARGE_NUMBERS):
        if years >= scale:
            value = years / scale
            formatted_time = f"{value:.2f} {name} years"
            return formatted_time

    if years >= 1e9:
        value = years / 1e9
        formatted_time = f"{value:.2f} billion years"
    elif years >= 1e6:
        value = years / 1e6
        formatted_time = f"{value:.2f} million years"
    elif years >= 1e3:
        value = years / 1e3
        formatted_time = f"{value:.2f} thousand years"
    else:
        formatted_time = f"{years:.2f} years"

    return formatted_time


def get_character_breakdown(password: str) -> Dict[str, List[str]]:
    alpha = []
    upper = []
    lower = []
    digit = []
    symbol = []
    for char in password:
        if char.isalpha():
            alpha.append(char)
            if char.isupper():
                upper.append(char)
            elif char.islower():
                lower.append(char)

        elif char.isdigit():
            digit.append(char)

        elif not char.isalnum() and not char.isspace():
            symbol.append(char)
    password_dict = dict(
        alpha=alpha, upper=upper, lower=lower, digit=digit, symbol=symbol
    )
    return password_dict


def analyze_password(password: str) -> Dict[str, Any]:
    zxcvbn_result = zxcvbn(password)
    char_breakdown = get_character_breakdown(password)

    return {
        "breakdown": char_breakdown,
        "score": zxcvbn_result["score"],
        "guesses": zxcvbn_result["guesses"],
        "crack_times": zxcvbn_result["crack_times_seconds"],
        "feedback": zxcvbn_result["feedback"],
        "sequence": zxcvbn_result["sequence"],
    }


def display_results(password: str, results: Dict[str, Any]) -> None:
    logging.info(SEPARATOR)
    logging.info(f"{f'Password Analysis for {password!r} ':^50}")
    logging.info(SEPARATOR)

    for key, value in results["breakdown"].items():
        if key != "alpha" and value:
            logging.info(f" {key.title()} (Total {len(value)}): {value}")

    pass_strength = STRENGTH_MAP.get(results["score"], "Unknown")

    logging.info(SEPARATOR)
    logging.info(f"Password Strength : {pass_strength}")
    logging.info(f"Guesses Required  : {results['guesses']:,}")
    logging.info(SEPARATOR)

    logging.info(f"{'Time-to-Crack Password Analysis:':^50}")
    logging.info(SEPARATOR)

    for key, value in results["crack_times"].items():
        if key in ATTACK_TYPES:
            readable_time = format_crack_time(int(value))
            logging.info(f" {ATTACK_TYPES[key]:<35}: {readable_time}")

    logging.info(SEPARATOR)
    logging.info("- Detected Patterns")
    for m in results["sequence"]:
        if m.get("pattern") != "bruteforce":
            logging.info(
                f" {m.get('pattern'):<12}: {m.get('token')!r:20} (Pos: {m.get('i')}-{m.get('j')})"
            )
        else:
            logging.info("  No patterns detected")

    feedback = results["feedback"]
    if feedback.get("warning"):
        logging.info(SEPARATOR)
        logging.info(f"- Feedback\n Warning : {feedback['warning']}")
        for suggestion in feedback.get("suggestions", []):
            logging.info(f" Suggestion : {suggestion}")

    logging.info(SEPARATOR)


def main():
    try:
        while True:
            password = input("Enter your password: ")

            if password:
                break
            else:
                logging.error("No password provided.")

        results = analyze_password(password)
        display_results(password, results)

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
