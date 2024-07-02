# FXRate API

## Overview
FXRate API is a robust and user-friendly Flask-based web application designed to provide accurate and real-time currency conversion rates. It seamlessly fetches exchange rates from [x-rates.com](https://www.x-rates.com/), ensuring users have access to reliable and up-to-date currency information. Whether for financial applications, e-commerce platforms, travel services, or personal use, FXRate API offers a dependable solution for all currency conversion needs.

## Features
- **Home Page**: Renders the home page of the Currency Rate API.
- **Currency Conversion API**: Endpoint for retrieving currency conversion rate between two currencies.

## Technologies Used
- **beautifulsoup4**: A library for parsing HTML and XML documents.
- **Flask**: A micro web framework for building web applications.
- **python-dotenv**: A library for managing environment variables in .env files.
- **requests**: A library for making HTTP requests.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as `constants.py`.
   - Ensure to set up `constants.py` with the appropriate values.
5. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. Make GET requests to the following endpoint:
   - `/api/v1/rate/<source_currency>-<target_currency>`
     - Replace `<source_currency>` with the source currency code (e.g., USD) and `<target_currency>` with the target currency code (e.g., EUR).
     - Example: To get the conversion rate from USD to EUR, make a GET request to `/api/v1/rate/USD-EUR`.

```
{
    "source_currency": "USD",
    "target_currency": "EUR",
    "rate": 0.928099
}
```

3. The `rate` field represents the conversion rate from the source currency to the target currency.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.