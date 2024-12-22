
def knapsack(weights,capacity,values):
n = len(Values)
dp = [(capacity+1),(n+1)]

for i in (1,n+1):
    for w in (1,capacity+1):
        if weights[i-1]<w:
            dp[i][w] = max(dp[i-1][w],dp[i-1],[w-weights[i-1]])
        else:
            dp[i][w]= dp[i-1][w]
                        
def index():
        
    weights=[3, 5, 7, 4, 3, 9, 2, 11, 5]
    values=[2, 3, 3, 4, 4, 5, 7, 8, 8]
    capacity=15
    dp=knapsack(weights,capacity,values)

if __name__ == '__main__':
    app.run(debug=True)