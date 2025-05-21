import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('oil_volume_model.pkl')

st.title("Oil Volume Prediction App")
st.markdown("🔮 Enter well parameters to predict expected oil production (BORE_OIL_VOL)")

# Input fields
avg_whp_p = st.number_input("AVG_WHP_P (Wellhead Pressure)", min_value=0.0)
avg_choke_size_p = st.number_input("AVG_CHOKE_SIZE_P", min_value=0.0)
avg_wht_p = st.number_input("AVG_WHT_P (Wellhead Temp)", min_value=0.0)
flow_kind = st.selectbox("FLOW_KIND", ['production', 'injection'])

# Convert to model input
flow_kind_encoded = 1 if flow_kind == 'production' else 0

# Create DataFrame
input_df = pd.DataFrame([{
    'AVG_WHP_P': avg_whp_p,
    'AVG_CHOKE_SIZE_P': avg_choke_size_p,
    'AVG_WHT_P': avg_wht_p,
    'FLOW_KIND_ENCODED': flow_kind_encoded
}])

# Predict
if st.button("Predict Oil Volume"):
    prediction = model.predict(input_df)[0]
    st.success(f"🛢️ Predicted Oil Volume: **{prediction:.2f}** barrels")
