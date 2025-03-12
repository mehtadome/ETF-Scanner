import importlib.metadata
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from modules.calcs.ETFs.annual_return import one_year_return as etf_one_year_return
from modules.calcs.MutualFunds.annual_return import one_year_return as mf_one_year_return

import sys
sys.path.append('../backend/')

app = Flask(__name__)
# Explicit setup for Cross-Origin calls
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Accept"],
        "expose_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

# Setup custom logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.DEBUG)

# Add Werkzeug logger for access logs
logging.getLogger('werkzeug').setLevel(logging.INFO)
logging.getLogger('werkzeug').addHandler(logging.StreamHandler())



@app.route('/')
def home():
    """
    Return the ID of the app and Flask version.

    Returns:
        HTML: A string containing:
            - flask_version (str): The version of Flask being used.
            - host_name (str): The hostname of the machine running the app.
    """
    app.logger.info(f"Received request for home page")
    flask_version = importlib.metadata.version("flask")
    host_name = request.host
    return f"<h1>Hello World!</h1> <br /><h2>Backend is running :)</h2> <br /><h3>Flask Version: {flask_version}</h3> <br /><h3>Host Name: {host_name}</h3>"
    

@app.route('/etfs/1year')
def etfs_1year():
    """
    Return the top 10 best choices for 1 year return.

    Returns:
        JSON: { "message": List[] }
    Raises:
        400: If request fails.
        500: Backend logic wrong.
    """
    try: 
        app.logger.info(f"Received request for best 1 year return on ETFs.")
        best_10 = etf_one_year_return()

        app.logger.info(f"Best 10 ETFs for 1 year return: {best_10}")
        return jsonify(best_10)
    
    except Exception as e:
        app.logger.error(f"Error, {e}")
        return jsonify({"error": f"{e}"}), 400


@app.route('/mutualfunds/10year')
def mutualfunds_10year():
    """
    Return the top 10 best choices for 10 year return.

    Returns:
        JSON: { "message": List[] }
    Raises:
        400: If request fails.
        500: Backend logic wrong.
    """
    try:
        app.logger.info(f"Received request for best 10 year return on mutual funds.")
        best_10 = mf_one_year_return()

        app.logger.info(f"Best 10 Mutual Funds for 10 year return: {best_10}")
        return jsonify(best_10)

    except Exception as e:
        app.logger.error(f"Error, {e}")
        return jsonify({"error": f"{e}"}), 400

@app.route('/connection', methods=['GET'])
def conn_test():
    """
    Test connection btwn Vite <--> Flask
    
    Returns:
        JSON: { "Yo": "Hello World!" }
    Raises:
        400: If request fails
    """
    try:
        app.logger.info(f"Received request for connection test.")
        app.logger.info (f"=============== CONNECTION TEST ===============\n\nYo: Hello World!\n")
        app.logger.info (f"=============== END OF CONNECTION TEST ===============\n")
        return jsonify({ "message" : "Yo, Hello World!"})
    
    except Exception as e:
        app.logger.error(f"Error, {e}")
        return jsonify({"error": f"{e}"}), 40


# Add a catch-all route for debugging
@app.route('/<path:path>')
def catch_all(path):
    app.logger.info(f"Caught unhandled path: {path}")
    return jsonify({"error": "Route not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
   