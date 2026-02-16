import streamlit as st

st.title("IA - Projeto Acadêmico")

user_input = st.text_input("Digite sua pergunta:")

if user_input:
    if "projeto" in user_input.lower():
        st.write("Este projeto foi desenvolvido do zero utilizando Python.")
    elif "tecnologia" in user_input.lower():
        st.write("Utilizei Python, lógica de programação e conceitos de sistemas.")
    else:
        st.write("Obrigado por visitar meu projeto!")
