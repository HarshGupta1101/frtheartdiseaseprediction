from flask import Flask, render_template, request
import azure

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("main.html")

@app.route("/predict")
def predict():
    return render_template("prediction.html")

@app.route('/predictresult/', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        return f"The URL /predictresult is accessed directly. Try going to '/predict' to submit form"

    if request.method == 'POST':
        age = request.form.get('age')
        gender = request.form.get('gender')
        cp = request.form.get('cp')
        trestbps = request.form.get('trestbps')
        chol = request.form.get('chol')
        fbs = request.form.get('fbs')
        restecg = request.form.get('restecg')
        thalach = request.form.get('thalach')
        exang = request.form.get('exang')
        oldpeak = request.form.get('oldpeak')
        slope = request.form.get('slope')
        ca = request.form.get('ca')
        thal = request.form.get('thal')
        gender1 = request.form.get('gen')
        cp1 = request.form.get('chp')
        fbs1 = request.form.get('fb')
        restecg1 = request.form.get('rer')
        exang1 = request.form.get('eia')
        slope1 = request.form.get('slo')
        thal1 = request.form.get('tha')
        result = azure.userData(age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        return render_template('results.html', form_data=[result,age,gender1,cp1,trestbps,chol,fbs1,restecg1,thalach,exang1,oldpeak,slope1,ca,thal1])

if __name__ == '__main__':
    app.run(debug=True)
