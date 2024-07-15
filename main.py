import os
import sqlite3
import numpy as np
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3  #type:ignore
from tensorflow.keras.preprocessing import image #type:ignore
from tensorflow.keras.applications.inception_v3 import preprocess_input #type:ignore
from sklearn.metrics.pairwise import cosine_similarity  #type:ignore

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Initialize the InceptionV3 model
model = InceptionV3(weights='imagenet', include_top=False)

# Connect to SQLite database
conn = sqlite3.connect('dresses.db', check_same_thread=False)
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS dresses
             (id INTEGER PRIMARY KEY, name TEXT, features BLOB)''')
conn.commit()

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    features = model.predict(img_data)
    return features.flatten()

def get_features_from_db():
    c.execute("SELECT id, name, features FROM dresses")
    rows = c.fetchall()
    feature_list = []
    for row in rows:
        feature_list.append({
            'id': row[0],
            'name': row[1],
            'features': np.frombuffer(row[2], dtype=np.float32)
        })
    return feature_list

def search_similar_dress(query_features):
    dresses = get_features_from_db()
    max_similarity = 0
    best_match = None

    for dress in dresses:
        db_features = dress['features'].reshape(-1)  # Flatten to 1D array
        similarity = cosine_similarity(query_features.reshape(1, -1), db_features.reshape(1, -1))[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = dress

    return best_match, max_similarity

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        query_features = extract_features(file_path)
        best_match, similarity = search_similar_dress(query_features)
        
        if similarity > 0.8:  # Adjust threshold as needed
            #return jsonify({'message': f"Best match: {best_match['name']} with similarity: {similarity}"})
            return jsonify({'message': "It is there in the stock! GRAB IT NOW!!!"})
        else:
            return jsonify({'message': "It will be in stock in a few days!"})

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
