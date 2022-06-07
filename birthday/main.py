from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def birthday():
    return render_template('birthday.html')

@app.route('/check_birthday', methods=['POST'])
def check_birthday():
    user_month = request.form['month']
    user_day = request.form['day']
    dt_obj = datetime.now()
    today_month = dt_obj.strftime('%B')
    today_day = dt_obj.strftime('%d')

    check_month = today_month == user_month
    check_day = today_day == user_day

    if check_month and check_day:
        msg = 'Happy birthday!'
        txt = 'Today is your birthday. Spend it doing something you enjoy with those you enjoy being around.'
    else:
        msg = 'It is not your birthday'
        txt = 'Sadly, today is not your birthday. Try again later.'
        
    return render_template('check.html', value=(msg, txt))

@app.route('/about')
def about():
    return render_template("about.html")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)