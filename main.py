import os

# Hardcoded secret (Kwetsbaarheid)
API_KEY = "123456-abcdef-67890"

# Insecure code (Kwetsbaarheid)
os.system("rm -rf /")


def say_hello():
    print("Hello, Secure Pipeline!")


say_hello()