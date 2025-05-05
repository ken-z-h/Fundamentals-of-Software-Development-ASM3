def validate_email(email):
    if not email.endswith("@university.com"):
        return False
    try:
        name_part = email[:-len("@university.com")]
        firstname, lastname = name_part.split(".")
        if not (firstname.islower() and lastname.islower() and firstname.isalpha() and lastname.isalpha()):
            return False
        return True
    except ValueError:
        return False  

def validate_password(password):
    if len(password) < 8: 
        return False
    if not password[0].isupper():
        return False
    
    letters_part = ''
    digits_part = ''
    
    for c in password[1:]:
        if c.isalpha():
            letters_part += c
        else:
            digits_part += c
    
    if len(letters_part) < 4:
        return False  
    if len(digits_part) < 3:
        return False
    if not all(c.isalpha() for c in letters_part):
        return False
    if not all(c.isdigit() for c in digits_part):
        return False
    return True