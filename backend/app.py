from flask import Flask, jsonify, request
from db import get_targets
from scanner import run_scan

app = Flask(__name__)

@app.route('/api/targets', methods=['GET'])
def list_targets():
    targets = get_targets()
    return jsonify(targets)

@app.route('/api/scan', methods=['POST'])
def scan_target():
    target_ip = request.json.get('ip')
    result = run_scan(target_ip)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
