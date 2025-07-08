# 🟢 Oil, Gas & Water Volume Prediction App – README

A full‑stack ML project that predicts **oil, gas, and water production volumes** from well‑sensor data.  It covers everything from data ingestion on AWS EC2 to automated deployment on Render.

---

## 🚀 Live Demo

👉 [https://your-app-url.onrender.com](https://ml-oilandgas-streamlit-app.onrender.com)

---

## ⚙️ Tech Stack

| Layer      | Tool / Framework                  |
| ---------- | --------------------------------- |
| Data & EDA |  Pandas, Seaborn (Jupyter on EC2) |
| Models     |  Scikit‑learn (Random Forest)     |
| Serving    |  Streamlit (web UI)               |
| DevOps     |  Git & Git‑Bash ➜ GitHub ➜ Render |

---

## 🧪 How It Works

* **Dropdown** lets users choose which target to predict (`BORE_OIL_VOL`, `BORE_GAS_VOL`, or `BORE_WAT_VOL`).
* Takes three numeric inputs (`AVG_WHP_P`, `AVG_CHOKE_SIZE_P`, `AVG_WHT_P`) and flow type.
* Loads the corresponding `*.pkl` model and returns a prediction.
* Supports **batch CSV upload** and download of results.

---

## 📊 Model Performance

| Target | Hold‑out R² | Hold‑out RMSE | Notes                                                                                                                                   |
| ------ | ----------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Oil    | **0.95**    | 302           | Tuned via 5×5 `GridSearchCV` (`n_estimators = 100`). 5‑fold CV avg ≈ 0.63 due to one outlier fold → future work: GroupKFold by well‑ID. |
| Gas    | 0.94        | 37 893        | Default RF (100 trees).                                                                                                                 |
| Water  | 0.95        | 302           | Default RF (100 trees).                                                                                                                 |

---

## 📁 File Structure

```
.
├── app.py                     # Streamlit UI (dropdown + batch upload)
├── oil_volume_model_tuned.pkl # Tuned oil model
├── gas_volume_model.pkl       # Gas model
├── water_volume_model.pkl     # Water model
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

---

## 💻 Local Setup

```bash
git clone https://github.com/yourname/yourrepo.git
cd yourrepo
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment on Render

| Setting   | Value                                         |
| --------- | --------------------------------------------- |
| **Build** | `pip install -r requirements.txt`             |
| **Start** | `streamlit run app.py --server.headless true` |
| **Plan**  | Free 512 MiB                                  |

Auto‑redeploys on every `git push origin main`.

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/7fbcf579-f363-4f62-a223-ca827247ed67)
---

## ✍️ Author

Nishanth
