import streamlit as st

st.set_page_config(page_title="Portfólio Acadêmico", layout="wide")

# Menu lateral
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ("Bem-Vindo",
     "Quem sou eu",
     "Competências",
     "Certificações",
     "Experiência",
     "Projeto Acadêmico")
)

# 🔹 Mensagem padrão (sempre aparece primeiro)
if opcao is None:
    st.title("👋 Seja Bem-Vindo")
    st.write("""
    Seja bem-vindo ao meu portfólio acadêmico.

    Neste ambiente você poderá conhecer um pouco mais sobre mim,
    minhas competências, certificações e projetos desenvolvidos.

    Utilize o menu ao lado esquerdo para navegar.
    É um prazer tê-lo(a) por aqui.
    """)

# 1️⃣ Quem sou eu
elif opcao == "Quem sou eu":
    st.title("👨‍💻 Quem sou eu")
    st.write("""
    Sou estudante de Análise e Desenvolvimento de Sistemas (3º semestre),
    com interesse em tecnologia aplicada ao mercado financeiro.
    Busco desenvolver soluções eficientes utilizando programação e análise de dados.
    """)

# 2️⃣ Competências
elif opcao == "Competências":
    st.title("💡 Competências")
    st.write("""
    - Desenvolvimento de sistemas
    - Banco de dados (nível básico/intermediário)
    - Análise de dados com Python
    - Fundamentos de mercado financeiro
    - Matemática financeira (intermediária)
    - Comunicação profissional
    - Trabalho em equipe
    """)

# 3️⃣ Certificações
elif opcao == "Certificações":
    st.title("📜 Certificações")
    st.write("""
    - CPA-20 – ANBIMA
    - Processo de migração para C-Pro R
    - Microcertificações ANBIMA:
        • Mercado Financeiro
        • Fundos de Investimento
        • Renda Variável
        • ESG
    """)

# 4️⃣ Experiência
elif opcao == "Experiência":
    st.title("💼 Experiência")
    st.write("""
    Experiência em organização de processos, atendimento e rotina operacional.
    Desenvolvimento acadêmico focado em lógica, modelagem e estruturação de sistemas.
    """)

# 5️⃣ Projeto Acadêmico
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")
    st.write("""
    Sistema desenvolvido do zero aplicando conceitos de programação,
    lógica, modelagem e design de interface.
    """)

    st.subheader("🎥 Vídeo Demonstrativo")
    st.video("https://youtu.be/seu_link_aqui")

    st.subheader("🖼️ Imagens do Projeto")
    st.image("imagens/tela1.png", caption="Tela Inicial")
