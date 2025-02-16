def caesar_cipher(text, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift 
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char 
    
    return result

message = "Hello, World!"
shift_value = 3
encrypted = caesar_cipher(message, shift_value)
decrypted = caesar_cipher(encrypted, shift_value, encrypt=False)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
