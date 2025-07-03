import re  # Importing the 're' module to use regular expressions for pattern matching

def check_password_strength(password):
    # Define the minimum length for a strong password
    min_length = 6
    
    # Check if the password contains at least one uppercase letter
    has_upper = re.search(r'[A-Z]', password)
    
    # Check if the password contains at least one lowercase letter
    has_lower = re.search(r'[a-z]', password)
    
    # Check if the password contains at least one digit
    has_digit = re.search(r'\d', password)
    
    # Check if the password contains at least one special character
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Initialize the score variable to zero
    score = 0

    # Check each criterion and update the score accordingly
    if len(password) >= min_length:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Determine the strength level based on the score
    if score == 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    elif score == 5:
        strength = "Very Strong"
    else:
        strength = "Invalid"  # This should not normally occur with the given criteria

    return strength  # Return the strength level as a string


# Prompt the user to enter a password
password = input("Enter a password to check its strength: ")

# Check the strength of the entered password
strength = check_password_strength(password)

# Print the resulting strength level
print(f"Password strength: {strength}")
