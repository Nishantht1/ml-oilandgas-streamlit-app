import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('oil_volume_model.pkl')

st.title("Oil Volume Prediction App")
st.markdown("🔮 Enter well parameters to predict expected oil production (BORE_OIL_VOL)")


st.sidebar.header("Model Settings")
target_choice = st.sidebar.selectbox(
    "Select what to predict:",
    ("BORE_OIL_VOL", "BORE_GAS_VOL", "BORE_WAT_VOL")
)
st.write(f"You selected: {target_choice}")

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


st.header("📁 Batch Prediction from CSV")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    batch_df = pd.read_csv(uploaded_file)
    
    # Optional: display preview
    st.write("Preview of uploaded data:")
    st.dataframe(batch_df.head())

    # Ensure required columns are present
    expected_cols = ['AVG_WHP_P', 'AVG_CHOKE_SIZE_P', 'AVG_WHT_P', 'FLOW_KIND_ENCODED']
    if all(col in batch_df.columns for col in expected_cols):
        batch_preds = model.predict(batch_df[expected_cols])
        batch_df['Predicted_Oil_Volume'] = batch_preds

        st.success("✅ Predictions complete")
        st.dataframe(batch_df)

        # Download link
        csv = batch_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Results CSV", data=csv, file_name='predicted_oil_volume.csv', mime='text/csv')
    else:
        st.error(f"❌ CSV must include columns: {expected_cols}")

