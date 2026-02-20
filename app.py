from flask import Flask, request, current_app, jsonify

app = Flask(__name__)

@app.before_request
def before_request():
    print(request.method, request.path)


@app.after_request
def after_request(response):
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response

@app.teardown_request
def teardown_request(exception):
    if exception:
        print(exception)


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



@app.route('/calculate')
def calculate():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    operation = request.args.get('operation')
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400
        return jsonify({"result": result, "operation": operation})
    except Exception as e:
        # Log the exception and return an error response
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred during calculation"}), 500

@app.route("/echo", methods=["POST"])
def echo_endpoint():
    data = request.get_json()
    print(data)
    return {"echoed": True, "data" : data}

@app.route("/status/<int:code>", methods=["GET"])
def status_endpoint(code):
    return ((f'This is a {code} error'), code)



@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)



if __name__ =='__main__':
    app.run(debug=True)