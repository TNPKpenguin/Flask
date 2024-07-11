from flask import request, render_template, Flask
from body_shape_prediction import make_prediction 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    weight = request.form['weight']
    height = request.form['height']

    pred = make_prediction(weight, height)
    classification = '%s' % (pred)
    return render_template('index.html', prediction=classification)

if __name__ == "__main__":
    app.run(port=3002, debug=True)