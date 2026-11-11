def mask_card_number(number):
    if not isinstance(number, str):
        return ""

    digits = "".join(ch for ch in number if ch.isascii() and ch.isdigit())

    if not digits:
        return ""
    if len(digits) < 4:
        return "*" * len(digits)
    return "*" * 12 + digits[-4:]


def parse_transaction(line):
    if not isinstance(line, str):
        return None

    parts = line.split(",")
    if len(parts) != 3:
        return None

    category = parts[1].strip().lower()
    if not category:
        return None

    try:
        amount = int(parts[2].strip())
    except (ValueError, OverflowError):
        return None

    return category, amount


def parse_statement_total(text):
    if not isinstance(text, str) or ":" not in text:
        return None

    amount = text.split(":", 1)[1]
    amount = "".join(amount.replace(",", "").split())

    try:
        return int(amount)
    except (ValueError, OverflowError):
        return None


def main():
    print("==== Running mask_card_number ====")
    value = input("Enter a card number (e.g. 4111 1111 1111 1234): ")
    print("Masked card number:", mask_card_number(value) or "Invalid card number")

    print("\n==== Running parse_transaction ====")
    value = input("Enter a transaction as DATE,CATEGORY,AMOUNT (e.g. 2026-11-05,dining,1550): ")
    result = parse_transaction(value)
    print("Category and amount:", result if result is not None else "Invalid transaction")

    print("\n==== Running parse_statement_total ====")
    value = input("Enter the statement total line (e.g. Total: 12,500): ")
    result = parse_statement_total(value)
    print("Statement total:", result if result is not None else "Invalid statement total")


if __name__ == "__main__":
    main()