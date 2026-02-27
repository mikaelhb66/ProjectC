import streamlit as st

# Configuração da página
st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# ==============================
# 🔹 Definição dos textos
# ==============================
textos = {
    "pt": {
        "menu": ["Seja Bem-Vindo","Projeto Acadêmico", "Quem sou eu", "Certificações", "Experiência", "Obrigado"],
        "bem_vindo_titulo": "👋 Seja Bem-Vindo",
        "bem_vindo_texto": """
Aqui você poderá conhecer minhas competências, certificações e projetos desenvolvidos durante
minha formação em Análise e Desenvolvimento de Sistemas (3º semestre), demonstrando minhas
habilidades em desenvolvimento de sistemas, análise de dados e soluções tecnológicas.

Navegue pelo menu lateral para explorar minhas capacidades.
""",
        "objetivo_titulo": "🎯 Objetivo Profissional",
        "objetivo_texto": """
Atuar na área de tecnologia, com foco em desenvolvimento de sistemas e soluções voltadas ao
mercado financeiro, aplicando conhecimentos técnicos, boas práticas de programação e inovação
em projetos.
""",
        "projeto_titulo": "🚀 Projeto Acadêmico",
        "projeto_texto": """
Sistema desenvolvido como projeto acadêmico, com foco em organização, 
estruturação de interface e aplicação prática dos conceitos aprendidos durante o curso. 
Durante o desenvolvimento, utilizei ferramentas de inteligência artificial para otimizar partes do código, 
garantindo eficiência, consistência e aderência às melhores práticas de programação.
""",
        "video_titulo": "🎥 Demonstração em Vídeo",
        "video_desc1": "Veja abaixo um vídeo demonstrativo do funcionamento do sistema.",
        "video_desc2": "O vídeo mostra a navegação pelo sistema, incluindo telas de cadastro, consulta e relatórios, ilustrando a experiência completa do usuário.",
    },

    "en": {
        "menu": ["Welcome","Academic Project", "About Me", "Certifications", "Experience", "Thank You"],
        "bem_vindo_titulo": "👋 Welcome",
        "bem_vindo_texto": """
Here you can explore my skills, certifications, and projects developed during
my studies in Systems Analysis and Development (3rd semester), showcasing my
abilities in system development, data analysis, and technological solutions.

Use the sidebar menu to navigate through my capabilities.
""",
        "objetivo_titulo": "🎯 Professional Objective",
        "objetivo_texto": """
Work in the technology field, focusing on system development and solutions for
the financial market, applying technical knowledge, programming best practices,
and innovation in projects.
""",
        "projeto_titulo": "🚀 Academic Project",
        "projeto_texto": """
Academic project developed focusing on organization, 
interface structuring, and practical application of concepts learned during the course. 
During development, I used artificial intelligence tools to optimize parts of the code, 
ensuring efficiency, consistency, and adherence to programming best practices.
""",
        "video_titulo": "🎥 Video Demonstration",
        "video_desc1": "Below is a demo video demonstrating the system in operation.",
        "video_desc2": "The video shows system navigation, including registration, search, and reporting screens, illustrating the complete user experience.",
    }
}

# ==============================
# 🔹 Seleção de idioma
# ==============================
idioma = st.sidebar.selectbox("🌐 Language / Idioma", ["pt", "en"])

# MENU LATERAL
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:" if idioma == "pt" else "Choose an option:",
    textos[idioma]["menu"],
)

# ==============================
# 🔹 TELA INICIAL
# ==============================
if opcao in ["Seja Bem-Vindo", "Welcome"]:
    st.title(textos[idioma]["bem_vindo_titulo"])
    st.write(textos[idioma]["bem_vindo_texto"])
    st.markdown("---")
    st.subheader(textos[idioma]["objetivo_titulo"])
    st.write(textos[idioma]["objetivo_texto"])

# ==============================
# 🚀 PROJETO ACADÊMICO
# ==============================
elif opcao in ["Projeto Acadêmico", "Academic Project"]:
    st.title(textos[idioma]["projeto_titulo"])
    st.write(textos[idioma]["projeto_texto"])

    st.markdown("---")

    st.subheader(textos[idioma]["video_titulo"])
    st.write(textos[idioma]["video_desc1"])
    st.video("https://youtu.be/HtYt54H6uNQ")
    st.write(textos[idioma]["video_desc2"])

    st.markdown("---")

# ==============================
# 👨‍💻 QUEM SOU EU
# ==============================
elif opcao in ["Quem sou eu", "About Me"]:
    if idioma == "pt":
        st.title("👨‍💻 Olá! Sou Mikael, 23 anos – prazer em conhecê-lo(a)")
        st.write("Estudante de Análise e Desenvolvimento de Sistemas (3º semestre)...")
    else:
        st.title("👨‍💻 Hello! I'm Mikael, 23 years old – nice to meet you")
        st.write("Systems Analysis and Development student (3rd semester)...")

# ==============================
# 📜 CERTIFICAÇÕES
# ==============================
elif opcao in ["Certificações", "Certifications"]:
    st.title("📜 Certificações" if idioma == "pt" else "📜 Certifications")
    st.write("Conteúdo das certificações aqui...")

# ==============================
# 💼 EXPERIÊNCIA
# ==============================
elif opcao in ["Experiência", "Experience"]:
    st.title("💼 Experiência Profissional" if idioma == "pt" else "💼 Professional Experience")
    st.write("Conteúdo da experiência aqui...")

# ==============================
# 🙏 OBRIGADO
# ==============================
elif opcao in ["Obrigado", "Thank You"]:
    st.title("🙏 Obrigado" if idioma == "pt" else "🙏 Thank You")
    st.write(
        "Agradeço por dedicar seu tempo..." if idioma == "pt"
        else "Thank you for taking the time to review my portfolio..."
    )
