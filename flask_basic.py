from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# GET /
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Flask Basics API"})


# GET /data
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(data)


# POST /data
@app.route("/data", methods=["POST"])
def add_data():
    new_item = request.get_json()

    item = {
        "id": len(data) + 1,
        "name": new_item.get("name")
    }

    data.append(item)
    return jsonify(item), 201


# PUT /data/<id>
@app.route("/data/<int:id>", methods=["PUT"])
def update_data(id):
    updated = request.get_json()

    for item in data:
        if item["id"] == id:
            item["name"] = updated.get("name")
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


# DELETE /data/<id>
@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):

    for item in data:
        if item["id"] == id:
            data.remove(item)
            return jsonify({"message": "Item deleted"})

    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)