from flask import Flask, render_template, request
from model import recommend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    if request.method == 'POST':
        # User Details
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        mobile = request.form.get('mobile', 'N/A')
        email = request.form.get('email', 'N/A')
        previous_issues = request.form.get('previous', 'None')
        symptoms = request.form['symptoms']

        # Medicine recommendation
        result = recommend(symptoms)

        return render_template('result.html',
                               name=name,
                               age=age,
                               gender=gender,
                               mobile=mobile,
                               email=email,
                               previous_issues=previous_issues,
                               result=result)

    return render_template('symptoms.html')

if __name__ == '__main__':
    app.run(debug=True)
