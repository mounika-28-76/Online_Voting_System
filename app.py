from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/aadhar')
def aadhar():
    return render_template('aadhar.html')

@app.route('/eligibility')
def eligibility():
    voter = {"name": "Mounika", "age": 21, "status": "Eligible"}
    return render_template('eligibility.html', voter=voter)

@app.route('/face')
def face():
    return render_template('face.html')

@app.route('/fingerprint')
def fingerprint():
    return render_template('fingerprint.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
