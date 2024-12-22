from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def knapsack(capacity, weights, profits):
    n = len(weights)
    dp = np.zeros((n + 1, capacity + 1))

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    max_profit = dp[n][capacity]
    items_selected = []
    w = capacity

    # Find which items were selected
    for i in range(n, 0, -1):
        if max_profit != dp[i - 1][w]:
            items_selected.append(i - 1)
            max_profit -= profits[i - 1]
            w -= weights[i - 1]

    return dp, items_selected, dp[n][capacity]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        W = int(request.form['capacity'])
        n = int(request.form['num_items'])
        profits = list(map(int, request.form['profits'].split(',')))
        weights = list(map(int, request.form['weights'].split(',')))

        dp_table, items_selected, max_profit = knapsack(W, weights, profits)

        # Convert dp_table to a list for easier handling in the template
        dp_table_list = dp_table.tolist()

        return render_template('p7.html', dp_table=dp_table_list, 
                               items_selected=items_selected, 
                               max_profit=max_profit, 
                               num_items=len(items_selected))
    
    return render_template('p7.html', dp_table=None)

if __name__ == '__main__':
    app.run(debug=True)
