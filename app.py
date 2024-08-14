from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
  
def get_gemini_response(input, image):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input,image])
        return response.text
    except Exception as ex:
        st.error(f"Error: {str(ex)} ")
        return "Unable to Extract information at the moment"

def input_image_details(upload_file):
    if upload_file is not None:
        image = Image.open(upload_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        return image
    return None

st.set_page_config(page_title="GeminiDecode: Multilanguage Document Extrator")

st.markdown("""
<div style="text-align: center;">
    <h2>GeminiDecode: Multilanguage Document Extraction by Gemini Pro</h2>
    <p style="font-family: serif;">
        Utilizing Gemini Pro AI, this project effortlessly extracts vital information 
        from diverse multilingual documents, transcending language barriers with precision 
        and efficiency for enhanced productivity and decision-making.
    </p>
</div>
""", unsafe_allow_html=True)

userInput = st.text_input("tell about image in word: ")
ImgDescription = st.text_area("Description about Image")
upload_file = st.file_uploader("choose an image of document: ", type=["jpg","jpeg","png"])
submit = st.button("Tell me about the document")
input_prompts = f""" You are expert in understanding {userInput} We will upload a image as {userInput} 
and you will have to answer the questions based on the uploaded {userInput} image and here's description about the image {ImgDescription}"""


if submit and upload_file:
    image_data = input_image_details(upload_file)
    if image_data:
        with st.spinner("Processing the document..."):
            response = get_gemini_response(input_prompts, image_data)
            print(response)
            if response:
                st.subheader("Response: ")
                st.write(response)
            else:
                st.error("Failed to extract information from the document. Please try again.")
    else:
        st.warning("Please upload a valid image.")