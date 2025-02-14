## Vigenère Cipher

This repository contains an implementation of the Vigenère Cipher, a classic encryption algorithm used for secure communication. The cipher uses a keyword to encrypt and decrypt a message, with each letter being shifted based on the corresponding letter of the key.

## Features

- **Encryption**: Encrypt plaintext using a keyword.
- **Decryption**: Decrypt ciphertext back into the original plaintext using the same keyword.
- **Randomized Alphabet**: The cipher uses a randomized alphabet for added security.
- **Customizable Alphabet**: You can customize the alphabet used for encryption if needed.

### Clone the Repository

To clone this repository to your local machine, run the following command in your terminal:

```bash
git clone https://github.com/toncotales/vigenere-cipher.git
```

### Running the Code
```python
from vigenere_cipher import VigenereCipher

# Create a cipher object
vc = VigenereCipher()

# Create a simple cipher key
key = "JustASimpleKey"

# Or create a random key (Optional)
# key = vc.random_alphabet()

# Encrypt a message
plaintext = "Hello, World!"
ciphertext = vc.cipher(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the message
decrypted_text = vc.decipher(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
```

## Contributing
Feel free to fork this repository, make improvements, or report issues. Contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
