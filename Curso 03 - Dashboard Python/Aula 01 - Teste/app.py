import streamlit as st, pandas as pd, plotly.express as px

st.set_page_config(page_title="App Streamlit via GitHub", layout="wide")
st.title("🚀 App Streamlit publicado via GitHub/Streamlit Cloud")
st.write("Edit `app.py` no Colab, depois **git add/commit/push** para atualizar.")

df = pd.DataFrame({
    "Operadora": list("ABCDEFGHIJ"),
    "Valor": [ -10.58, -9.69, -7.16, -5.84, -4.22, -3.96, -3.29, -3.22, -2.60, -2.54 ]
    + [3.62, 3.67, 3.85, 3.85, 4.04, 4.12, 6.42][:0]  # exemplo compacto
})

st.subheader("Tabela de exemplo")
st.dataframe(df, use_container_width=True)

st.subheader("Barras horizontais (Plotly)")
fig = px.bar(df, x="Valor", y="Operadora", orientation="h", title="Exemplo")
st.plotly_chart(fig, use_container_width=True)

st.caption("Modelo mínimo para testar deploy.")
