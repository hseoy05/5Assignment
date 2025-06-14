from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes
message = "I DONT HAVE A VM TO RUN THIS..."
message_b = b"I DONT HAVE A VM TO RUN THIS..."
print(len(message))
print("Origin: "+str(bytes_to_long(message_b)))
message_b32 =  b"I DONT HAVE A VM TO RUN THIS..."
print("My think: "+str(bytes_to_long(message_b32)))
print("Origin Hex: "+str(hex(bytes_to_long(message_b32))))

bitAnswerNum = len(message_b32)
#-----------------------------------------
def enc(msg):
    padding_len = (-len(msg))%16
    msg+=bytes([padding_len]*padding_len)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(msg)

def dec(msg):
    cipher =AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(msg)
    print("PT[-1]결과: "+str(pt[-1]))
    return pt[:-pt[-1]]

def zerosum(msg):
    print("내 실행 결과: "+str(bytes_to_long(msg)-bytes_to_long(dec(enc(msg)))))
    print("복호화 결과: "+str(bytes_to_long(dec(enc(msg)))))
    print("------------------------")
    value = long_to_bytes(bytes_to_long(msg)-bytes_to_long(dec(enc(msg))))
    print(value)
    print(bytes_to_long(msg)-bytes_to_long(dec(enc(msg))))
    print("-----------------------")
    return bytes_to_long(msg)-bytes_to_long(dec(enc(msg)))


key, iv = urandom(16), urandom(16)
if(zerosum(bytes.fromhex(input("INPUT: "))) == bytes_to_long(b"I DONT HAVE A VM TO RUN THIS...")):
    print("Correct!")
else:
    print("Try Again...")

#------------------------------------------------------


print("비트 수: "+str(bitAnswerNum))
print("최종 결과 숫자: "+str(bytes_to_long(message_b)))
answerNum = 129202533240186286462732125273400048806685490057755497850365772060813045294

print()
#findNum
#findNum_ = dec(enc(findNum))
#findNum = answerNum + findNum_
#4920444f4e542048415645204120564d20544f2052554e20544849532e2e2e20
