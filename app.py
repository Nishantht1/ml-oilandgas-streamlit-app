import streamlit as st
import pandas as pd
import joblib

st.title("Oil, Gas, and Water Volume Prediction App")

# --- Dropdown for target selection ---
st.sidebar.header("Prediction Target")
target_choice = st.sidebar.selectbox(
    "What do you want to predict?",
    ("BORE_OIL_VOL", "BORE_GAS_VOL", "BORE_WAT_VOL")
)

# --- Select corresponding model based on dropdown ---
model_file = {
    "BORE_OIL_VOL": "oil_volume_model_tuned.pkl",
    "BORE_GAS_VOL": "gas_volume_model.pkl",
    "BORE_WAT_VOL": "water_volume_model.pkl"
}[target_choice]

model = joblib.load(model_file)

# --- Input features ---
st.subheader(f"Enter input features for {target_choice}")

avg_whp = st.number_input("AVG_WHP_P", min_value=0.0)
choke_size = st.number_input("AVG_CHOKE_SIZE_P", min_value=0.0)
avg_wht = st.number_input("AVG_WHT_P", min_value=0.0)

flow_kind = st.selectbox("FLOW_KIND", ['production', 'injection'])
flow_encoded = 1 if flow_kind == 'production' else 0

input_data = pd.DataFrame([{
    'AVG_WHP_P': avg_whp,
    'AVG_CHOKE_SIZE_P': choke_size,
    'AVG_WHT_P': avg_wht,
    'FLOW_KIND_ENCODED': flow_encoded
}])

# --- Predict button ---
if st.button("Predict"):
    result = model.predict(input_data)[0]
    st.success(f"Predicted {target_choice}: {result:.2f}")

# --- Batch prediction ---
st.subheader("📁 Batch Prediction from CSV")

uploaded_file = st.file_uploader("Upload CSV with required features", type=["csv"])

if uploaded_file is not None:
    batch_df = pd.read_csv(uploaded_file)

    expected_cols = ['AVG_WHP_P', 'AVG_CHOKE_SIZE_P', 'AVG_WHT_P', 'FLOW_KIND_ENCODED']
    if all(col in batch_df.columns for col in expected_cols):
        batch_df['Predicted_' + target_choice] = model.predict(batch_df[expected_cols])
        st.success("✅ Batch predictions completed")
        st.dataframe(batch_df)

        csv = batch_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name=f"{target_choice}_predictions.csv", mime='text/csv')
    else:
        st.error(f"CSV must contain these columns: {expected_cols}")
