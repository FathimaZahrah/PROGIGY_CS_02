from PIL import Image

def is_odd(num):
    return num % 2 != 0

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load() 

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            r_new = (r * key) % 256
            g_new = (g * key) % 256
            b_new = (b * key) % 256
            pixels[i, j] = (r_new, g_new, b_new)

    img.save("encrypted_image.png")
    print("Image encrypted successfully as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load() 

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            r_new = (r * pow(key, -1, 256)) % 256
            g_new = (g * pow(key, -1, 256)) % 256
            b_new = (b * pow(key, -1, 256)) % 256
            pixels[i, j] = (int(r_new), int(g_new), int(b_new))

    img.save("decrypted_image.png")
    print("Image decrypted successfully as 'decrypted_image.png'.")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").upper()
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key (an integer, must be odd): "))

    if not is_odd(key):
        print("The key must be an odd integer. Please try again.")
        return

    if choice == 'E':
        encrypt_image(image_path, key)
    elif choice == 'D':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice! Please select (E)ncrypt or (D)ecrypt.")

if __name__ == "__main__":
    main()
