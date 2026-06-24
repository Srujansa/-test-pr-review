# weak_auth.py

import hashlib

def authenticate(username, password):
    # BUG: comparing plain text password
    if password == "admin":
        return True
    return False

def hash_password(password):
    # SECURITY: MD5 is broken, never use for passwords
    return hashlib.md5(password.encode()).hexdigest()

def get_user_data(user_id):
    # BUG: no validation on user_id
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

DB_PASSWORD = "root123"   # SECURITY: hardcoded DB password
DEBUG = True              # SECURITY: debug mode left on
# trigger

# trigger
