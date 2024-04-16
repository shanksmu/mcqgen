import os
import json
import traceback
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging
from langchain.callbacks import get_openai_callback


with open("/Users/sbhardwa/Documents/Learning/Machine Learning & AI/Gen AI/mcqgen/response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQs Creator  Application with Lanchain")

with st.form("user_inputs"):
    uploaded_files = st.file_uploader("Upload pdf or txt file")

    mcq_count = st.number_input("No of MCQs", min_value=3, max_value=5)

    subject = st.text_input("Insert Subject", max_chars=20)

    tone = st.text_input("Complexity of the Questions", max_chars=20, placeholder="simple")

    button = st.form_submit_button("Create MCQs")

    if button and uploaded_files is not None and mcq_count and subject and tone:
        with st.spinner("loading.."):
            try:
                text=read_file(uploaded_files)
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject":subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                )
                    
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")

            else:
                logging.info("Entering else statement")
                logging.info(f"Total Tokens:{cb.total_tokens}")
                logging.info(f"Prompt Tokens:{cb.prompt_tokens}")
                logging.info(f"Completion Tokens:{cb.completion_tokens}")
                logging.info(f"Total Cost:{cb.total_cost}")

                logging.info(response)
                if isinstance(response, dict):
                    quiz = response.get("quiz")
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)

                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in table data")

                else:
                    st.write(response)