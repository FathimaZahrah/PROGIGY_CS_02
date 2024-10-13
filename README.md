# Image Encryption using Pixel Manipulation.
This python program implements a simple image encryption and decryption tool using basic mathematical operation (Multiplication and Modulus) for pixel manipulation. 

The encryption process involves applying a mathematical operation, multiplication on the RGB values of each pixel in an image, using a user-defined odd integer key. 

For decryption, the program computes the modular inverse of the key to restore the original pixel values, thereby reversing the encryption process. The choice of an odd integer for the key ensures that the encryption is robust, as it guarantees the existence of a modular inverse under the modulus of 256, thus preventing potential errors during the decryption phase.

The implementation leverages the Pillow library in Python for handling image files, allowing users to easily encrypt and decrypt images through a straightforward command-line interface.
