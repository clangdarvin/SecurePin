import argparse
import pyperclip
from utils import pin_generator


def main():
    parser = argparse.ArgumentParser(description="Generate a secure 4 or 6-digit PIN.")
    parser.add_argument(
        "length",
        type=int,
        choices=[4, 6],
        help="Length of the PIN to generate (must be 4 or 6)",
    )

    args = parser.parse_args()

    pin = pin_generator.generate_pin(args.length)
    pyperclip.copy(pin)
    print(f"Success! {args.length}-digit PIN copied to clipboard.")


if __name__ == "__main__":
    main()
