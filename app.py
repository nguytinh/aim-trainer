from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for scores (consider using a database for production)
scores = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game')
def index():
    return render_template('index.html')

@app.route('/submit-score', methods=['POST'])
def submit_score():
    data = request.get_json()
    name = data['name']
    score = data['score']
    scores.append({'name': name, 'score': score})
    scores.sort(key=lambda x: x['score'], reverse=True)  # Sort by score
    return jsonify({'message': 'Score submitted'})

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    return render_template('leaderboard.html')  # Render the leaderboard page

@app.route('/api/leaderboard', methods=['GET'])
def api_leaderboard():
    return jsonify(scores[:10])  # Return top 10 scores

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
