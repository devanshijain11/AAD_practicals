from flask import Flask, render_template, request
import heapq

app = Flask(__name__)

# Step 1: Define the Huffman tree and codes
def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap)
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    # Build the tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Extract the huffman codes
    huffman_tree = heap[0]
    huffman_codes = {pair[0]: pair[1] for pair in huffman_tree[1:]}
    return huffman_codes

# Step 2: Huffman code and tree for the given characters and frequencies
frequencies = {'A': 0.5, 'B': 0.35, 'C': 0.5, 'D': 0.1, 'E': 0.4, '-': 0.2}
huffman_codes = build_huffman_tree(frequencies)

# Step 3: Define the encoding and decoding functions
def encode_text(text):
    return ''.join(huffman_codes[char] for char in text)

def decode_binary(binary_string):
    # Reverse the huffman codes to decode
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    decoded_text = []
    current_code = ''
    for digit in binary_string:
        current_code += digit
        if current_code in reverse_codes:
            decoded_text.append(reverse_codes[current_code])
            current_code = ''
    return ''.join(decoded_text)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        action = request.form.get('action')
        text_or_binary = request.form.get('input_text_or_binary')

        if action == 'encode':
            result = encode_text(text_or_binary)
        elif action == 'decode':
            result = decode_binary(text_or_binary)
    
    return render_template('p10.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
