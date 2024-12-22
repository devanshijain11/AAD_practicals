from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

def longest_common_subsequence(P, Q):
    m = len(P)
    n = len(Q)
    
    # Create a DP table
    dp = np.zeros((m + 1, n + 1), dtype=int)

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if P[i - 1] == Q[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Construct the LCS from the DP table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if P[i - 1] == Q[j - 1]:
            lcs.append(P[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()  # Reverse to get the correct order
    return lcs, dp

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get sequences as strings and convert them to lists of characters
        P = list(request.form['sequence1'].strip())
        Q = list(request.form['sequence2'].strip())
        
        lcs, dp_table = longest_common_subsequence(P, Q)

        return render_template('p8.html', sequence1=P, sequence2=Q, lcs=lcs, dp_table=dp_table)
    
    return render_template('p8.html', sequence1=None, sequence2=None)

if __name__ == '__main__':
    app.run(debug=True)
