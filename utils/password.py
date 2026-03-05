import bcrypt


# ==============================
# HASH PASSWORD
# ==============================

def hash_password(password):

    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode("utf-8")



# ==============================
# CHECK PASSWORD
# ==============================

def check_password(password, hashed_password):

    password_bytes = password.encode("utf-8")

    hashed_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hashed_bytes)
