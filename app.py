import streamlit as st
import pandas as pd
from file_reader import read_docx, read_pdf
from generator import generate_mcqs

st.title("📘 Note2Quiz - Auto MCQ Generator by Kabir_1000020761")

uploaded_file = st.file_uploader("Upload Notes (PDF / DOCX)")

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = read_pdf(uploaded_file)
    else:
        text = read_docx(uploaded_file)

    st.success("✅ File Uploaded Successfully")

    num = st.slider("How many questions do you want?", 5, 50, 10)

    if st.button("Generate MCQs"):
        with st.spinner("Generating questions..."):
            mcqs = generate_mcqs(text, num)
            st.text_area("MCQs Generated:", mcqs, height=400)

            df = pd.DataFrame({"MCQs": mcqs.split("\n")})
            df.to_csv("question_bank.csv", index=False)

            st.success("✅ Exported to question_bank.csv")
