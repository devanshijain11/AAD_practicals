from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Function to calculate the minimum number of coins
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

@app.route('/', methods=['GET', 'POST'])
def index():
    coins = [1, 4, 6]
    amounts = list(range(1, 11))
    results = [min_coins(coins, amount) for amount in amounts]
    
    # Initialize variables
    min_coins_result = None
    user_amount = None

    if request.method == 'POST':
        # Get user input from form
        try:
            user_amount = int(request.form['amount'])
            min_coins_result = min_coins(coins, user_amount)
        except ValueError:
            min_coins_result = "Invalid input. Please enter a valid integer."
    
    # Generate the plot using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(amounts, results, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Amount (Rs.)')
    ax.set_ylabel('Number of Coins')
    ax.set_title('Minimum Coins Required for Various Amounts')
    
    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # Encode image to base64
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return render_template('p5.html', 
                           image_data=img_base64,
                           min_coins_result=min_coins_result,
                           user_amount=user_amount)

if __name__ == '__main__':
    app.run(debug=True)
