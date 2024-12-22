# to create virtual environment : python -m venv venv
# to activate virtual environment : .\venv\Scripts\activate
# to run : python filename.py


from flask import Flask, render_template, request

app = Flask(__name__)

# Define a function to calculate comparison points
def compare_points(a, b):
    points_chef1 = 0
    points_chef2 = 0
    
    for i in range(3):  # Since there are 3 categories
        if a[i] > b[i]:
            points_chef1 += 1
        elif a[i] < b[i]:
            points_chef2 += 1
    
    return points_chef1, points_chef2

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a_presentation = int(request.form['a_presentation'])
        a_taste = int(request.form['a_taste'])
        a_hygiene = int(request.form['a_hygiene'])
        
        b_presentation = int(request.form['b_presentation'])
        b_taste = int(request.form['b_taste'])
        b_hygiene = int(request.form['b_hygiene'])
        
        # Create tuples for ratings of Chef 1 and Chef 2
        a = (a_presentation, a_taste, a_hygiene)
        b = (b_presentation, b_taste, b_hygiene)
        
        # Calculate comparison points
        points_chef1, points_chef2 = compare_points(a, b)
        
        return render_template('result.html', points_chef1=points_chef1, points_chef2=points_chef2)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
