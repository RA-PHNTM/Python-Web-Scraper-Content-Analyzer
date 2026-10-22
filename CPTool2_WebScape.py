import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def load_content(source):
    # Check if source is a URL
    if urlparse(source).scheme in ('http', 'https'):
        try:
            response = requests.get(source)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error: Could not retrieve data from URL '{source}'.\n{e}")
            return None
    else:
        # Assume source is a filename
        try:
            with open(source, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{source}' was not found.")
            return None

# ... [rest of your functions remain the same]

def main():
    # ... [rest of your main function remains the same]

    source = input("Please provide filename or URL: ")
    content = load_content(source)

    if content is None:
        return

    mixed_data = find_mixed_data(client_name, content, client_keywords)
    # ... [rest of your main function remains the same]

if __name__ == "__main__":
    main()
