# Currency Rate API

## Overview
Currency Rate API is a Flask-based web application that provides currency conversion rates between different currencies.

## Features
- **Home Page**: Renders the home page of the Currency Rate API.
- **Currency Conversion API**: Endpoint for retrieving currency conversion rate between two currencies.

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
This project is licensed under the [MIT License](LICENSE).