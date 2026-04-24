from flask import Flask, render_template, request
from vaccines import get_schedule

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/scheduler')
def scheduler():
    return render_template('scheduler.html')

@app.route('/result', methods=['POST'])
def result():
    child_name = request.form.get('child_name', 'Your Child')
    age_years = int(request.form.get('age_years', 0) or 0)
    age_months_extra = int(request.form.get('age_months_extra', 0) or 0)
    age_months = (age_years * 12) + age_months_extra
    vaccines_input = request.form.get('vaccines_received', '')
    if vaccines_input.strip() == '':
        vaccines_received = []
    else:
        vaccines_received = [v.strip() for v in vaccines_input.split(',')]
    done, overdue, upcoming = get_schedule(age_months, vaccines_received)
    return render_template('result.html',
        child_name=child_name,
        age_months=age_months,
        done=done,
        overdue=overdue,
        upcoming=upcoming
    )

if __name__ == '__main__':
    app.run(debug=True)