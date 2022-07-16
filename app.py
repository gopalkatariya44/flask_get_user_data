from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        result = request.form
        hobbies = request.form.getlist('hobbies')
        print(hobbies)
        return render_template('data.html', result=result, hobbies=hobbies)


if __name__ == "__main__":
    app.run(debug=True)
