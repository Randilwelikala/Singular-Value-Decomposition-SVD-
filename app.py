from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/compute_svd', methods=['POST'])
def compute_svd():
    try:
        # Get matrix from textarea input
        raw_matrix = request.form['matrix']

        # Convert string to numpy matrix
        matrix = np.array([[float(num) for num in row.split()] for row in raw_matrix.strip().split('\n')])

        # Compute SVD
        U, S, VT = np.linalg.svd(matrix)

        return render_template('index.html', U=U, S=S, VT=VT, original=matrix)

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)
