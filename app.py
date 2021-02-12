from flask import Flask, request, render_template_string
import time
from datetime import datetime
import random

app = Flask(__name__)

# Credentials
USERNAME = "biaz"
PASSWORD = "tom123"
SECURITY_QUESTION = "Le nom de mon chat préféré?"
SECURITY_ANSWER = "tom"

# HTML Templates with CSS
LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        .center-form {
            margin: auto;
            width: 50%;
            border: 3px solid green;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="center-form">
        <h1>Login</h1>
        <form method="post" action="/login">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
        {{ message|safe }}
    </div>
</body>
</html>
'''

BRUTE_FORCE_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Brute Force Simulation</title>
    <style>
        .center-form {
            margin: auto;
            width: 50%;
            border: 3px solid red;
            padding: 10px;
            text-align: center;
        }
        .attempts-container {
            text-align: left;  /* Aligns text to the left */
        }
        .attempt {
            color: red;
        }
        .success {
            color: green;
        }
    </style>
</head>
<body>
    <div class="center-form">
        <h1>Brute Force Attack Simulation</h1>
        <form method="post" action="/brute-force">
            Username for brute force: <input type="text" name="username"><br><br>
            <input type="submit" value="Start Brute Force Attack">
        </form>
        <div class="attempts-container">{{ attempts|safe }}</div>
    </div>
</body>
</html>
'''

FORGOT_PASSWORD_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Forgot Password</title>
    <style>.center-form {margin: auto;width: 50%;border: 3px solid blue;padding: 10px;text-align: center;}</style>
</head>
<body>
    <div class="center-form">
        <h1>Forgot Password</h1>
        <form method="post" action="/forgot-password">
            Enter your username: <input type="text" name="username"><br><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
'''

SECURITY_QUESTION_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Security Question</title>
    <style>
        .center-form {{
            margin: auto;
            width: 50%;
            border: 3px solid orange;
            padding: 10px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="center-form">
        <h1>Security Question</h1>
        <p>{}</p>
        <form method="post" action="/security-question">
            Answer: <input type="text" name="answer"><br><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
'''.format(SECURITY_QUESTION)


RESET_PASSWORD_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Reset Password</title>
    <style>.center-form {margin: auto;width: 50%;border: 3px solid green;padding: 10px;text-align: center;}</style>
</head>
<body>
    <div class="center-form">
        <h1>Reset Password</h1>
        <form method="post" action="/reset-password">
            New Password: <input type="password" name="new_password"><br><br>
            Confirm Password: <input type="password" name="confirm_password"><br><br>
            <input type="submit" value="Reset Password">
        </form>
    </div>
</body>
</html>
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            message = '<p>Login successful!</p>'
        else:
            message = '<p>Login failed!</p>'
    return render_template_string(LOGIN_PAGE + '<br><a href="/forgot-password">Forgot Password</a>', message=message)




@app.route('/brute-force', methods=['GET', 'POST'])
def brute_force():
    attempts_html = ""
    if request.method == 'POST':
        username = request.form['username']
        with open('common_passwords.txt', 'r') as file:
            common_passwords = [line.strip() for line in file]

        random.shuffle(common_passwords)  # Randomize the order of passwords

        for i, password in enumerate(common_passwords, 1):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if username == USERNAME and password == PASSWORD:
                attempts_html += f'<p class="success">Attempt {i}: {password} at {timestamp} → successful</p>'
                break
            else:
                attempts_html += f'<p class="attempt">Attempt {i}: {password} at {timestamp} → failed</p>'
                time.sleep(0.01)  # Simulating delay
    return render_template_string(BRUTE_FORCE_PAGE, attempts=attempts_html)


@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']
        if username == USERNAME:
            return render_template_string(SECURITY_QUESTION_PAGE)
        else:
            return render_template_string(FORGOT_PASSWORD_PAGE + '<p>Username not valid.</p>')
    return render_template_string(FORGOT_PASSWORD_PAGE)

@app.route('/security-question', methods=['POST'])
def security_question():
    answer = request.form['answer']
    if answer.lower() == SECURITY_ANSWER.lower():
        return render_template_string(RESET_PASSWORD_PAGE)
    else:
        return render_template_string(SECURITY_QUESTION_PAGE + '<p>Error: Incorrect answer.</p>')

@app.route('/reset-password', methods=['POST'])
def reset_password():
    global PASSWORD  # This should be handled more securely in a real application
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    if new_password == confirm_password:
        PASSWORD = new_password
        return '<p>Password has been reset successfully. <a href="/login">Return to login</a></p>'
    else:
        return render_template_string(RESET_PASSWORD_PAGE + '<p>Passwords do not match.</p>')

@app.route('/')
def home():
    return '<p><a href="/login">Login Page</a></p><p><a href="/brute-force">Brute Force Page</a></p>'

if __name__ == "__main__":
    app.run(debug=True)