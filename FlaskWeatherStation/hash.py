import hashlib

# Accepts a string and converts it into a hash.
def hash_string(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
