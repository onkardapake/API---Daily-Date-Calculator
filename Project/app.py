''' from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)

def calculate_sum_upto_day(day):
    return sum(range(1, day + 1))

def calculate_mtd_sum(month, year):
    today = date.today()
    if today.month == month and today.year == year:
        return sum(range(1, today.day + 1))
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    today = date.today()
    today_sum = calculate_sum_upto_day(today.day)
    mtd_sum = calculate_mtd_sum(today.month, today.year)
    
    entered_date_sum = None
    entered_date = None
    
    if request.method == 'POST':
        entered_date_str = request.form['date']
        try:
            entered_date = datetime.strptime(entered_date_str, '%Y-%m-%d').date()
            entered_date_sum = calculate_sum_upto_day(entered_date.day)
        except ValueError:
            entered_date_sum = 'Invalid date format. Please enter in YYYY-MM-DD format.'

    return render_template('index.html', today_sum=today_sum, mtd_sum=mtd_sum,
                           entered_date_sum=entered_date_sum, today=today, entered_date=entered_date)

if __name__ == '__main__':
    app.run(debug=True) 

-----------------------------------------------------------------------------------------------

from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)

def calculate_sum_upto_day(day):
    return sum(range(1, day + 1))

def calculate_mtd_sum(month, year):
    today = date.today()
    if today.month == month and today.year == year:
        return sum(range(1, today.day + 1))
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    today = date.today()
    today_sum = calculate_sum_upto_day(today.day)
    mtd_sum = calculate_mtd_sum(today.month, today.year)
    
    entered_date_sum = None
    entered_date = None
    total_4_members_amount = None
    
    if request.method == 'POST':
        entered_date_str = request.form['date']
        try:
            entered_date = datetime.strptime(entered_date_str, '%Y-%m-%d').date()
            entered_date_sum = calculate_sum_upto_day(entered_date.day)
            total_4_members_amount = entered_date_sum * 4
        except ValueError:
            entered_date_sum = 'Invalid date format. Please enter in YYYY-MM-DD format.'

    return render_template('index.html', today_sum=today_sum, mtd_sum=mtd_sum,
                           entered_date_sum=entered_date_sum, total_4_members_amount=total_4_members_amount,
                           today=today, entered_date=entered_date)

if __name__ == '__main__':
    app.run(debug=True) '''


''' 3rd code

from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)

def calculate_sum_upto_day(day):
    return sum(range(1, day + 1))

def calculate_mtd_sum(month, year):
    today = date.today()
    if today.month == month and today.year == year:
        return sum(range(1, today.day + 1))
    return None

def calculate_today_contribution(day):
    return day * 4

def calculate_total_balance(day):
    mtd_contribution_one_person = day
    return mtd_contribution_one_person * 4

@app.route('/', methods=['GET', 'POST'])
def index():
    today = date.today()
    mtd_sum = calculate_mtd_sum(today.month, today.year)
    today_contribution = calculate_today_contribution(today.day)
    total_balance = calculate_total_balance(mtd_sum)
    
    entered_date_sum = None
    entered_date = None
    total_4_members_amount = None
    
    if request.method == 'POST':
        entered_date_str = request.form['date']
        try:
            entered_date = datetime.strptime(entered_date_str, '%Y-%m-%d').date()
            entered_date_sum = calculate_sum_upto_day(entered_date.day)
            total_4_members_amount = entered_date_sum * 4
        except ValueError:
            entered_date_sum = 'Invalid date format. Please enter in YYYY-MM-DD format.'

    return render_template('index.html', mtd_sum=mtd_sum, today_contribution=today_contribution,
                           total_balance=total_balance, entered_date_sum=entered_date_sum,
                           total_4_members_amount=total_4_members_amount, today=today, entered_date=entered_date)

if __name__ == '__main__':
    app.run(debug=True)

    '''

''' 4th code '''

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# For demonstration purposes, assume last month's total balance
# This would typically come from a database or persistent storage
last_month_total_balance = 1860

@app.route('/', methods=['GET', 'POST'])
def index():
    today = datetime.today().strftime('%Y-%m-%d')
    today_date = datetime.today().day
    today_contribution = today_date * 4  # Today's contribution for 4 people is today_date * 4

    mtd_sum = sum(range(1, today_date + 1))
    total_balance = mtd_sum * 4  # Total balance for the current month

    # Calculate the total balance till now
    total_balance_till_now = last_month_total_balance + total_balance

    entered_date_sum = None
    total_4_members_amount = None
    entered_date = None

    if request.method == 'POST':
        entered_date_str = request.form['date']
        try:
            entered_date = datetime.strptime(entered_date_str, '%Y-%m-%d')
            entered_date_sum = sum(range(1, entered_date.day + 1))
            total_4_members_amount = entered_date_sum * 4
        except ValueError:
            entered_date_sum = 'Invalid date format. Please use YYYY-MM-DD.'

    return render_template('index.html', today=today, today_contribution=today_contribution, mtd_sum=mtd_sum,
                           total_balance=today_contribution, total_balance_till_now=total_balance_till_now,
                           entered_date=entered_date, entered_date_sum=entered_date_sum,
                           total_4_members_amount=total_4_members_amount)

if __name__ == '__main__':
    app.run(debug=True)

