import streamlit as st
import pandas as pd
import openai
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

import pandas as pd
import matplotlib
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


openai.api_key = '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' 
st.title("hi")
matplotlib.use("TkAgg")
openai_api_key = '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' 
llm = OpenAI(api_token=openai_api_key)
pandas_ai = PandasAI(llm)
uploaded_file = st.file_uploader("upload",type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
    prompt = st.text_area("enter query")
    if st.button("Generate"):
        if prompt:
            with st.spinner("wait for response..."):
                st.write(pandas_ai.run(df, prompt=prompt))
        else:
            st.warning("enter prompt")
