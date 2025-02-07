import cv2
import os

# Base directory for storing images
DATASET_DIR = "dataset"
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# Take user input
name = input("Enter your name: ")
class_id = input("Enter your class (2 digits): ")
roll_no = input("Enter your roll number (3 digits): ")

# Validate inputs
if not (class_id.isdigit() and len(class_id) == 2):
    print("Invalid class format! Enter a 2-digit class number.")
    exit()
if not (roll_no.isdigit() and len(roll_no) == 3):
    print("Invalid roll number format! Enter a 3-digit roll number.")
    exit()

# Create filename (e.g., 09123.png)
image_name = f"{class_id}{roll_no}.png"
image_path = os.path.join(DATASET_DIR, image_name)

# Start the camera
cap = cv2.VideoCapture(0) # Open the default camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'Space' to capture the image, or 'Esc' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Capture Image", frame)
    key = cv2.waitKey(1)

    if key == 32: # Space key to capture image
        cv2.imwrite(image_path, frame)
        print(f"Image saved as {image_path}")
        break
    elif key == 27: # Esc key to exit
        print("Capture cancelled.")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
