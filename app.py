import streamlit as st

st.set_page_config(page_title="Portfólio Acadêmico", layout="wide")

# MENU LATERAL (sem Bem-vindo)
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Quem sou eu", "Competências", "Certificações", "Experiência", "Projeto Acadêmico"],
    index=None
)

# ==============================
# 🔹 TELA INICIAL (AUTOMÁTICA)
# ==============================
if opcao is None:
    st.title("👋 Seja Bem-Vindo")

    st.write("""
    Seja bem-vindo ao meu portfólio acadêmico.

    Aqui você poderá conhecer minhas competências,
    certificações e projetos desenvolvidos durante
    minha formação em Análise e Desenvolvimento de Sistemas.

    Utilize o menu lateral para navegar.
    """)

    st.markdown("---")
    st.subheader("🎯 Objetivo Profissional")
    st.write("""
    Atuar na área de tecnologia com foco em desenvolvimento
    de sistemas e soluções voltadas ao mercado financeiro.
    """)

# ==============================
# 👨‍💻 QUEM SOU EU
# ==============================
elif opcao == "Quem sou eu":
    st.title("👨‍💻 Quem sou eu")
    st.write("""
    Sou estudante de Análise e Desenvolvimento de Sistemas,
    com interesse em tecnologia aplicada ao mercado financeiro.
    """)

# ==============================
# 💡 COMPETÊNCIAS
# ==============================
elif opcao == "Competências":
    st.title("💡 Competências")
    st.write("""
    - Python  
    - Lógica de programação  
    - Banco de dados  
    - Análise de dados  
    - Matemática financeira  
    """)

# ==============================
# 📜 CERTIFICAÇÕES
# ==============================
elif opcao == "Certificações":
    st.title("📜 Certificações")
    st.write("""
    - CPA-20 – ANBIMA  
    - Microcertificações ANBIMA  
    """)

# ==============================
# 💼 EXPERIÊNCIA
# ==============================
elif opcao == "Experiência":
    st.title("💼 Experiência")
    st.write("Descrição da sua experiência profissional.")

# ==============================
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")
    st.write("Descrição do projeto desenvolvido.")

    st.subheader("🎥 Vídeo Demonstrativo")
    st.video("https://youtu.be/seu_link_aqui")

    st.subheader("🖼️ Imagens do Projeto")
    st.image("imagens/tela1.png")
