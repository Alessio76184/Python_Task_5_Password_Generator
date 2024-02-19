import re
import secrets
import string

# define the formation of the password the higher the number, the more the recurrence of that specific type of character
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            #secrets is import that is technically safer for generating random results
            password += secrets.choice(all_characters)
        
        constraints = [
            #r is a raw string which essentially reads everything
            #\d is short for digits 0-9
            #\W matches characters like punctuation marks, spaces, and other symbols while \w matches alphanumeric characters (letters and digits) and underscores.
            (nums, r'\d'),
            #f-strings and r-strings can be joined in one expression
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            # Hypothetical: If you want to, just check for a special character like. + or anything simply add a \ then the character e.g. \.
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    break
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
