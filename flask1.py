from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Base directory for storing images
DATASET_DIR = "dataset"
if not os.path.exists(DATASET_DIR):
    os.makedirs(DATASET_DIR)

# Endpoint for uploading a student's image
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files or 'name' not in request.form:
        return jsonify({'error': 'Image and name are required'}), 400

    image = request.files['image']
    name = request.form['name'].strip().replace(" ", "_") # Remove spaces in name

    person_dir = os.path.join(DATASET_DIR, name)
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)

    image_path = os.path.join(person_dir, f"{name}.png")
    image.save(image_path)

    return jsonify({'message': f"Image saved as {image_path}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
