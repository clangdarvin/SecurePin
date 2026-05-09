# SecurePin

<!--toc:start-->
- [SecurePin](#securepin)
  - [Motivation](#motivation)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Test](#test)
<!--toc:end-->

## Motivation

As a computer science student, I find the process of manually coming up with passcodes repetitive and trivial. However, the best practice of formulating a robust passcode must still be observed. This CLI tool is useful for situations where you quickly need a secure passcode consisting of 4 to 6 digits.

Under the hood, this tool relies on Python's built-in `secrets` library. According to the documentation:

> The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

— [Python `secrets` library documentation](https://docs.python.org/3/library/secrets.html)

## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/clangdarvin/SecurePin.git

cd SecurePin
```

Install the required dependencies

```
pip install -r requirements.txt
```

## Usage

Run the script and specify the number of digits (4 or 6) as an argument. The PIN will be automatically copied to your clipboard.

```bash
python main.py 4

python main.py 6
```

## Test

To ensure everything is working correctly, you can run the test suite using pytest

```bash
pytest test_pin.py
```
