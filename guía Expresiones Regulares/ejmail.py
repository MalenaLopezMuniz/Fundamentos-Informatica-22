import re
def validar_mail (string):
    return bool(re.search("[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+@[a-zA-Z]{2,9}(\.[a-zA-z]{2,4})",string))

print(validar_mail("davidr@gmail.com"))   