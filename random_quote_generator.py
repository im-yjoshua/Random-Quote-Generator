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
