#  Password Strength Analyzer

A web application that checks the strength of passwords in real-time using both frontend (JavaScript) and backend (Python Flask) logic. It provides detailed recommendations and visual indicators to help users create secure passwords.

##  Features

-  Real-time password strength meter
-  Backend analysis with detailed feedback
-  Frontend recommendations while typing
-  Clean and responsive UI (Bootstrap + custom CSS)
-  Highlights strength with colored progress bars and line indicators

##  Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python, Flask
- **Templating**: Jinja2

##  Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Password-Strength-Analyzer.git
   cd Password-Strength-Analyzer

2. Create a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install flask

4. Run the Flask app:
   python app.py

## How It Works

Backend Analysis:

Checks for length, uppercase, lowercase, numeric, whitespace, and special characters.

Gives textual feedback on what’s missing.

Ranks password on a 0–6 scale with corresponding feedback.

Frontend Meter:

Dynamically updates strength bar and suggestions as user types.

##  Author
Name: Riya Behl



