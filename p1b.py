from flask import Flask, render_template, request

app = Flask(__name__)

def closest_pairs_sum(numbers):
    min_sum = float('inf')
    closest_pairs = []
    
    n = len(numbers)
    # Generate all possible Pair
    for i in range(n):
        for j in range(i + 1, n):
            pair = (numbers[i], numbers[j])
            current_sum = sum(pair)
            if abs(current_sum) < abs(min_sum):
                # if true it will update sum and reset the value of min sum
                min_sum = current_sum
                closest_pairs = [pair]
                # else if it will append the pair into closest_pair array
            elif abs(current_sum) == abs(min_sum):
                closest_pairs.append(pair)
    
    return closest_pairs

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            input_string = request.form['numbers']
            # store the string input into list
            numbers = list(map(int, input_string.split(',')))
            pairs = closest_pairs_sum(numbers)
            # to print the pairs and join the string pairs also fomatting the pairs.
            result = ' & '.join([f'{p[0]}, {p[1]}' for p in pairs])
        except ValueError:
            result = 'Invalid input. Please enter a comma-separated list of numbers.'
    
    return render_template('array.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
