import hashlib

encoded = hashlib.sha256(b"Encode me!")

print( encoded.hexdigest())

# '68907fbd785a694c3617d35a6ce49477ac5704d75f0e727e353da7bc664aacc2'