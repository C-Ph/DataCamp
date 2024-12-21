# Start coding here
# Use as many cells as you need

def validate_user(name, email, password):
    if validate_name(name) == False:
        raise ValueError('name Error')
    
    if validate_email(email) == False:
        raise ValueError('email Error')
        
    if validate_password(password) == False:
        raise ValueError('password Error')
    
    return True

def register_user(name, email, password):
    
    if validate_user(name, email, password):
        user = {
            "name": name,       # เก็บชื่อที่ได้รับ
            "email": email,     
            "password": password 
        }
        return user
        
    return False