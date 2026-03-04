from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    # Logic to save the blog post
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)