from flask import Flask, request, jsonify, redirect
import hashlib

app = Flask(__name__)

url_mapping = {}

def generate_short_code(url):
    hash_object = hashlib.sha256(url.encode())
    hex_dig = hash_object.hexdigest()
    short_code = hex_dig[:6]
    
    
    while f"http://localhost:5000/{short_code}" in url_mapping:
        
        hash_object.update(url.encode())
        hex_dig = hash_object.hexdigest()
        short_code = hex_dig[:6]
    
    return short_code

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data.get('url')

   
    short_code = generate_short_code(long_url)
    short_url = f"http://localhost:5000/{short_code}"

    url_mapping[short_url] = long_url

    return jsonify({"short_url": short_url})

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    short_url = f"http://localhost:5000/{short_code}"
    long_url = url_mapping.get(short_url)

    if long_url:
        return redirect(long_url)
    else:
        return jsonify({"error": "URL not found"}), 404
    
if __name__ == "__main__":
    app.run()