from flask import Flask, jsonify

app = Flask(__name__)
visit_count = 0

@app.route('/')
def home():
    global visit_count
    visit_count += 1
    return f"Hello from flask running on kubernetes! Visit Count: {visit_count}"

@app.route('/about')
def about():
    return "This is a demo flask app for kubernetes CI/CD!"

@app.route('/status')
def status():
    return "App is running, perfectly"

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}! Welcome to flask on kubernetes!"

@app.route('/api/info')
def api_info():
    return jsonify({
        "app": "Flask on kubernetes",
        "version": "v1.0",
        "status": "running"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)