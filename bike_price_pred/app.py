#using linear regression model accurace 75%

from flask import  Flask,render_template,request,url_for
import joblib
# libarry to load model joblib

model=joblib.load('model.lb')
#linear reg accuracy 0.75 is not giving correct results

#object to access properties of a class

app=Flask(__name__)

# __name __ not in quotes as it is keyword

# starting mein home page ayga

#create root using decorator

@app.route("/")  #'/' home page
# def index():
#     return "hello   world "

#render_template function search for templates folder to render file
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/project')
def project():
    
    return render_template('project.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        brand_name = request.form['brand_name']
        owner_name=int(request.form['owner'])
        age_bike=int(request.form['age'])
        power_bike= int(request.form['power'])
        kms_driven_bike= int(request.form['kms_driven'])
        # print(brand_name,owner_name,age_bike,power_bike,kms_driven_bike)

        #encoding of bike data as in backend we need to send it as numeric data
        bike_numbers={'TVS': 0,
                        'Royal Enfield': 1,
                        'Triumph': 2,
                        'Yamaha': 3,
                        'Honda': 4,
                        'Hero': 5,
                        'Bajaj': 6,
                        'Suzuki': 7,
                        'Benelli': 8,
                        'KTM': 9,
                        'Mahindra': 10,
                        'Kawasaki': 11,
                        'Ducati': 12,
                        'Hyosung': 13,
                        'Harley': 14,
                        'Jawa': 15,
                        'BMW': 16,
                        'Indian': 17,
                        'Rajdoot': 18,
                        'LML': 19,
                        'Yezdi': 20,
                        'MV': 21,
                        'Ideal': 22}
        brand_name_encode=bike_numbers[brand_name]

        lst=[[kms_driven_bike,owner_name,age_bike,power_bike,brand_name_encode]]  #sequence order
        print(lst)
        pred=model.predict(lst)
        pred = pred[0]
        print("predicted price is ", pred)

        # pred = round(pred, 2)
        user_data = (str(owner_name),str(brand_name),kms_driven_bike,age_bike,power_bike,pred)
        print(user_data)
        return render_template("project.html",prediction=str(pred))

    return render_template('project.html')


if __name__=='__main__':
    app.run(debug=True)
    # debug parameter ?   no need to rerun again to see change your file by default - false


