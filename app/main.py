from flask import Flask, request, jsonify, render_template
import shutil
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move_folder', methods=['POST'])
def move_folder():
    data = request.get_json()
    source = os.path.abspath(data['source'])
    destination = os.path.abspath(data['destination'])

    print(f"Moving from: {source} to: {destination}")

    try:
        if os.path.exists(source) and os.path.isdir(source):
            shutil.move(source, destination)
            return jsonify({"message": "Folder moved successfully!"})
        else:
            return jsonify({"message": "Source folder not found"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
