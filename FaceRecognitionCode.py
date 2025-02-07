from PIL import Image, ImageDraw
import os
import xlwt
from xlwt import Workbook
from datetime import date
import xlrd
from xlutils.copy import copy as xl_copy

# Directory paths
base_path = "/sdcard/FaceRecognition"
if not os.path.exists(base_path):
    os.makedirs(base_path)

# Image paths (place images like rahul.png, sneha.png in the same folder)
image1_path = os.path.join(base_path, 'rahul.png')
image2_path = os.path.join(base_path, 'sneha.png')

# Check if image files exist
if not os.path.exists(image1_path) or not os.path.exists(image2_path):
    raise FileNotFoundError("Required image files (rahul.png, sneha.png) are missing in the directory: " + base_path)

# Excel file path
excel_path = os.path.join(base_path, 'attendance_excel.xls')

# Known faces and names (manually set for simplicity)
person1_name = "Rahul"
person2_name = "Sneha"

# Create or load Excel file
if os.path.exists(excel_path):
    rb = xlrd.open_workbook(excel_path, formatting_info=True)
    wb = xl_copy(rb)
else:
    wb = Workbook()

subject_name = input("Please enter the subject name: ")
sheet1 = wb.add_sheet(subject_name)
sheet1.write(0, 0, 'Name/Date')
sheet1.write(0, 1, str(date.today()))
row = 1
col = 0
already_attendance_taken = ""

# Simple method to recognize faces based on image matching
def process_image(image_path):
    global row, col, already_attendance_taken
    
    # Open image with Pillow
    image = Image.open(image_path)
    
    # Simulate face recognition based on image matching
    # In real use, you would process the image and compare features for recognition
    # Here, we assume the images are "Rahul.png" and "Sneha.png" for simplicity
    name = "Unknown"
    if image_path == image1_path:
        name = person1_name
    elif image_path == image2_path:
        name = person2_name

    if name != "Unknown" and already_attendance_taken != name:
        sheet1.write(row, col, name)
        col += 1
        sheet1.write(row, col, "Present")
        row += 1
        col = 0
        print(f"Attendance recorded for {name}")
        wb.save(excel_path)
        already_attendance_taken = name
    else:
        print("Next person...")

    # Save the processed image
    output_image_path = os.path.join(base_path, "processed_" + os.path.basename(image_path))
    image.save(output_image_path)
    print(f"Processed image saved at: {output_image_path}")

# Main Program
while True:
    print("Place a new image in the folder and provide its name, or type 'q' to quit.")
    image_name = input("Enter the name of the image file (e.g., 'new_image.png'): ")
    if image_name.lower() == 'q':
        print("Exiting...")
        break

    image_path = os.path.join(base_path, image_name)
    if not os.path.exists(image_path):
        print(f"File '{image_name}' not found in {base_path}. Try again.")
        continue

    # Process the provided image
    process_image(image_path)
