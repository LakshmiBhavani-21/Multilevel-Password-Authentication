from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import random
import string
import time
import os

app = Flask(__name__)
app.secret_key = 'yoursecretkey'

# File upload config
UPLOAD_FOLDER = 'files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'xlsx'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Dummy user data
users = {}

# OTP store
otp_store = {}

# Home / Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('otp'))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        security_q = request.form['security_q']
        security_a = request.form['security_a']
        symbol = request.form['symbol']
        hashed_password = generate_password_hash(password)
        users[username] = {
            'password': hashed_password,
            'security_q': security_q,
            'security_a': security_a,
            'symbol': symbol
        }
        msg = "Your registration is completed."
        return render_template('register.html', msg=msg)
    return render_template('register.html', msg=msg)

# OTP generation
@app.route('/otp', methods=['GET', 'POST'])
def otp():
    username = session.get('username')
    error = None
    otp_code = None
    if request.method == 'GET':
        if not username:
            return redirect(url_for('login'))
        otp_code = ''.join(random.choices(string.digits, k=6))
        otp_store[username] = {'otp': otp_code, 'expiry': time.time() + 30}
        return render_template('otp.html', otp_code=otp_code, error=error)
    else:
        user_otp = request.form['otp']
        data = otp_store.get(username)
        if not data:
            error = "OTP Invalid or expired"
        else:
            otp_code = data['otp']
            expiry = data['expiry']
            if time.time() > expiry:
                error = "OTP Expired"
            elif user_otp != otp_code:
                error = "OTP Incorrect"
        if error:
            return render_template('otp.html', otp_code=otp_code, error=error)
        else:
            return redirect(url_for('security_question'))

# Security question level
@app.route('/security_question', methods=['GET', 'POST'])
def security_question():
    username = session.get('username')
    user = users.get(username)
    error = None
    if request.method == 'POST':
        answer = request.form['answer']
        if answer == user['security_a']:
            return redirect(url_for('symbol'))
        else:
            error = "Wrong Security Answer"
    return render_template('security_question.html', question=user['security_q'], error=error)

# Symbol recognition level
@app.route('/symbol', methods=['GET', 'POST'])
def symbol():
    username = session.get('username')
    user = users.get(username)
    error = None
    symbols = ['🌟', '🔥', '🌈', '💧']
    if request.method == 'POST':
        selected_symbol = request.form['symbol']
        stored_symbol = user['symbol']
        if selected_symbol == stored_symbol:
            return redirect(url_for('dashboard'))
        else:
            error = "Wrong Symbol! Please try again."
    return render_template('symbol_recognition.html', symbols=symbols, error=error)

# Dashboard route with file listing and upload
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Handle file upload
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect(url_for('dashboard'))
        else:
            flash('File type not allowed')
            return redirect(request.url)

    files_list = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('dashboard.html', username=username, files=files_list)

# File download route
@app.route('/download/<filename>')
def download_file(filename):
    if "username" not in session:
        return redirect(url_for('login'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# File delete route
@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    if "username" not in session:
        return redirect(url_for('login'))
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        flash('File deleted successfully.')
    else:
        flash('File not found.')
    return redirect(url_for('dashboard'))

# Logout route
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
