import string
from itertools import product
import re

# 암호문 입력
ciphertext = "BCBCCLBSTGIGSRATCXRKEIOBVFSHNCERSRURQKBGDWMMHWSBGPXGKLFJCVGFZTIGVJFONWKODGQEHRPQLURMWKHRCVNSXRKVH..."

# 영어 사전 불러오기 (간단한 버전)
with open("/usr/share/dict/words", "r") as f:
    english_words = set(word.strip().lower() for word in f if word.strip().isalpha() and len(word.strip()) > 3)

# 복호화 함수
def decrypt_vigenere(text, key_shifts):
    result = []
    for i, c in enumerate(text):
        shift = key_shifts[i % len(key_shifts)]
        if 'A' <= c <= 'Z':
            p = (ord(c) - ord('A') - shift + 26) % 26
            result.append(chr(p + ord('A')))
        else:
            result.append(c)
    return ''.join(result)

# 영어 단어 포함 개수 세는 함수
def score_english_words(text, dictionary):
    words = re.findall(r'\b[A-Z]{3,}\b', text)
    return sum(1 for word in words if word.lower() in dictionary)

# 전수조사
alphabet = string.ascii_uppercase
key_candidates = product(alphabet, repeat=5)

top_keys = []
for candidate in key_candidates:
    key_str = ''.join(candidate)
    shifts = [(ord(c) - ord('A')) for c in key_str]
    decoded = decrypt_vigenere(ciphertext, shifts)
    score = score_english_words(decoded[:300], english_words)  # 앞부분만 평가
    if score >= 2:  # 단어가 2개 이상이면 후보로 간주
        top_keys.append((key_str, score, decoded[:100]))
        if len(top_keys) >= 10:
            break

# 결과 출력
for k, score, preview in top_keys:
    print(f"Key: {k}, Score: {score}\nPreview: {preview}\n")
