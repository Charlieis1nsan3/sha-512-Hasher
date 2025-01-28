import hashlib

# Convert the dum ah data to hash

data = "put yo sha-512 shi here"

# Create a ShA-512 Hash of the data

hash_object = hashlib.sha512(data.encode())
hash_hex = hash_object.hexdigest()
print(hash_hex)
