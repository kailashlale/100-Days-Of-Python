from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

DIV = "-" * 45


def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            logger.error("Invalid format! Please use DD/MM/YYYY")


def calculate_difference():
    d1 = get_date_input("Enter first date (DD/MM/YYYY): ")
    d2 = get_date_input("Enter second date (DD/MM/YYYY): ")

    if d1 > d2:
        d1, d2 = d2, d1
        logger.info("Swapped dates to ensure positive difference.")

    include_end = input("Include end date in difference? (y/n): ").lower().strip()

    if include_end == "y":
        calc_d2 = d2 + timedelta(days=1)
    else:
        calc_d2 = d2

    diff = relativedelta(calc_d2, d1)

    parts = []
    if diff.years > 0:
        parts.append(f"{diff.years} years")
    if diff.months > 0:
        parts.append(f"{diff.months} months")
    if diff.days > 0:
        parts.append(f"{diff.days} days")

    if not parts:
        output_str = "0 days"
    else:
        output_str = ", ".join(parts)

    print(f"{DIV}\nDifference: {output_str}")

    total_days = (calc_d2 - d1).days
    total_weeks = total_days / 7

    print(f"{DIV}\nAlternative time units:")
    print(f"{total_weeks:.1f} total weeks")
    print(f"{total_days} total days")
    print(f"{total_days * 24:,} total hours")
    print(f"{total_days * 1440:,} total minutes")
    print(f"{total_days * 86400:,} total seconds")
    print(f"{DIV}")


calculate_difference()
