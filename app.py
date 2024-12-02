# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the / route (home page)
@app.route('/')
def home():
    return render_template('test.html')


@app.route('/services')
def contact():
    return render_template('services.html')

@app.route('/contacts')
def project():
    return render_template('contacts.html')

@app.route('/research')
def research():
    return render_template('research.html')


@app.route('/latex')
def latex():
    return render_template('latex.html')




# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
