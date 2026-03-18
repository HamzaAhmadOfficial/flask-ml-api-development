from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def preprocess(image):

    image = image.resize((224,224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    return image


@app.route("/classify", methods=["POST"])
def classify():

    file = request.files["image"]

    image = Image.open(file)

    input_data = preprocess(image)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])

    prediction = np.argmax(output)

    confidence = float(np.max(output))

    return jsonify({
        "prediction": int(prediction),
        "confidence": confidence
    })


@app.route("/classify_batch", methods=["POST"])
def classify_batch():

    files = request.files.getlist("images")

    results = []

    for file in files:

        image = Image.open(file)

        input_data = preprocess(image)

        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        output = interpreter.get_tensor(output_details[0]['index'])

        prediction = int(np.argmax(output))
        confidence = float(np.max(output))

        results.append({
            "prediction": prediction,
            "confidence": confidence
        })

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)