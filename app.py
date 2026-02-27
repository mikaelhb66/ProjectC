import streamlit as st

st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# ==============================
# 🌐 SELEÇÃO DE IDIOMA
# ==============================
idioma = st.sidebar.selectbox("🌐 Selecione o idioma / Select Language:", ["Português", "English"])

# ==============================
# 📌 MENU LATERAL
# ==============================
menu_pt = ["Seja Bem-Vindo","Projeto Acadêmico","Quem sou eu","Certificações","Experiência","Obrigado"]
menu_en = ["Welcome","Academic Project","About Me","Certifications","Experience","Thank You"]
menu = menu_pt if idioma == "Português" else menu_en

opcao = st.sidebar.radio(
    "Escolha uma opção:" if idioma == "Português" else "Select an option:",
    menu
)

# ==============================
# 📚 TEXTOS BILÍNGUES
# ==============================
texts = {
    "bem_vindo_title": "👋 Seja Bem-Vindo" if idioma=="Português" else "👋 Welcome",
    "bem_vindo_text": """Aqui você poderá conhecer minhas competências, certificações e projetos desenvolvidos durante
    minha formação em Análise e Desenvolvimento de Sistemas (3º semestre), demonstrando minhas
    habilidades em desenvolvimento de sistemas, análise de dados e soluções tecnológicas.

    Navegue pelo menu lateral para explorar minhas capacidades.""" if idioma=="Português" else
    """Here you can explore my skills, certifications, and projects developed during my
    studies in Systems Analysis and Development (3rd semester), showcasing my abilities
    in system development, data analysis, and technological solutions.

    Use the sidebar menu to explore my capabilities.""",
    "objetivo_title": "🎯 Objetivo Profissional" if idioma=="Português" else "🎯 Professional Goal",
    "objetivo_text": """Atuar na área de tecnologia, com foco em desenvolvimento de sistemas e soluções voltadas ao
    mercado financeiro, aplicando conhecimentos técnicos, boas práticas de programação e inovação
    em projetos.""" if idioma=="Português" else
    """Work in the technology area, focusing on system development and solutions aimed at the financial market,
    applying technical knowledge, programming best practices, and innovation in projects.""",
    "quem_sou_title": "👨‍💻 Olá! Sou Mikael, 23 anos – prazer em conhecê-lo(a)" if idioma=="Português" else
                       "👨‍💻 Hi! I'm Mikael, 23 years old – nice to meet you",
    "quem_sou_text": """Estudante de Análise e Desenvolvimento de Sistemas (3º semestre), com conhecimentos em lógica de programação, banco de dados e análise de dados. Certificado CPA-20 (ANBIMA) e em processo de migração para C-Pro R, agregando visão de mercado financeiro e produtos de investimento. Perfil analítico, organizado e orientado à solução de problemas, com interesse em atuar em tecnologia aplicada ao setor financeiro.""" if idioma=="Português" else
                       """Systems Analysis and Development student (3rd semester), with knowledge in programming logic, databases, and data analysis. CPA-20 certified (ANBIMA) and migrating to C-Pro R, gaining financial market insight and investment products. Analytical, organized, problem-solving oriented, with interest in technology applied to the financial sector.""",
    "competencias_tecnicas": """- Lógica de programação  
- Noções de desenvolvimento de sistemas
- Banco de dados (nível básico/intermediário)
- Análise de dados com Python
- Fundamentos de mercado financeiro
- Matemática financeira""" if idioma=="Português" else
                           """- Programming logic  
- Basic system development concepts
- Databases (basic/intermediate)
- Data analysis with Python
- Financial market fundamentals
- Financial mathematics""",
    "competencias_comportamentais": """- Pensamento analítico  
- Organização e gestão de rotina  
- Comunicação profissional  
- Trabalho em equipe  
- Proatividade e aprendizado contínuo""" if idioma=="Português" else
                                     """- Analytical thinking  
- Organization and routine management  
- Professional communication  
- Teamwork  
- Proactivity and continuous learning""",
    "obrigado_title": "🙏 Obrigado" if idioma=="Português" else "🙏 Thank You",
    "obrigado_text": """Agradeço por dedicar seu tempo para conhecer meu portfólio e minhas certificações.
    Espero que as informações apresentadas possam demonstrar minhas habilidades, dedicação
    e interesse em continuar aprendendo e desenvolvendo soluções tecnológicas.""" if idioma=="Português" else
                     """Thank you for taking the time to explore my portfolio and certifications.
                     I hope the information presented demonstrates my skills, dedication, and interest in continuing to learn and develop technological solutions."""
}

# ==============================
# 🔹 FUNÇÃO PARA MOSTRAR IMAGENS COM DESCRIÇÃO
# ==============================
def show_image(title, filename, description):
    st.subheader(title)
    st.image(filename)
    st.write(description)

# ==============================
# 🟢 SEÇÕES DO PORTFÓLIO
# ==============================

# === Seja Bem-Vindo / Welcome
if opcao in ["Seja Bem-Vindo","Welcome"]:
    st.title(texts["bem_vindo_title"])
    st.write(texts["bem_vindo_text"])
    st.markdown("---")
    st.subheader(texts["objetivo_title"])
    st.write(texts["objetivo_text"])

