# app.py
from flask import Flask, render_template, request, jsonify
from recommender.model_inference import get_personalized_recommendations

app = Flask(__name__)

# Simulated user behavior store
user_behavior = {}

@app.route('/')
def home():
    user_id = request.args.get('user_id', 'guest_001')
    behavior = user_behavior.get(user_id, {})
    
    # Fetch personalized recommendations
    recommendations = get_personalized_recommendations(user_id, behavior)
    return render_template('index.html', recommendations=recommendations)

@app.route('/track', methods=['POST'])
def track_behavior():
    data = request.json
    user_id = data.get('user_id', 'guest_001')
    product_id = data['product_id']
    
    # Save viewed product (simulated tracking)
    if user_id not in user_behavior:
        user_behavior[user_id] = {"views": []}
    user_behavior[user_id]["views"].append(product_id)

    return jsonify({"status": "tracked"})

if __name__ == '__main__':
    app.run(debug=True)
