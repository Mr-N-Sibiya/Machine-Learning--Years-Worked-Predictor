import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from flask import Flask,request, jsonify, render_template
#create flask here
app = Flask(__name__)


#load the pickle Model
model =pickle.load(open("finalized_mode.pkl","rb"))


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/predict",methods = ['POST','GET'])
def predict():
        features =request.form.values()
        output=[np.array(features)]
        prediction = model.predict([output])
        prediction=float(prediction)
        return render_template("login.html", prediction_text=" Salary is{}".format(prediction))

if __name__ == '__main__':
   app.run(debug = True)
