What does the @app.route() decorator actually do?
    @app.route() sets the route for requests and specifies which requests are allowed. 
How does Flask know which function to call when a request arrives?
    @app.route is the path from the request to the function
What's the difference between route parameters (<name>) and query parameters (?key=value)?
    Route parameters are part of the route itself and get passed into the function, while
    query parameters are not part of the route, they are used for different inputs. 
Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?
    GET requests are meant to get non-structured data and post requests are meant to send structured data. That's why 
    they need to be converted to JSON but get requests are getting the data from the URL.
What happens if you try to access request.args outside of a request context?
    You get an error because the request is arguments are local to a request. 