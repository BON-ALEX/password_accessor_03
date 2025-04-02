import re
def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 16:
        strength += 2
    elif len(password) >= 12:
        strength += 1
        if len(password) < 16:
            feedback.append("Consider making your password longer (at least 16 characters).")
    elif len(password) >= 8:
        feedback.append("Your password is too short (aim for at least 12 characters).")
    else:
        feedback.append("Your password is much too short (minimum 8 characters).")
        return (0, feedback)
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add uppercase letters to strengthen your password.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add lowercase letters to strengthen your password.")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Include numbers to strengthen your password.")
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    else:
        feedback.append("Add special characters (!@#$%^&*, etc.) to strengthen your password.")
    
    # Check for common patterns or weak passwords
    common_passwords = ["password", "123456", "qwerty", "letmein", "welcome"]
    if password.lower() in common_passwords:
        strength = 0
        feedback = ["This is an extremely common and weak password. Please "
        "choose something more unique."]
    
    # Strength descriptions
    strength_description = [
        "Very Weak",
        "Weak",
        "Moderate",
        "Strong",
        "Very Strong",
        "Excellent"
    ]
    
    # Ensure strength is within bounds
    strength = min(strength, 5)
    
    # If password is strong enough, provide positive feedback
    if strength >= 4 and not feedback:
        feedback.append("Great job! Your password meets all the important security criteria.")
    elif strength >= 4:
        feedback.insert(0, "Your password is strong, but could be even better:")
    
    return (strength, strength_description[strength], feedback)

def main():
    print("Password Strength Assessor")
    print("-------------------------")
    while True:
        password = input("\nEnter a password to assess (or 'quit' to exit): ")
        if password.lower() == 'quit':
            break
        
        strength, rating, feedback = assess_password_strength(password)
        
        print(f"\nPassword Strength: {rating} ({strength}/5)")
        
        if strength <= 2:
            print("⚠️ Warning: This password is not secure enough for most purposes.")
        
        print("\nFeedback:")
        for item in feedback:
            print(f"- {item}")
        
        # Visual strength indicator
        print("\nStrength Meter:")
        print("[" + "█" * strength + " " * (5 - strength) + "]")

if __name__ == "__main__":
    main()