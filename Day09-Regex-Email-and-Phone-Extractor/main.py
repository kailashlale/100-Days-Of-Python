import csv
import re
from typing import List
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, ConfigDict


class EmailContact(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    email: EmailStr


class PhoneContact(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    phone: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        cleaned = re.sub(r"[^\d+]", "", v)
        digit_count = len(re.findall(r"\d", cleaned))

        if digit_count < 10:
            raise ValueError(
                f"Phone number must have at least 10 digits, got {digit_count}"
            )

        if digit_count > 15:
            raise ValueError(f"Phone number too long, got {digit_count} digits")

        if not re.match(r"^[\+1-9]", v.strip()):
            raise ValueError("Phone number must start with + or digit 1-9")

        return v.strip()


class ContactInfo(BaseModel):
    emails: List[str] = []
    phone_numbers: List[str] = []
    invalid_emails: List[str] = []
    invalid_phones: List[str] = []


def get_contents():
    while True:
        print("Select input method")
        print("1. CSV file (.csv)")
        print("2. TXT file (.txt)")
        print("3. Paste in terminal")
        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            csv_path = input("Enter .csv file path: ").strip()
            text_parts = []
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    text_parts.append(" ".join(row))
            content = " ".join(text_parts)
            return content

        if choice == "2":
            txt_path = input("Enter .txt file path: ").strip()
            with open(txt_path, "r", encoding="utf-8") as f:
                content = f.read()
            return content

        if choice == "3":
            content = input("Paste your text here: ").strip()
            return content

        else:
            print("Invalid choice")
            print(f"{'-' * 30}")


def extract_email(content):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)
    unique_emails = set(emails)

    valid_emails = []
    invalid_emails = []

    for email in unique_emails:
        try:
            validated = EmailContact(email=email)
            valid_emails.append(validated.email)

        except ValidationError as e:
            invalid_emails.append(f"{email}\n{e.errors()[0]['msg']}")

    return valid_emails, invalid_emails


def extract_contact(content):
    contact_pattern = r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]"
    phone_numbers = re.findall(contact_pattern, content)
    unique_contacts = set(phone_numbers)

    valid_phones = []
    invalid_phones = []

    for contact in unique_contacts:
        try:
            validated = PhoneContact(phone=contact)
            valid_phones.append(validated.phone)
        except ValidationError as e:
            invalid_phones.append(f"{contact}\n{e.errors()[0]['msg']}")

    return valid_phones, invalid_phones


def process_content():
    content = get_contents()
    valid_emails, invalid_emails = extract_email(content)
    valid_phones, invalid_phones = extract_contact(content)

    contact_details = ContactInfo(
        emails=valid_emails,
        phone_numbers=valid_phones,
        invalid_emails=invalid_emails,
        invalid_phones=invalid_phones,
    )

    print(f"{'-' * 30}")
    print("EXTRACTION & VALIDATION RESULTS")
    print(f"{'-' * 30}")

    if contact_details.emails:
        print(f"Valid Emails ({len(contact_details.emails)}):")
        for email in contact_details.emails:
            print(email)

    print(f"{'-' * 30}")

    if contact_details.phone_numbers:
        print(f"Valid Phone Number ({len(contact_details.phone_numbers)}):")
        for number in contact_details.phone_numbers:
            print(number)

    print(f"{'-' * 30}")

    if contact_details.invalid_emails:
        print(f"Invalid Emails ({len(contact_details.invalid_emails)}):")
        for email in contact_details.invalid_emails:
            print(email)

    print(f"{'-' * 30}")

    if contact_details.invalid_phones:
        print(f"Invalid Phone Number: ({len(contact_details.invalid_phones)}):")
        for number in contact_details.invalid_phones:
            print(number)

    print(f"{'-' * 30}")

    return contact_details


if __name__ == "__main__":
    process_content()
