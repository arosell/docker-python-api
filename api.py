from flask import Flask, json
from datetime import datetime

payload = [{"timestamp": datetime.now(), "message": "test"}]

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return json.dumps(payload)

if __name__ == "__main__":
    app.run(port=5000)
