
# Selenium Automation Script for OPAL Login

## Overview
This Python script uses Selenium to automate the login process for the OPAL education portal at the Technische Universität Dresden. It demonstrates handling web elements, waiting for conditions, and extracting data using regular expressions.

## Features
- **Automated Login**: Automatically fills and submits the login and password fields.
- **Dropdown Selection**: Selects the correct institution from a dropdown menu.
- **Secret Token Extraction**: Extracts and uses secret token values from text using regular expressions.
- **Error Handling**: Includes basic error handling to manage exceptions during the login process.

## Prerequisites
To run this script, you will need Python installed on your system along with the Selenium package and a compatible WebDriver for your browser. The script uses Google Chrome, so you will need the ChromeDriver.

## Dependencies
- Python (3.6 or later recommended)
- Selenium Python package
- ChromeDriver executable

## Installation
### Python and Pip
Ensure Python and pip are installed:

```bash
python --version
pip --version
```

### Selenium Installation
Install Selenium via pip:

```bash
pip install selenium
```

### ChromeDriver
Download the appropriate version of ChromeDriver from ChromeDriver Downloads. Ensure it's in your PATH or specify the path directly in the script.

## Configuration
Before running the script, update the following placeholders in the script:
- `your_username`: Replace with your actual username for the OPAL portal.
- `your_password`: Replace with your password.

## Running the Script
To run the script, use the following command from the terminal:

```bash
python path_to_script.py
```

## Notes
The script includes an infinite loop at the end to prevent it from closing immediately after execution. You may want to adjust this behavior based on your needs.
Always ensure your credentials are secured and not hard-coded in scripts in a production environment.
