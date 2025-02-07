from PIL import ImageGrab
import os

# Directory to save captured images
base_path = "/sdcard/FaceRecognition"
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Input person's name
person_name = input("Enter the person's name: ")

# Instruction
print("Please open your camera app, capture an image, and save it in the folder:")
print(base_path)

# Wait for user input
input("Once you've saved the image, press Enter to continue...")

# Save the image with the person's name
image_name = f"{person_name}.png"
image_path = os.path.join(base_path, image_name)

# Confirm image saving
if os.path.exists(image_path):
    print(f"Image '{image_name}' successfully saved in {base_path}.")
else:
    print(f"No image found in {base_path} with the name '{image_name}'. Please try again.")
