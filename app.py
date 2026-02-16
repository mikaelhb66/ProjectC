import streamlit as st

st.set_page_config(page_title="Portfólio Acadêmico", layout="wide")

# MENU LATERAL (Projeto Acadêmico primeiro)
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Projeto Acadêmico", "Quem sou eu", "Competências", "Certificações", "Experiência"],
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
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao == "Projeto Acadêmico":
    st.title("🚀 Projeto Acadêmico")

    st.write("""
    Sistema desenvolvido como projeto acadêmico com foco em
    organização, estruturação de interface e aplicação prática
    dos conceitos aprendidos durante o curso.
    """)

    st.markdown("---")

    # 🎥 VÍDEO COM TÍTULO E DESCRIÇÃO
    st.subheader("🎥 Demonstração em Vídeo")
    st.write("Veja abaixo um vídeo demonstrativo do funcionamento do sistema, destacando suas principais funcionalidades.")
    st.video("https://youtu.be/seu_link_aqui")
    st.write("O vídeo mostra a navegação pelo sistema, incluindo telas de cadastro, consulta e relatórios, ilustrando a experiência completa do usuário.")

    st.markdown("---")

    # 🖼️ IMAGENS COM TÍTULO E DESCRIÇÃO
    st.subheader("🖼️ Tela Inicial do Sistema")
    st.image("Tela01.png")
    st.write("Essa é a tela inicial do sistema, mostrando o menu principal e a navegação inicial para o usuário.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela02.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela03.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela04.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela05.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela06.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela07.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela08.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela09.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela10.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela11.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela12.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela14.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela16.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela17.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela19.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela20.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela21.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela22.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela23.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

    st.subheader("🖼️ Tela de Funcionalidades")
    st.image("Tela24.png")
    st.write("Aqui é apresentada a tela de funcionalidades, destacando as principais ações que o usuário pode realizar dentro do sistema.")

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
