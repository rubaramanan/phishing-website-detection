from flask import Flask, request
from flask.json import jsonify
from src.phish_detector.predict_pipeline import predict
import json

app = Flask(__name__)


@app.route('/predict', methods=['post'])
def prediction():
    url = json.loads(request.data)['url']
    return jsonify(predict(url))


if __name__ == '__main__':
    app.run(debug=True)
