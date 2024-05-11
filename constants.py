
HTML_CONTENT = """
<body style="background-color: #1e1e3f; font-family: 'Lucida Console', monospace; font-size: 14px;">
<div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #444; border-radius: 5px; background-color: #282a36; color: #f8f8f2;">
    <h1>Currency Rate API</h1>
    <p>Welcome to the Currency Rate API!</p>
    <p>This API provides currency conversion rates between different currencies.</p>
    <h2>Usage</h2>
    <p>To use this API, you can make GET requests to the following endpoint:</p>
    <p style="color: #20B2AA; font-size: larger;"><code>/api/v1/rate/&lt;source_currency&gt;-&lt;target_currency&gt;</code></p>
    <p>Replace <span style="color: #32CD32;">&lt;source_currency&gt;</span> with the source currency code (e.g., <span style="color: #FFD700;">USD</span>) and <span style="color: #32CD32;">&lt;target_currency&gt;</span> with the target currency code (e.g., <span style="color: #FFD700;">EUR</span>).</p>
    <p>Example: To get the conversion rate from USD to EUR, you can make a GET request to <a href="/api/v1/rate/USD-EUR" style="color: #20B2AA; font-size: larger; text-decoration: none;"><code>/api/v1/rate/USD-EUR</code></a>.</p>
    <h2>Response Format</h2>
    <p>The API returns JSON data with the following format:</p>
    <pre>
    {
        "source_currency": <span style="color: #FFD700;">"USD"</span>,
        "target_currency": <span style="color: #FFD700;">"EUR"</span>,
        "rate": <span style="color: #FFD700;">0.85</span>
    }
    </pre>
    <p>The <span style="color: #32CD32;"><code>rate</code></span> field represents the conversion rate from the source currency to the target currency.</p>
</div>
</body>
"""


# Define custom headers to mimic a web browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

X_RATES_ENDPOINT = "https://www.x-rates.com/calculator/"
