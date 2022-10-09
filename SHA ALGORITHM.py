import hashlib

text1 = hashlib.sha1(b'hello')
encrypt1 = text1.hexdigest()
print(encrypt1)

text2 = hashlib.sha256(b'hello')
encrypt2 = text2.hexdigest()
print(encrypt2)

text3 = hashlib.sha384(b'hello')
encrypt3 = text3.hexdigest()
print(encrypt3)

text4 = hashlib.sha224(b'hello')
encrypt4 = text4.hexdigest()
print(encrypt4)
