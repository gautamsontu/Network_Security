import base64
with open("forensic.txt", "r") as file:
    base64_encoded_str = file.read()
base64_encoded_str = base64_encoded_str.replace("\n", "")

decoded_bytes = base64.b64decode(base64_encoded_str)

with open("decoded.docx", "wb") as file:
    file.write(decoded_bytes)