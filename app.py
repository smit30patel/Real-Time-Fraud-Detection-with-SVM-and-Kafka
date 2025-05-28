import streamlit as st
import pandas as pd
import joblib
import base64

st.set_page_config(page_title="💳 Fraud Detection Dashboard", layout="wide")
st.sidebar.title("📁 Options")
uploaded_file = st.sidebar.file_uploader("Upload test CSV", type=["csv"])
st.title("Real-Time Fraud Detection with SVM")
st.markdown("""
This app allows you to:
- Upload a test dataset
- Run predictions using a pre-trained **SVM model**
- Visualize fraud predictions
- Download the results as CSV
""")
st.markdown(""" Github Repo (https://github.com/smit30patel/Real-Time-Fraud-Detection-with-SVM-and-Kafka)""")

def load_default_data():
    return pd.read_csv("X_test_may28.csv")  

if uploaded_file is not None:
    test_data = pd.read_csv(uploaded_file)
    st.success("✅ Test data uploaded successfully!")
else:
    st.info("ℹ️ No file uploaded. Using default test dataset.")
    test_data = load_default_data()
model = joblib.load("new_svm_model.pkl")
predictions = model.predict(test_data)
result_df = test_data.copy()
result_df['Predicted_isFraud'] = predictions
st.subheader("📊 Prediction Results")
st.dataframe(result_df.head(20), use_container_width=True)
st.subheader("📈 Fraud Prediction Distribution")
fraud_count = result_df['Predicted_isFraud'].value_counts().sort_index()
fraud_count.index = ['Not Fraud (0)', 'Fraud (1)']
st.bar_chart(fraud_count)
csv = result_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ Download Full Prediction Results",
    data=csv,
    file_name='fraud_predictions.csv',
    mime='text/csv'
)
st.markdown("---")
st.markdown("Made By: Smit Patel | Model: SVM")
