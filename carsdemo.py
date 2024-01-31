from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# File path for storing cars data
file_path = "cars.json"

def read_cars_from_file():
    try:
        with open(file_path, "r") as file:
            cars_data = json.load(file)
        return cars_data
    except FileNotFoundError:
        return {}

def write_cars_to_file(cars_data):
    with open(file_path, "w") as file:
        json.dump(cars_data, file, indent=2)

# Just a basic home page
@app.route('/')
def index():
    return "Hello World"

# Route to get all cars
# 'GET /cars' - Get all cars
@app.route('/cars', methods=['GET'])
def get_all_cars():
    cars_data = read_cars_from_file()
    return jsonify(cars_data)

# Route to get details of a specific car
# 'GET /cars/<car_id>' - Get details of a specific car
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    cars_data = read_cars_from_file()
    car = cars_data.get(str(car_id))
    if car:
        return jsonify(car)
    else:
        return jsonify({"error": "Car not found"}), 404

# Route to add a new car
# 'POST /cars' - Add a new car
@app.route('/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    cars_data = read_cars_from_file()
    new_car_id = str(max(map(int, cars_data.keys()), default=0) + 1)
    cars_data[new_car_id] = {
        "name": data["name"],
        "year": data["year"],
        "price": data["price"]
    }
    write_cars_to_file(cars_data)
    return jsonify({"message": "Car added successfully", "car_id": new_car_id})

# Route to delete a car
# 'DELETE /cars/<car_id>' - Delete a car
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    cars_data = read_cars_from_file()
    if str(car_id) in cars_data:
        del cars_data[str(car_id)]
        write_cars_to_file(cars_data)
        return jsonify({"message": "Car deleted successfully"})
    else:
        return jsonify({"error": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)
