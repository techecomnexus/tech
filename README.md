# 🛒 TechEcomNexus – Real-Time AI Product Recommendation Engine

Welcome to **TechEcomNexus**, an advanced AI-powered recommendation engine built using **NVIDIA Merlin** to personalize the eCommerce shopping experience.

> Boost conversions, increase average order value, and reduce bounce rates by delivering smart, real-time product suggestions tailored to each user.

---

## 🎯 Key Benefits

- 🔄 **Increases Average Order Value**  
  By showing highly relevant add-ons or upgrades based on behavior.

- 🚀 **Boosts Conversion Rates**  
  Engaging users with items they’re more likely to purchase.

- 👣 **Reduces Bounce Rates**  
  Delivering immediate relevance keeps visitors engaged longer.

---

## 🧠 Powered by NVIDIA Merlin

Merlin is NVIDIA’s end-to-end framework for building and deploying deep learning recommender systems. It enables lightning-fast training, real-time inference, and seamless integration with production stacks.

---

## 💡 Features

- ✅ Real-time personalized recommendations
- ✅ Built using NVIDIA Merlin, NVTabular, and Transformers4Rec
- ✅ Scalable API powered by Python Flask
- ✅ Frontend-agnostic REST integration (React, HTML, JS)
- ✅ Deployable via Triton Inference Server + Docker
- ✅ Behavior-based tracking for deep user insights

---

## 🛠 Tech Stack

| Layer           | Technology                                |
|----------------|--------------------------------------------|
| Backend API     | Flask (Python)                            |
| AI Engine       | NVIDIA Merlin, NVTabular, Transformers4Rec |
| Inference Host  | NVIDIA Triton Inference Server            |
| Frontend        | JavaScript / React / Preact / HTML        |
| Deployment      | Docker, NGINX, Cloudflare (optional)      |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/TechEcomNexus/ai-recommendation-engine.git
cd ai-recommendation-engine
# Python Dependencies
pip install flask flask-cors
pip install nvidia-pyindex
pip install nvtabular
pip install transformers4rec[tensorflow]  # or [torch]
pip install tritonclient[grpc]
python app.py
docker run --gpus all --rm -p8000:8000 -p8001:8001 -p8002:8002 \
  -v $(pwd)/models:/models nvcr.io/nvidia/tritonserver:latest \
  tritonserver --model-repository=/models
