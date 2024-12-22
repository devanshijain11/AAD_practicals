from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Function for fractional knapsack
# Function for fractional knapsack
def fractional_knapsack(profits, weights, capacity):
    # Calculate the ratio of profit to weight for each item
    ratios = [p / w for p, w in zip(profits, weights)]
    
    # Create list of items with profit, weight, ratio, and index
    items = [(profits[i], weights[i], ratios[i], i) for i in range(len(profits))]
    
    # Sort items based on the ratio (high to low)
    items.sort(key=lambda x: x[2], reverse=True)
    
    # Initialize variables for the selected items
    total_profit = 0.0
    selected_items = [0] * len(profits)
    
    for profit, weight, ratio, idx in items:
        if capacity >= weight:
            # Take the whole item
            capacity -= weight
            total_profit += profit
            selected_items[idx] = 1
        else:
            # Take the fraction of the item
            fraction = capacity / weight
            total_profit += profit * fraction
            selected_items[idx] = fraction
            break
    
    return total_profit, selected_items, items



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input for profits, weights, and capacity
        profits = list(map(int, request.form["profits"].split(',')))
        weights = list(map(int, request.form["weights"].split(',')))
        capacity = int(request.form["capacity"])

        # Get the result from fractional knapsack
        total_profit, selected_items, sorted_items = fractional_knapsack(profits, weights, capacity)
        
        # Prepare data to pass to the template
        ratios = [item[2] for item in sorted_items]
        sorted_items_data = sorted_items
        selected_data = [round(sel, 2) for sel in selected_items]
        
        return render_template(
            "p9.html", 
            profits=profits, 
            weights=weights, 
            capacity=capacity, 
            total_profit=round(total_profit, 2), 
            sorted_items=sorted_items_data, 
            ratios=ratios,
            selected_items=selected_data
        )

    return render_template("p9.html")


if __name__ == "__main__":
    app.run(debug=True)
