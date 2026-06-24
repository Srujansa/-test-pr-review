# buggy_code.py

def divide(a, b):
    # BUG: no check for division by zero
    return a / b

def get_user(db, username):
    # SECURITY: SQL injection risk
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db.execute(query)

def save_password(password):
    # SECURITY: hardcoded secret key
    secret = "supersecret123"
    return password + secret

API_KEY = "sk-1234567890abcdef"  # SECURITY: exposed API key

result = divide(10, 0)
print(result)