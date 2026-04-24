from flask import Flask, render_template, request
from vaccines import get_schedule

app = Flask(__name__)

@app.route('/')
def home():
    # Just shows the input form (index.html)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Step 1: Get what the user typed in the form
    child_name = request.form.get('child_name', 'Your Child')
    age_months = int(request.form.get('age_months', 0))
    
    # Step 2: Get the list of vaccines already received
    # The form sends them as a comma-separated string e.g. "BCG, OPV-0"
    vaccines_input = request.form.get('vaccines_received', '')
    
    # Step 3: Split by comma and strip extra spaces
    if vaccines_input.strip() == '':
        vaccines_received = []
    else:
        vaccines_received = [v.strip() for v in vaccines_input.split(',')]
    
    # Step 4: Call our vaccines.py brain
    done, overdue, upcoming = get_schedule(age_months, vaccines_received)
    
    # Step 5: Send everything to result.html to display
    return render_template('result.html',
        child_name=child_name,
        age_months=age_months,
        done=done,
        overdue=overdue,
        upcoming=upcoming
    )

if __name__ == '__main__':
    app.run(debug=True)