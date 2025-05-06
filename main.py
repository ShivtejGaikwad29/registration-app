from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    print(f"Received: {name}, {email}")
    return render_template('thankyou.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
