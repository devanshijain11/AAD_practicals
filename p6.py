from flask import Flask, render_template, request

app = Flask(__name__)

def matrix_chain_order(dimensions):
    n = len(dimensions) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):  # length of the chain
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def optimal_parenthesization(s, i, j):
    if i == j:
        return f"A{i + 1}"
    else:
        k = s[i][j]
        left = optimal_parenthesization(s, i, k)
        right = optimal_parenthesization(s, k + 1, j)
        return f"({left} x {right})"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dimensions = request.form['dimensions']
        try:
            dimensions = list(map(int, dimensions.split(',')))
            m, s = matrix_chain_order(dimensions)
            min_mult = m[0][len(dimensions) - 2]
            parenthesization = optimal_parenthesization(s, 0, len(dimensions) - 2)
            return render_template('p6.html', min_mult=min_mult, parenthesization=parenthesization, table=m, error=None)
        except ValueError:
            return render_template('p6.html', error="Invalid input. Please enter integers separated by commas.", min_mult=None, parenthesization=None, table=None)

    return render_template('p6.html', min_mult=None, parenthesization=None, table=None, error=None)

if __name__ == '__main__':
    app.run(debug=True)
