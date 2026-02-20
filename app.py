from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

@app.before_request
def before_request():
    #add code to log


@app.route("/", methods=["GET"])
def welcome_endpoint():
    return "<h1>Welcome to My Flask API!</h1>"


@app.route("/about", methods=["GET"])
def about_endpoint():
    return jsonify({"name": "Rikki Genack", "course":
        "MCON-357 - Backend Development", "semester":
        "Spring 2026"})

@app.route("/greet/<name>", methods=["GET"])
def greet_endpoint(name):
    return f"Hello, {name}! Welcome to Flask."



@app.route("/calculate", methods=["GET"])
def calculate_endpoint():
    #num1, num2, operation
    operation = request.args.get("operation")
    if operation == "add":
        result = int(request.args.get("num1")) + int(request.args.get("num2"))
    elif operation == "subtract":
        result = int(request.args.get("num1")) - int(request.args.get("num2"))
    elif operation == "multiply":
        result = int(request.args.get("num1")) * int(request.args.get("num2"))
    elif operation == "divide":
        result = int(request.args.get("num1")) / int(request.args.get("num2"))
    return jsonify({"result": result, "operation": operation})

@app.route("/echo", methods=["POST"])
def echo_endpoint():
    print(request.get_json())
    return f'{request.get_json()} echoed": true'

@app.route("/status/<int:code>", methods=["GET"])
def status_endpoint(code):
    return ((f'This is a {code} error'), code)







if __name__ =='__main__':
    app.run(debug=True)