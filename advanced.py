import re
import math

# Sample dictionary words for checking
dictionary_words = {"password", "welcome", "admin", "letmein", "monkey", "iloveyou", "princess", "babygirl", "ferrari", "mustang", "cowboy", "changeme" }

def calculate_entropy(password):
    # Calculate character set size based on types of characters in password
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32  # number of common special characters

    # Calculate entropy
    entropy = len(password) * math.log2(charset_size) if charset_size else 0
    return entropy

def check_password_strength(password, user_info=None, password_history=None):
    # Criteria definitions
    min_length = 8
    common_passwords = ["password", "123456", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "111111"]

    # Initialize score and feedback
    score = 0
    feedback = []

    # Check minimum length
    if len(password) >= min_length:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Check for sequences
    if re.search(r'(012345|123456|234567|345678|456789|567890|678901|789012|890123|901234|abcdefghijklmnopqrstuvwxyz|qwertyuiop|asdfghjkl|zxcvbnm)', password.lower()):
        feedback.append("Password should not contain sequences like '12345' or 'abcdef'.")
    else:
        score += 1
    
    # Check for repeating characters
    if re.search(r'(.)\1\1', password):
        feedback.append("Password should not contain repeating characters like 'aaa' or '111'.")
    else:
        score += 1
    
    # Check for common passwords
    if password.lower() in common_passwords:
        feedback.append("Password should not be a common password like 'password' or '123456'.")
    else:
        score += 1
    
    # Check for dictionary words
    if any(word in password.lower() for word in dictionary_words):
        feedback.append("Password should not contain dictionary words.")
    else:
        score += 1

    # Check for user-specific information
    if user_info:
        if any(info.lower() in password.lower() for info in user_info):
            feedback.append("Password should not contain personal information like your name or email.")
    
    # Check against password history
    if password_history:
        if password.lower() in (old_password.lower() for old_password in password_history):
            feedback.append("Password should not be reused from your password history.")

    # Calculate entropy
    entropy = calculate_entropy(password)
    if entropy < 50:
        feedback.append("Password entropy is low, consider adding more unique characters for better security.")
    else:
        score += 1

    # Determine strength level
    if score <= 2:
        strength = "Very Weak"
    elif score <= 4:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback, entropy

# Sample usage of the function
if __name__ == "__main__":
    # Prompt the user to enter a password
    password = input("Enter a password to check its strength: ")
    
    # Optionally, pass user information and password history
    user_info = ["username", "user@example.com"]
    password_history = ["oldpassword123", "password123!"]
    
    # Check the strength of the entered password
    strength, feedback, entropy = check_password_strength(password, user_info, password_history)
    
    # Print the resulting strength level
    print(f"Password strength: {strength}")
    
    # Print entropy
    print(f"Password entropy: {entropy:.2f} bits")
    
    # Print feedback
    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
