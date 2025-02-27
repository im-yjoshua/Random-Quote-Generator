# Quote Generator

This Python script fetches and displays quotes from various categories using the [API Ninjas Quotes API](https://api-ninjas.com/api/quotes).

## Features

- Fetches random quotes or quotes from specific categories.
- Displays the quote along with the author's name.
- Handles errors gracefully.

## Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```bash
pip install requests
```

# Usage
1. Clone the repository:
```
git clone https://github.com/im-yjoshua/Random-Quote-Generator.git
```
2. Navigate to the project directory:
```
cd .\Random-Quote-Generator\
```
3. Run the script:
```
python random_quote_generator.py
```
# Code
```
import requests

API_KEY = 't9Nkn7Xa18jqPW09JN8nsw==uqG0BTtfUK3ZlaKL'
BASE_URL = 'https://api.api-ninjas.com/v1/quotes'

def get_quote(category=None):
    params = {'category': category} if category else {}
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            return data[0]['quote'], data[0]['author']
        else:
            return None, "No quotes found for the given category."
    else:
        return None, f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    category = input("Enter Quote Category (leave blank for random): ").strip()
    quote, author = get_quote(category)
    if quote:
        print(f'QUOTE: {quote}\nAUTHOR: {author}')
    else:
        print(author)
```

# API Key
This script uses the API Ninjas Quotes API. You need to replace the `API_KEY` variable with your own API key. You can get an API key by signing up on the [API Ninjas website](https://api-ninjas.com/).

# License
This project is licensed under the MIT License

# Contributing
- Fork the repository
- Create your feature branch (git checkout -b feature/fooBar)
- Commit your changes (git commit -am 'Add some fooBar')
- Push to the branch (git push origin feature/fooBar)
- Create a new Pull Request

# Acknowledgments
- [API Ninjas](https://api-ninjas.com/) for providing the Quotes API.