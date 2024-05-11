import requests
from bs4 import BeautifulSoup
from constants import X_RATES_ENDPOINT, HEADERS


def get_currency_rate(from_currency, to_currency):
    """
    Scrape the currency rate for the conversion.

    Args:
        from_currency (str): The currency symbol to convert from.
        to_currency (str): The currency symbol to convert to.

    Returns:
        float: The currency rate.
    """
    try:
        # Construct the URL for the currency conversion API
        url = f'{X_RATES_ENDPOINT}?from={
            from_currency}&to={to_currency}&amount=1'
        # Define headers for the HTTP request
        headers = HEADERS

        # Send HTTP GET request to the API
        response = requests.get(url, headers=headers)
        # Check if the response is successful
        response.raise_for_status()

        # Extract the HTML content from the response
        html_source = response.text
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_source, 'html.parser')

        # Select the currency rate element from the parsed HTML
        rate_element = soup.select_one(
            "#content > div:nth-child(1) > div > div:nth-child(1) > div > div > span.ccOutputRslt")

        # Check if the currency rate element is found
        if rate_element is None:
            raise Exception("\n-- Currency rate element not found --\n\n")

        # Get the text content of the currency rate element
        rate = rate_element.get_text()
        # Clean the extracted rate and convert it to float
        cleaned_rate = rate.strip()[:-4]

        return float(cleaned_rate)

    except requests.RequestException as e:
        # Handle errors related to HTTP request
        raise Exception(f"\n-- Error during HTTP request: {e}\n\n")

    except Exception as e:
        # Handle other unexpected errors
        raise Exception(f"\n-- Error occurred: {e}\n\n")
