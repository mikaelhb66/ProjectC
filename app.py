import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portfólio Acadêmico", layout="wide")

# Menu lateral
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ("", "Quem sou eu", "Competências", "Certificações", "Experiência", "Projeto Acadêmico")
)

# ==============================
# 🔹 TELA INICIAL (AUTOMÁTICA)
# ==============================
if opcao is None:
    st.title("👋 Seja Bem-Vindo")

    st.write("""
    Seja bem-vindo ao meu portfólio acadêmico.

    Neste ambiente você poderá conhecer um pouco mais sobre mim,
    minhas competências, certificações e projetos desenvolvidos
    durante minha formação em Análise e Desenvolvimento de Sistemas.

    Utilize o menu ao lado esquerdo para navegar pelas seções.
    É um prazer tê-lo(a) por aqui.
    """)

    st.markdown("---")
    st.subheader("🎯 Objetivo Profissional")
    st.write("""
    Atuar na área de tecnologia, com foco em desenvolvimento de sistemas
    e soluções aplicadas ao mercado financeiro, contribuindo com
    pensamento analítico e organização.
    """)

# ==============================
# 👨‍💻 QUEM SOU EU
# ==============================
elif opcao == "Quem sou eu":
    st.title("👨‍💻 Quem sou eu")

    st.write("""
    Sou estudante de Análise e Desenvolvimento de Sistemas (3º semestre),
    com interesse em tecnologia aplicada ao mercado financeiro.

    Busco desenvolver soluções eficientes utilizando programação,
    análise de dados e organização estruturada de sistemas.
    """)

# ==============================
# 💡 COMPETÊNCIAS
# ==============================
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

# ==============================
# 📜 CERTIFICAÇÕES
# ==============================
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

# ==============================
# 💼 EXPERIÊNCIA
# ==============================
elif opcao == "Experiência":
    st.title("💼 Experiência")

    st.write("""
    Experiência em organização de processos, atendimento ao cliente
    e rotina operacional.

    Desenvolvimento acadêmico focado em lógica de programação,
    modelagem e estruturação de sistemas.
    """)

# ==============================
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")

    st.write("""
    Sistema desenvolvido do zero aplicando conceitos de programação,
    lógica, modelagem e design de interface.

    O projeto envolveu estruturação da lógica, organização das funções
    e aplicação prática dos conhecimentos adquiridos na graduação.
    """)

    st.markdown("---")

    st.subheader("🎥 Vídeo Demonstrativo")
    st.video("https://youtu.be/seu_link_aqui")

    st.markdown("---")

    st.subheader("🖼️ Imagens do Projeto")

    col1, col2 = st.columns(2)

    with col1:
        st.image("imagens/tela1.png", caption="Tela Inicial")

    with col2:
        st.image("imagens/tela2.png", caption="Funcionalidade Principal")
