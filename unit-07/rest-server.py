from flask import Flask, request, jsonify
import json, datetime

app = Flask(__name__) # Initialize the Flask application

# Simple GET endpoint for testing
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online",
            "message": "Server is running. POST to /api/data"})

@app.route("/api/data", methods=["POST"])
def receive_data():
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        collected_info = {"data": request.get_json(),
                          "time": timestamp}
        filename = f"{timestamp}.json"
        # Add logging before return
        with open(filename, "w") as f:
            json.dump(collected_info, f, indent=4)
        return {"status": "success"}, 200
    except Exception as e:  # Add more specific Exceptions
        return {"status": "error", "message": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
    print("Starting server on port 5000...")
