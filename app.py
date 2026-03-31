import streamlit as st

st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# MENU LATERAL (Projeto Acadêmico primeiro)
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Seja Bem-Vindo", "Quem sou eu", "Certificações", "Obrigado"],
)

# ==============================
# 🔹 TELA INICIAL (AUTOMÁTICA)
# ==============================
if opcao == "Seja Bem-Vindo":
    st.title("👋 Seja Bem-Vindo")

    st.write("""
    Aqui você poderá conhecer minhas competências, certificações e projetos desenvolvidos durante
    minha formação em Análise e Desenvolvimento de Sistemas (3º semestre), demonstrando minhas
    habilidades em desenvolvimento de sistemas, análise de dados e soluções tecnológicas.

    Navegue pelo menu lateral para explorar minhas capacidades.
    """)

    st.markdown("---")
    st.subheader("🎯 Objetivo Profissional")
    st.write("""
    Atuar na área de tecnologia, com foco em desenvolvimento de sistemas e soluções voltadas ao
    mercado financeiro, aplicando conhecimentos técnicos, boas práticas de programação e inovação
    em projetos.
    """)

# ==============================
# 👨‍💻 QUEM SOU EU
# ==============================
elif opcao == "Quem sou eu":
    st.title("👨‍💻 Olá! Sou Mikael, 23 anos – prazer em conhecê-lo(a)")
    
    st.write("""
    Estudante de Análise e Desenvolvimento de Sistemas (3º semestre), com conhecimentos em lógica de programação, banco de dados e análise de dados. Certificado CPA-20 (ANBIMA) e em processo de migração para C-Pro R, agregando visão de mercado financeiro e produtos de investimento. Perfil analítico, organizado e orientado à solução de problemas, com interesse em atuar em tecnologia aplicada ao setor financeiro.
    """)
    
    st.write("Competências Técnicas:")
    st.write("""
    - Lógica de programação.  
    - Noções de desenvolvimento de sistemas.
    - Banco de dados (nível básico/intermediário).
    - Análise de dados com Python.
    - Fundamentos de mercado financeiro.
    - Matemática financeira.
    """)

    st.write("Competências Comportamentais:")
    st.write("""
    - Pensamento analítico.  
    - Organização e gestão de rotina.  
    - Comunicação profissional.  
    - Trabalho em equipe.  
    - Proatividade e aprendizado contínuo.  
    """)

# ==============================
# 📜 CERTIFICAÇÕES
# ==============================
elif opcao == "Certificações":
    st.title("📜 Certificações")

    st.subheader("Análise de Dados com Python")
    st.image("Certi (8).png")
    st.write("Faculdade Anhanguera | Sorocaba/SP — 2025")

    st.subheader("Matemática Financeira para Análise de Riscos")
    st.image("Certi (2).png")
    st.write("Faculdade Anhanguera | Sorocaba/SP — 2025")

    st.subheader("Planejamento e Desenvolvimento de Negócios Internacionais")
    st.image("Certi (9).png")
    st.write("Faculdade Anhanguera | Sorocaba/SP — 2025")

    st.subheader("CPA-20")
    st.image("Certi (6).png")
    st.write("Certificação válida até 22/01/2028 — ANBIMA | Sorocaba/SP — 2025")

    st.subheader("CPA")
    st.image("Certi (0).png")
    st.write("Processo Migração em andamento — ANBIMA | Sorocaba/SP — 2026")

    st.subheader("C-Pro R")
    st.image("Certi (0).png")
    st.write("Processo Migração em andamento — ANBIMA | Sorocaba/SP — 2026")

# ==============================
# 💼 Obrigado
# ==============================
elif opcao == "Obrigado":
    st.title("🙏 Obrigado")

    st.write("""
    Agradeço por dedicar seu tempo para conhecer meu portfólio e minhas certificações.
    Espero que as informações apresentadas possam demonstrar minhas habilidades, dedicação
    e interesse em continuar aprendendo e desenvolvendo soluções tecnológicas.
    """)
    st.image("Adeus2.png")
