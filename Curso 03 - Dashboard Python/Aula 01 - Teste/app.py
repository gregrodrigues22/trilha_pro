import streamlit as st, pandas as pd
st.set_page_config(page_title="Meu App", layout="wide")
st.title("🚀 App Streamlit publicado via GitHub")
st.write("Edite `app.py` e faça `git push` para atualizar o app!!")
st.write("Exemplo de DF:")
st.dataframe(pd.DataFrame({"A":[1,2,3],"B":[4,5,6]}))
