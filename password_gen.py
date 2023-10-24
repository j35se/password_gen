import random
import string

REGCHARS = string.ascii_letters + string.digits
SPCHAR = "!#)(*+-:;<=>?~^}{|,"
PASSWORDCHAR = REGCHARS + SPCHAR

def generate_password():
    while True:
        n = random.randint(15, 31)
        PASSWORD = []
        for i in range(n):
            char = random.choice(PASSWORDCHAR)
            while char in PASSWORD[-2:]:
                char = random.choice(PASSWORDCHAR)
            PASSWORD.append(char)
        PASSWORD = "".join(PASSWORD)
        if PASSWORD[0] not in SPCHAR and \
            (any(p.islower() for p in PASSWORD)
            and any(p.isupper() for p in PASSWORD)
            and sum(p.isdigit() for p in PASSWORD) >= 3):
                break
    print(PASSWORD)


generate_password()
