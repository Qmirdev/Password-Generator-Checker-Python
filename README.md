# Password Generator & Strength Checker

A Python script to generate random passwords and analyze their strength.

#### This Python script has two main features for generating and analyzing passwords:

## Password Generator

- Generates random passwords of user-specified length
- Uses a combination of letters, numbers and symbols to create secure passwords
- Password length is configurable based on user input
- Uses the secrets module to generate cryptographically secure random characters
- Ensures at least 2 numbers and 1 special symbol in each password before considering it strong
- Logs each generated password with timestamp to passwords.log file

## Password Strength Checker

Password Strength Checker
- Analyzes strength of a user-input password
- Checks password for:
    - Lowercase letters
    - Uppercase letters
    - Numbers
    - Symbols
    - Whitespace characters
- Calculates overall password strength score out of 1.0
- Provides feedback to user on how to improve password security
- Considers password with all character types as very strong
- Provides remarks based on strength score to change or keep password
- Logs feedback provided to user for each password checked

## Usage

Run `python3 PassGEN.py`

1. Enter desired password length when prompted
2. Generated password will be printed
3. Optionally check strength of the generated password
4. Or check strength of a different password entered when prompted

## Requirements

- Python 3.x
- secrets, string, getpass, logging, datetime modules
-
Overall, this script generates strong random passwords and analyzes the strength of user passwords to enforce good password security practices. The logging provides an audit trail of passwords.

> [!NOTE]
> Simply Install all needed dependencies with executing `pip install -r requirements.txt` in the project directory.

## License
This project is open source and available under the MIT License.

<3