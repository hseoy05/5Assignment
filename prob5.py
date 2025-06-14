from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes

def enc(msg):
    padding_len = (-len(msg))%16
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(msg)

def dec(msg):
    cipher =AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(msg)
    print(pt[-1])
    return pt[:-pt[-1]]

def zerosum(msg):
    d = dec(enc(msg))
    print("A - B: ")
    print("B: "+str(bytes_to_long(d)))
    print("A: " + str(bytes_to_long(msg)))
    result =bytes_to_long(msg) - bytes_to_long(d)
    print("Zerosum result: " + str(long_to_bytes(result)))
    return result

#------------- 1st try -----------------------------------------------------
print("[Zero-Sum Checker]")

print("ORIGIN NUmber: " + str(bytes_to_long(b"I DONT HAVE A VM TO RUN THIS...")))

#result=> 
#129202533240186286462732125273400048806685490057755497850365772060813045294
#n = bytes_to_long(b"I DONT HAVE A VM TO RUN THIS...")
#m = bytes_to_long(b"I DONT HAVE A VM TO RUN THIS...")
#print(n + m)
#result=>
#258405066480372572925464250546800097613370980115510995700731544121626090588
#print(long_to_bytes(258405066480372572925464250546800097613370980115510995700731544121626090588))
#result=>
#b'\x92@\x88\x9e\x9c\xa8@\x90\x82\xac\x8a@\x82@\xac\x9a@\xa8\x9e@\xa4\xaa\x9c@\xa8\x90\x92\xa6\\\\\\'
#print(hex(258405066480372572925464250546800097613370980115510995700731544121626090588))
#result=>
#0x9240889e9ca8409082ac8a408240ac9a40a89e40a4aa9c40a89092a65c5c5c
#-------------------------------------------------------------------------

# ---------------- 2트 --------------------------------------

original_msg = b"I DONT HAVE A VM TO RUN THIS..."  # 31 bytes
padded_msg = original_msg + b'\x01'                # PKCS#7 padding → 32 bytes

msg_long = bytes_to_long(padded_msg)
crafted = long_to_bytes(msg_long)
print(f"HEX input: {crafted.hex()}")
print(f"BYTE 길이: {len(crafted)}")
# ----------------------------------------------------------------------


key, iv = urandom(16), urandom(16)
if(zerosum(bytes.fromhex(input("INPUT: "))) == bytes_to_long(b"I DONT HAVE A VM TO RUN THIS...")):
    print("Correct!")
else:
    print("Try Again...")