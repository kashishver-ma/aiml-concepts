#file serve as flaskweb server 

from flask import Flask,render_template,request
import joblib


#importing model

model=joblib.load("model.lb") #using already created model called insurance.ipynb

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict(): 
    print("Form received!")  # 
    if request.method=='POST':
        age = int(request.form['age'])
        children=int(request.form['children'])
        bmi=int(request.form['bmi'])
        smoker= request.form['smoker']
         
        smokermap = {'yes': 1, 'no': 0}
        smoker_encode = smokermap[smoker.lower()]

        print(age, children, bmi, smoker_encode)
       
        print(age,children,bmi,smoker_encode)
        lstt=[[ age     ,bmi,  children , smoker_encode]]
        pred=model.predict(lstt)[0]
     

        print(pred)


    return render_template("index.html",prediction=pred)

if __name__=='__main__':
    app.run(debug=True)




