from PIL import Image
import google.generativeai as genai
import pdf2image
import io
import os
import streamlit as st
import base64
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key="AIzaSyCO4lF2U3tjwv5myTkqH1LUBWaWuwuedis")


def get_gemini_response(input, pdf_cotent, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read(
        ), poppler_path=r"C:\Program Files (x86)\poppler\Library\bin")

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",

                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App


st.set_page_config(page_title="Resume ATS Cheaker", page_icon="🔍")
st.header(" ProTrack.ai [ATS]  ")
# st.page_icon = "https://example.com/my-custom-icon.png"
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Your Resume In PDF", type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("   1... Tell Me How  is My Resume")


submit3 = st.button("2...  Percentage matching ")


input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
        #  from hear desineing part is starting

# Add Footer
# Create a Custom Header

footer = """
<style>
footer {
    visibility: hidden;
}
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #f5f5f5;
    color: #000;
    text-align: center;
    padding: 10px 0;
    font-size: 12px;
}
</style>
<div class="footer">
    ProTrack created by<strong> Raginee Darade</strong>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
