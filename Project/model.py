import json
import google.generativeai as genai
import openpyxl
from openpyxl.styles import Font

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyAaSko_ML10ndIOzoK7h3JDIs_nlEBTh6w"  # Replace with your API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Load elements data
with open('elements.json', 'r') as f:
    elements = json.load(f)

# Create prompt for Gemini
prompt = f"""
Analyze this website UI elements data and generate 5 test cases focusing on core functionality.
Include test cases for form submissions, navigation, and key user interactions.

UI Elements Summary:
- Buttons ({len(elements['buttons'])}): Login, Signup, Cart, etc.
- Forms ({len(elements['forms'])}): Contact, Login, Signup forms
- Inputs ({len(elements['inputs'])}): Username, password, message fields
- Links ({len(elements['links'])}): Navigation, product categories, etc.

Format the response as a markdown table with these columns:
| Test Case ID | Test Scenario | Steps to Execute | Expected Result |

Example:
| TC01 | Successful Login | 1. Click Login button<br>2. Enter valid credentials<br>3. Submit form | User is logged in and session is created |
"""

# Generate test cases
response = model.generate_content(prompt)
content = response.text

# Parse the response
test_cases = []
rows = [line.split('|') for line in content.split('\n') if line.startswith('|')]
headers = [h.strip() for h in rows[0][1:-1]]

for row in rows[2:]:  # Skip header and separator rows
    cleaned = [cell.strip() for cell in row[1:-1]]  # Remove empty first/last cells
    test_cases.append({
        headers[0]: cleaned[0],
        headers[1]: cleaned[1],
        headers[2]: cleaned[2].replace('<br>', '\n'),
        headers[3]: cleaned[3]
    })

# Create Excel file
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Test Cases"

# Create header
headers = ["Test Case ID", "Test Scenario", "Steps to Execute", "Expected Result"]
ws.append(headers)

# Add data
for tc in test_cases:
    ws.append([
        tc["Test Case ID"],
        tc["Test Scenario"],
        tc["Steps to Execute"],
        tc["Expected Result"]
    ])

# Formatting
for column in ws.columns:
    max_length = 0
    column = [cell for cell in column]
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2
    ws.column_dimensions[column[0].column_letter].width = adjusted_width

# Save file
wb.save("test_cases.xlsx")
print("Test cases saved to test_cases.xlsx")