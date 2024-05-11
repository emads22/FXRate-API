from flask import Flask, jsonify
from constants import HTML_CONTENT
from utils import get_currency_rate

# Create an instance of the Flask application
app = Flask(__name__)


@app.route("/")
def home():
    """
    Renders the home page of the Currency Rate API.

    Returns:
        str: HTML content for the home page.
    """
    return HTML_CONTENT


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
