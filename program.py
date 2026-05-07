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

pass_len = 8
temp_pass = []

def brute_force(callback):
    for i in range(pass_len):
        temp_pass.append("")
        for k in range(i):
            temp_pass.remove(k)
        while temp_pass[i-1] < 126 or i is 0:
            for j in range(32, 127):
                temp_pass[i] = chr(j)
                temp_string = str(temp_pass)
                temp_string_bytes = bytes(temp_string, "utf-8")
                temp_pass_hex = callback(temp_string_bytes)
            if i > 0:
                if temp_pass[i-1] < 126:
                    temp_pass[i-1] += 1
                    temp_pass.remove(i)

def hash_sha1(p):
    return hl.sha1(p).hexdigest()

def hash_md5(p):
    return hl.md5(p).hexdigest()

def hash_bp(p):
    return bp.hashpw(p, bp.gensalt()).hex()

password = b"123456"
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
