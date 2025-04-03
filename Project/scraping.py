import requests
from bs4 import BeautifulSoup
import json

# Fetch the webpage content
url = 'https://demoblaze.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Structure to hold extracted elements
elements = {
    "buttons": [],
    "links": [],
    "inputs": [],
    "forms": []
}

# Extract buttons
for button in soup.find_all('button'):
    btn_data = {
        "id": button.get('id', ''),
        "classes": button.get('class', []),
        "type": button.get('type', ''),
        "text": button.get_text(strip=True),
        "onclick": button.get('onclick', ''),
        "data-target": button.get('data-target', ''),
        "data-dismiss": button.get('data-dismiss', '')
    }
    elements["buttons"].append(btn_data)

# Extract links (<a> tags)
for link in soup.find_all('a'):
    link_data = {
        "id": link.get('id', ''),
        "classes": link.get('class', []),
        "href": link.get('href', ''),
        "text": link.get_text(strip=True),
        "data-toggle": link.get('data-toggle', ''),
        "data-target": link.get('data-target', '')
    }
    elements["links"].append(link_data)

# Extract input fields
for input_field in soup.find_all('input'):
    input_data = {
        "id": input_field.get('id', ''),
        "type": input_field.get('type', ''),
        "classes": input_field.get('class', []),
        "name": input_field.get('name', ''),
        "placeholder": input_field.get('placeholder', ''),
        "value": input_field.get('value', '')
    }
    elements["inputs"].append(input_data)

# Extract forms
for form in soup.find_all('form'):
    form_data = {
        "id": form.get('id', ''),
        "action": form.get('action', ''),
        "method": form.get('method', ''),
        "classes": form.get('class', []),
        "onsubmit": form.get('onsubmit', '')
    }
    elements["forms"].append(form_data)

# Save the structured data to a JSON file
with open('elements.json', 'w', encoding='utf-8') as f:
    json.dump(elements, f, ensure_ascii=False, indent=2)

print("Elements extracted and saved to elements.json")