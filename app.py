import streamlit as st

st.set_page_config(page_title="Projeto Acadêmico", layout="wide")

# Título principal
st.title("Projeto Acadêmico – Sistema Desenvolvido do Zero")

# Apresentação
st.header("👨‍💻 Sobre o Desenvolvedor")
st.write("""
Sou estudante de Análise e Desenvolvimento de Sistemas (3º semestre),
com interesse em desenvolvimento de software e tecnologia aplicada ao mercado financeiro.
Este projeto foi desenvolvido como parte da disciplina acadêmica,
aplicando conceitos de lógica de programação, modelagem e design de interface.
""")

# Sobre o projeto
st.header("📌 Sobre o Projeto")
st.write("""
O sistema foi desenvolvido do zero, incluindo:
- Estruturação da lógica do sistema
- Desenvolvimento da interface
- Aplicação de conceitos de programação
- Organização e modelagem das funcionalidades
""")

# Vídeo demonstrativo
st.header("🎥 Vídeo Demonstrativo")
st.video("https://www.youtube.com/seu_video_aqui")

# Imagens do projeto
st.header("🖼️ Imagens do Sistema")

col1, col2 = st.columns(2)

with col1:
    st.image("imagens/tela1.png", caption="Tela Inicial")

with col2:
    st.image("imagens/tela2.png", caption="Funcionalidade Principal")

# Se quiser manter um mini chat
st.header("🤖 Assistente do Projeto")

user_input = st.text_input("Digite sua pergunta:")

if user_input:
    if "projeto" in user_input.lower():
        st.write("Este projeto foi desenvolvido utilizando Python e conceitos de sistemas.")
    elif "tecnologia" in user_input.lower():
        st.write("Foram utilizados Python e fundamentos de desenvolvimento de software.")
    else:
        st.write("Obrigado por visitar meu projeto!")
