from flask import Flask, render_template, request
import string

app = Flask(__name__)

def multiply(value, factor):
    return value * factor

app.jinja_env.filters['multiply'] = multiply

def analyze_password(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    # Check length
    length = len(password)
    if length >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Check character types
    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    # Check strength
    if lower_count >= 1:
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.\n"
    if upper_count >= 1:
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"
    if num_count >= 1:
        strength += 1
    else:
        remarks += "Add at least one numeric character.\n"
    if wspace_count == 0:
        strength += 1
    else:
        remarks += "Avoid using whitespace characters.\n"
    if special_count >= 1:
        strength += 1
    else:
        remarks += "Add at least one special character.\n"

    # Remarks based on strength
    if strength <= 2:
        remarks += "Very Bad Password!! Change ASAP\n"
    elif strength == 3:
        remarks += "Not a good Password!! Change ASAP\n"
    elif strength == 4:
        remarks += "It's a weak Password, consider changing\n"
    elif strength == 5:
        remarks += "It's a hard Password, but can be better\n"
    elif strength == 6:
        remarks += "It's a strong Password\n"

    result = {
        'remarks': remarks,
        'counts': {
            'lowercase': lower_count,
            'uppercase': upper_count,
            'numeric': num_count,
            'whitespace': wspace_count,
            'special': special_count,
            'strength': strength
        }
    }
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.form['password']
    result = analyze_password(password)
    result_text = result['remarks']
    counts = result['counts']
    width_percentage = counts['strength'] * 20
    return render_template('index.html', result=result_text, counts=counts, width_percentage=width_percentage)

if __name__ == '__main__':
    app.run(debug=True)
