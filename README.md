# 🛢️ Oil Volume Prediction App

This is a full-stack machine learning project to predict oil production volume (`BORE_OIL_VOL`) from oil well sensor data. It includes:

* Data cleaning and feature engineering
* Model training using Random Forest
* Deployment via Streamlit + Render
* Hosted from Jupyter on AWS EC2

---

## 🔗 Live Demo

👉 [Deployed Streamlit App](https://ml-oilandgas-streamlit-app.onrender.com)

---

## ⚙️ Tech Stack

| Area           | Tools Used                   |
| -------------- | ---------------------------- |
| ML Model       | Python, Scikit-learn, Pandas |
| Notebook       | Jupyter on AWS EC2 (Ubuntu)  |
| UI             | Streamlit                    |
| Deployment     | GitHub + Render (Free Tier)  |
| CLI & Transfer | Git Bash, SSH, SCP           |

---

## 📁 Project Structure

```
ml-oilandgas-streamlit-app/
├── app.py                  # Streamlit web app
├── oil_volume_model.pkl    # Trained ML model
├── load_s3_data.ipynb      # Notebook for EDA + training
└── requirements.txt        # Required packages
```

---

## 🧪 Local Setup Instructions

```bash
git clone https://github.com/yourusername/ml-oilandgas-streamlit-app.git
cd ml-oilandgas-streamlit-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🚀 Deployment (Render)

* Connect GitHub repo to [https://render.com](https://render.com)
* Use these commands:

  * **Build Command**: `pip install -r requirements.txt`
  * **Start Command**: `streamlit run app.py --server.headless true`
* Set instance type to **Free**
* Deploy → You’ll get a public link

---

## 📷 Screenshot
****![image](https://github.com/user-attachments/assets/035485fc-5eee-404c-8288-6a0b6a75d8eb)


---

## ✍️ Author

Nishanth

---

## 📜 License

For educational/demo purposes only.
