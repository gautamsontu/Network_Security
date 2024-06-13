with open('EviRaw.txt', 'r') as file:
    hex_string = file.read()

hex_string = ''.join(hex_string.split())
binary_data = bytes.fromhex(hex_string)

with open('recipe_converted.docx', 'wb') as binary_file:
    binary_file.write(binary_data)

print("Conversion complete.")
