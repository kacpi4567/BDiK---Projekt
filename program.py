import hashlib as hl
import bcrypt as bp
import time as tm
import itertools as it
from datetime import datetime as dm


def hash():
    for line in f:
        # list_sha1.append([line, hl.sha1(line).hexdigest()])
        list_md5.append([line, hl.md5(line).hexdigest()])
        # list_bcrypt.append(bp.hashpw(line, bp.gensalt()).hex())
    f.close()


def check(list, password):
    for elem, hex in list:
        if hex == password:
            return elem.decode()
    return False


password = b"admin"
pass_sha1 = hl.sha1(password).hexdigest()
pass_md5 = hl.md5(password).hexdigest()
pass_bcrypt = bp.hashpw(password, bp.gensalt()).hex()

f = open("rockyou_short.txt", "rb")
list_sha1 = []
list_md5 = []
list_bcrypt = []


hash()
# print(check(list_sha1, pass_sha1))
print(check(list_md5, pass_md5))
# print(check(pass_bcrypt, pass_bcrypt))
