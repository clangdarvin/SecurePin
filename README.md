# SecurePin

<!--toc:start-->
- [SecurePin](#securepin)
  - [Motivation](#motivation)
  - [Installation](#installation)
    - [Prerequisites (Linux only)](#prerequisites-linux-only)
    - [Option 1: Global Install using ```pipx``` (Recommended)](#option-1-global-install-using-pipx-recommended)
    - [Option 2: Local install using ```pip```](#option-2-local-install-using-pip)
  - [Usage](#usage)
  - [Test](#test)
<!--toc:end-->

## Motivation

As a computer science student, I find the process of manually coming up with passcodes repetitive and trivial. However, the best practice of formulating a robust passcode must still be observed. This CLI tool is useful for situations where you quickly need a secure passcode consisting of 4 to 6 digits.

Under the hood, this tool relies on Python's built-in `secrets` library. According to the documentation:

> The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

— [Python `secrets` library documentation](https://docs.python.org/3/library/secrets.html)

## Installation

### Prerequisites (Linux only)
If you are on a Linux system (Debian or Ubuntu), you will need Python, pipx, and a clipboard manager (for X11 or Wayland) installed:

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv pipx xclip wl-clipboard
```

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/clangdarvin/SecurePin.git
cd SecurePin
```

### Option 1: Global Install using ```pipx``` (Recommended)

```bash
pipx install .
```

Ensure pipx is in your system path. (First-time setup only)

```bash
pipx ensurepath
```

Restart your terminal, or reload your shell

```bash
source ~/.bashrc # For bash users
# OR 
source ~/.zshrc # For zsh users
```

### Option 2: Local install using ```pip```

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the script and specify the number of digits (4 or 6) as an argument. The PIN will be automatically copied to your clipboard.

If installed through pipx:

```bash
securepin 4
securepin 6
```

If installed through pip:

```bash
python main.py 4
python main.py 6
```

## Test

To ensure everything is working correctly, you can run the test suite using ```pytest```. Make sure you have installed the requirements using the ```pip``` option above.

```bash
pytest test_pin.py
```