# === Projeto Acadêmico / Academic Project
elif opcao in ["Projeto Acadêmico","Academic Project"]:
    st.title("🚀 Projeto Acadêmico" if idioma=="Português" else "🚀 Academic Project")
    st.write("""Sistema desenvolvido como projeto acadêmico, com foco em organização, 
    estruturação de interface e aplicação prática dos conceitos aprendidos durante o curso. 
    Durante o desenvolvimento, utilizei ferramentas de inteligência artificial para otimizar partes do código, 
    garantindo eficiência, consistência e aderência às melhores práticas de programação.""" if idioma=="Português" else
             """System developed as an academic project, focusing on organization,
             interface structuring, and practical application of concepts learned during the course.
             AI tools were used to optimize parts of the code, ensuring efficiency, consistency, and adherence to best coding practices.""")
    
    st.markdown("---")
    st.subheader("🎥 Demonstração em Vídeo" if idioma=="Português" else "🎥 Video Demonstration")
    st.write("Veja abaixo um vídeo demonstrativo do funcionamento do sistema." if idioma=="Português" else
             "Below is a video demonstration of the system in action.")
    st.video("https://youtu.be/HtYt54H6uNQ")

    # Lista de imagens e descrições (pode expandir conforme necessidade)
    imagens_projeto = [
        ("🖼️ Inicio do Projeto", "Tela01.png", "Desenvolvi este projeto em Python utilizando Visual Studio Code, aplicando boas práticas de programação desde a concepção inicial." if idioma=="Português" else
                                   "I developed this project in Python using Visual Studio Code, applying programming best practices from the initial conception."),
        ("🖼️ Primeira Versão", "Tela02.png", "Criei a primeira versão funcional, priorizando lógica e eficiência, demonstrando habilidade em desenvolvimento backend em Python." if idioma=="Português" else
                                           "I created the first functional version, prioritizing logic and efficiency, demonstrating backend development skills in Python."),
        ("🖼️ Versão Interface", "Tela03.png", "Implementei uma interface inicial, demonstrando capacidade de transformar programas de console em soluções com interação visual." if idioma=="Português" else
                                               "I implemented an initial interface, demonstrating the ability to turn console programs into solutions with visual interaction."),
        # Adicione todas as outras imagens do projeto seguindo este formato...
    ]

    for img in imagens_projeto:
        show_image(*img)

# === Quem sou eu / About Me
elif opcao in ["Quem sou eu","About Me"]:
    st.title(texts["quem_sou_title"])
    st.write(texts["quem_sou_text"])
    st.subheader("Competências Técnicas" if idioma=="Português" else "Technical Skills")
    st.write(texts["competencias_tecnicas"])
    st.subheader("Competências Comportamentais" if idioma=="Português" else "Soft Skills")
    st.write(texts["competencias_comportamentais"])

# === Certificações / Certifications
elif opcao in ["Certificações","Certifications"]:
    st.title("📜 Certificações" if idioma=="Português" else "📜 Certifications")
    certificados = [
        ("Análise de Dados com Python","Certi (8).png","Faculdade Anhanguera | Sorocaba/SP — 2025"),
        ("Matemática Financeira para Análise de Riscos","Certi (2).png","Faculdade Anhanguera | Sorocaba/SP — 2025"),
        ("Planejamento e Desenvolvimento de Negócios Internacionais","Certi (9).png","Faculdade Anhanguera | Sorocaba/SP — 2025"),
        ("CPA-20","Certi (6).png","Certificação válida até 22/01/2028 — ANBIMA | Sorocaba/SP — 2025"),
        ("CPA","Certi (0).png","Processo Migração em andamento — ANBIMA | Sorocaba/SP — 2026"),
        ("C-Pro R","Certi (0).png","Processo Migração em andamento — ANBIMA | Sorocaba/SP — 2026")
    ]
    for c in certificados:
        show_image(*c)

# === Experiência / Experience
elif opcao in ["Experiência","Experience"]:
    st.title("💼 Experiência Profissional" if idioma=="Português" else "💼 Professional Experience")
    experiencias = [
        ("BENASSI SP | Sorocaba/SP — PROMOTOR HORTIFRÚTI — 04/2024 a 01/2026","Exp (1).png",
         "Atuação predominante no turno da madrugada, com apoio eventual no período da manhã..." if idioma=="Português" else
         "Mainly worked the night shift, with occasional morning support..."),
        ("Princesa Supermercado Cosméticos | Sorocaba/SP — ESTOQUISTA (Temporário) — 09/2023 a 01/2024","Exp (3).png",
         "Responsável pela organização e controle de estoque..." if idioma=="Português" else
         "Responsible for organizing and controlling inventory..."),
        # Adicione todas as outras experiências seguindo o mesmo formato
    ]
    for e in experiencias:
        show_image(*e)

# === Obrigado / Thank You
elif opcao in ["Obrigado","Thank You"]:
    st.title(texts["obrigado_title"])
    st.write(texts["obrigado_text"])
    st.image("Adeus2.png")
