# Password Manager App

A simple yet powerful password manager application written in Python. This app provides a graphical user interface (GUI) and leverages cryptography to keep your data secure. It also includes a password generator to help you create strong passwords.

## Features

- **GUI**: User-friendly graphical interface.
- **Cryptography**: Securely encrypts your data.
- **Password Generator**: Generates strong, random passwords and automatically copies them to the clipboard for better user experience and security.
- **Data Security**: Your data is encrypted, so even if it gets leaked, it cannot be accessed without your `secret.key`.

## How It Works

1. **Data Encryption**: All your data is encrypted and stored in `data.txt`. 
2. **Secret Key**: To encrypt and decrypt your data, a `secret.key` file is required. This key is crucial for accessing your data.
3. **Data Safety**: Without the `secret.key`, your data remains secure even if `data.txt` is exposed.

### Important Notes

- **Decrypting Data**: To decrypt your data, place `secret.key` in the same folder as the code.
- **Handling Sensitive Data**: For highly sensitive data, write your `secret.key` on paper and delete the digital copy. Type it back when needed.
- **Password Generator**: Automatically copies generated passwords to the clipboard for convenience and enhanced security.
- **Disclaimer**: This project is a demo. There is no guarantee for your data safety. Use at your own risk.

## Recommendations

- **Customize**: You can change the `DEFAULT_USERNAME` constant to improve the user experience.
- **Security Best Practices**: Always handle your `secret.key` with care and follow recommended security practices to ensure your data remains secure.

Enjoy using your password manager app!
