# recommender/model_inference.py
import numpy as np
import pandas as pd

# This should ideally call a trained Merlin model or Triton endpoint
def get_personalized_recommendations(user_id, behavior_data):
    # Placeholder: mimic prediction logic
    # In real case, send data to a Merlin-trained model endpoint
    recommended_items = [
        {"product_id": "101", "name": "AI Smartwatch", "price": "$129"},
        {"product_id": "102", "name": "Wireless Earbuds", "price": "$89"},
        {"product_id": "103", "name": "Fitness Tracker", "price": "$99"},
    ]
    return recommended_items
