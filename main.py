from flask import Flask, jsonify, render_template
from utils import get_currency_rate

# Create an instance of the Flask application
app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the home page of the FXRate API.

    This endpoint handles the root URL and returns the rendered 
    HTML template for the home page, providing an interface for 
    users to interact with the currency conversion API.

    Returns:
        Response: The rendered HTML template for the home page.
    """
    return render_template("index.html")


@app.route("/api/v1/rate/<string:source_currency>-<string:target_currency>")
def api_default(source_currency, target_currency):
    """
    Endpoint for retrieving currency conversion rate between two currencies.

    Args:
        source_currency (str): Source currency code.
        target_currency (str): Target currency code.

    Returns:
        dict: Dictionary containing source_currency, target_currency, and rate.
    """
    # Get the currency rate by scraping it from the x-rates website
    rate = get_currency_rate(source_currency, target_currency)

    # Define a dictionary
    data = {
        'source_currency': source_currency.upper(),
        'target_currency': target_currency.upper(),
        'rate': rate  # Placeholder for the actual conversion rate
    }

    # Return the dictionary as JSON response
    return jsonify(data)


if __name__ == "__main__":
    # Run the Flask application in debug mode, allowing for debugging information to be displayed
    app.run(debug=True)
