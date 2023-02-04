import tempfile
import streamlit as st
import pytesseract
import cv2

def convertImageToText(image):
    imagenew = cv2.imread(image)
    gray = cv2.cvtColor(imagenew, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(thresh,lang="eng")
    return text

st.set_page_config(page_title="Image to Text Convertor",page_icon=":camera:",layout="wide")
st.title("Image To Text Convertor")

uploaded_file = st.file_uploader("Choose an image...",type=["png","jpg","jpeg"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(suffix=".jpg") as f:
        f.write(uploaded_file.read())
        text = convertImageToText(image=f.name)
        st.text("TEXT EXTRACTED FROM THE IMAGE: ")
        st.write(text)
else:
    st.write("Please upload an image to get started")