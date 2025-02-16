
def check_passwords(passwords):
    valid_passwords = []

    # Iterate through each password provided
    for password in passwords:
        # Check the length requirement
        if len(password) < 6 or len(password) > 12:
            continue

        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False

        # Check each character of the password
        for char in password:
            if 'a' <= char <= 'z':
                has_lower = True
            elif 'A' <= char <= 'Z':
                has_upper = True
            elif '0' <= char <= '9':
                has_digit = True
            elif char in ')(}{][":?><,./$#@!%*^&':  # # This checks for all special characters
                has_special = True

        # If all criteria are met, add to valid_passwords list
        if has_lower and has_upper and has_digit and has_special:
            valid_passwords.append(password)

    return ','.join(valid_passwords)

# Input: comma-separated passwords
password_input = input("Enter passwords (comma-separated): ")
password_list = password_input.split(',')

# Check and print valid passwords
valid_passwords = check_passwords(password_list)
if valid_passwords:
    print("Valid passwords: ", valid_passwords)
else:
    print("No valid passwords found.")

