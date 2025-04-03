# Automated UI Testing Framework with GenAI Integration

## Project Overview
This project automates the process of UI testing by combining web scraping, AI-generated test cases, and AI-generated Selenium scripts. The framework consists of 3 main components:

1. **UI Element Scraper**: Extracts buttons, links, inputs, and forms from a website
2. **AI Test Case Generator**: Creates test scenarios using Gemini
3. **Selenium Script Generator**: Produces executable test scripts from test cases

## Approach
### Task 1: UI Element Extraction
- Used BeautifulSoup to parse static HTML content
- Extracted 4 key UI element types
- Structured output in JSON format

### Task 2: Test Case Generation
- Leveraged Google's Gemini model for test scenario creation
- Developed dynamic prompts based on UI elements
- Formatted output in Excel with auto-adjusting columns

### Task 3: Selenium Script Generation
- Created AI prompts with Selenium best practices
- Enforced explicit waits and proper locator strategies
- Maintained code formatting in Excel output

## Challenges Faced
1. **Dynamic Content Handling**: Initial difficulty with JavaScript-rendered elements
2. **Prompt Engineering**: Required multiple iterations to get consistent AI responses
3. **Excel Formatting**: Maintaining proper code indentation in cells
4. **AI Hallucinations**: Occasional generation of non-existent element locators

## Setup Instructions

### Prerequisites
- Python 3.6+
- Google API Key (for Gemini)
- Chrome Browser
- Basic understanding of Selenium

### Installation
1. Clone repository:
```bash
git clone https://github.com/Karthic-Elangovan/Sodio-Tech.git
cd Sodio-Tech
cd Project
```


2. Install dependencies:
```bash
pip install -r requirements.txt
```


3. Set up environment variables:
```bash
GEMINI_API_KEY = your_api_key_here > .env
```


## Usage
1. **Scrape UI Elements**:
```bash
python scraping.py
```


2. **Generate Test Cases**:
```bash
python model.py
```


3. **Generate Selenium Scripts**:
```bash
python SeleniumScript.py
```

## File Structure

```
Projects
├── elements.json            # Extracted UI elements
├── test_cases.xlsx          # Generated test scenarios
├── test_scripts.xlsx        # Generated Selenium scripts
├── scraping.py              # Task 1 script
├── model.py                 # Task 2 script
├── Selenium_Script.py       # Task 3 script
└── requirements.txt         # Dependencies
```
