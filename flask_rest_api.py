from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

API_KEY = "123456"

logging.basicConfig(level=logging.INFO)


class Prediction(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(100))
    prediction = db.Column(db.String(50))
    confidence = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)


def require_api_key(func):

    def wrapper(*args, **kwargs):

        key = request.headers.get("x-api-key")

        if key != API_KEY:
            return jsonify({"error":"Unauthorized"}),401

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper


@app.route("/predictions", methods=["POST"])
@require_api_key
def save_prediction():

    data = request.get_json()

    pred = Prediction(
        image_name=data["image_name"],
        prediction=data["prediction"],
        confidence=data["confidence"]
    )

    db.session.add(pred)
    db.session.commit()

    logging.info("Prediction saved")

    return jsonify({"message":"saved"})


@app.route("/predictions", methods=["GET"])
@require_api_key
def get_predictions():

    page = request.args.get("page",1,type=int)

    results = Prediction.query.paginate(page=page, per_page=5)

    output = []

    for r in results.items:

        output.append({
            "id": r.id,
            "image_name": r.image_name,
            "prediction": r.prediction,
            "confidence": r.confidence,
            "date": r.date
        })

    return jsonify(output)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)