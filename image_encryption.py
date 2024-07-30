from PIL import Image
import numpy as np

def load_image(image_path):
    """Load an image from the specified path and return it as a numpy array."""
    image = Image.open(image_path)
    image_array = np.array(image)
    return image_array, image.mode

def save_image(image_array, mode, output_path):
    """Save a numpy array as an image."""
    image = Image.fromarray(image_array, mode)
    image.save(output_path)

def encrypt_image(image_array, key):
    """Encrypt the image by applying XOR with a key on each pixel."""
    encrypted_array = image_array ^ key
    return encrypted_array

def decrypt_image(encrypted_array, key):
    """Decrypt the image by applying XOR with a key on each pixel."""
    decrypted_array = encrypted_array ^ key
    return decrypted_array


image_path = "C:\\MinGW\\bin\\Screenshot 2024-07-29 033256.png"

encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
encryption_key = 123 


image_array, mode = load_image(image_path)

encrypted_image_array = encrypt_image(image_array, encryption_key)
save_image(encrypted_image_array, mode, encrypted_image_path)


decrypted_image_array = decrypt_image(encrypted_image_array, encryption_key)
save_image(decrypted_image_array, mode, decrypted_image_path)

print("Encryption and decryption completed.")
