import streamlit as st
from app.gemini_utils import ask_gemini
from app.vertex_intent_model import classify_intent
from app.image_analysis import analyze_image

st.set_page_config(page_title="Disaster Response Buddy", layout="wide")
st.title("🆘 Disaster Response Buddy")

with st.sidebar:
    st.header("Upload Options")
    input_mode = st.radio("Choose input type:", ["Text", "Image"])

if input_mode == "Text":
    user_input = st.text_area("Ask your emergency-related question:")
    if st.button("Get Help") and user_input:
        intent = classify_intent(user_input)
        response = ask_gemini(user_input, intent)
        st.markdown("### 🤖 AI Response")
        st.write(response)

elif input_mode == "Image":
    uploaded_image = st.file_uploader("Upload an image (e.g., disaster site)", type=["jpg", "png", "jpeg"])
    if uploaded_image and st.button("Analyze Image"):
        analysis = analyze_image(uploaded_image)
        st.markdown("### 📷 Image Analysis")
        st.write(analysis)
