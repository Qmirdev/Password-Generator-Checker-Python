# Password Generator & Strength Checker
A Python script to generate random passwords and analyze their strength.

#### This script has two main features:

## Password Generator
Generates a random password of your desired length
Uses letters, numbers and symbols to create secure passwords
Password length is configurable via user input

## Password Strength Checker
Checks the strength of a user input password Analyzes password for:
- Lowercase, uppercase, numbers, symbols
- Password length
- Calculates a password strength score out of 1.0
- Provides feedback on how to improve password security
Passwords generated and checked are logged with a timestamp for records.

### Usage
To use the password generator simply run

`python3 PassGEN.py`

You will be prompted to enter the desired password length. A random password containing letters, numbers and symbols will be generated.

To check the strength of a password:

Enter a password when prompted after running the script. The password will be analyzed and you will receive feedback on its strength and how to improve it.

### Requirements
> [!NOTE]
> Simply Install all needed dependencies with executing `pip install -r requirements.txt` in the project directory.

This script requires Python 3 and the following modules:
secrets
string
logging
datetime
License
This project is open source and available under the MIT License.

<3