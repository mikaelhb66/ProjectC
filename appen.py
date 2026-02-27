import streamlit as st

st.set_page_config(page_title="Introducing Mikael", layout="wide")

# SIDE MENU (Academic Project first)
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Choose an option:",
    ["Welcome","Academic Project", "About Me", "Certifications", "Experience", "Thank You"],
)

# ==============================
# 🔹 HOME SCREEN (AUTOMATIC)
# ==============================
if opcao == "Welcome":
    st.title("👋 Welcome")

    st.write("""
    Here you will be able to learn about my skills, certifications, and projects developed during
    my degree in Systems Analysis and Development (3rd semester), demonstrating my
    abilities in systems development, data analysis, and technological solutions.

    Navigate through the side menu to explore my capabilities.
    """)

    st.markdown("---")
    st.subheader("🎯 Professional Goal")
    st.write("""
    To work in the technology field, focusing on systems development and solutions aimed at the
    financial market, applying technical knowledge, programming best practices, and innovation
    in projects.
    """)

# ==============================
# 🚀 ACADEMIC PROJECT
# ==============================
elif opcao == "Academic Project":
    st.title("🚀 Academic Project")

    st.write("""
    System developed as an academic project, focused on organization,
    interface structuring, and practical application of concepts learned during the course.
    During development, I used artificial intelligence tools to optimize parts of the code,
    ensuring efficiency, consistency, and adherence to programming best practices.
    """)

    st.markdown("---")

    # 🎥 VIDEO WITH TITLE AND DESCRIPTION
    st.subheader("🎥 Video Demonstration")
    st.write("Watch below a demonstration video of the system in operation.")
    st.video("https://youtu.be/HtYt54H6uNQ")
    st.write("The video shows navigation through the system, including registration, search, and report screens, illustrating the complete user experience.")

    st.markdown("---")

    # 🖼️ IMAGES WITH TITLE AND DESCRIPTION
    st.subheader("🖼️ Project Beginning")
    st.image("Tela01.png")
    st.write("I developed this project in Python using Visual Studio Code, applying programming best practices from the initial conception.")

    st.subheader("🖼️ First Version")
    st.image("Tela02.png")
    st.write("I created the first functional version, prioritizing logic and efficiency, demonstrating backend development skills in Python.")

    st.subheader("🖼️ Interface Version")
    st.image("Tela03.png")
    st.write("I implemented an initial interface, demonstrating the ability to transform console programs into visually interactive solutions.")

    st.subheader("🖼️ Final Version")
    st.image("Tela04.png")
    st.write("I integrated full functionalities with an intuitive interface, ensuring usability and user experience.")

    st.subheader("🖼️ Features")
    st.image("Tela05.png")
    st.write("I configured and tested all system features, ensuring software reliability and performance.")

    st.subheader("🖼️ Web Version")
    st.image("Tela06.png")
    st.write("I adapted the project for the web, increasing accessibility and enabling multi-platform usage.")

    st.subheader("🖼️ Web Logo")
    st.image("Tela07.png")
    st.write("I developed a visual identity for the project, highlighting attention to design and professional presentation.")

    st.subheader("🖼️ Login")
    st.image("Tela08.png")
    st.write("I explored integration with JavaScript to enhance the web experience, demonstrating versatility in front-end languages.")

    st.subheader("🖼️ Web Features")
    st.image("Tela09.png")
    st.write("At this stage, I began developing functionalities in JavaScript for the web version of the system.")

    st.subheader("🖼️ Feature ")
    st.image("Tela10.png")
    st.write("I organized feature screens highlighting key system actions, focusing on a clear and efficient interface.")

    st.subheader("🖼️ Registration Feature")
    st.image("Tela11.png")
    st.write("I developed the registration screen applying input validations and ensuring data consistency and integrity.")

    st.subheader("🖼️ Search Feature")
    st.image("Tela12.png")
    st.write("I implemented dynamic queries, providing quick access to stored information.")

    st.subheader("🖼️ Google Shell Editor")
    st.image("Tela16.png")
    st.write("I used Google Shell Editor as a cloud execution environment, allowing the system to run on machines with limited resources, ensuring continuity in development, testing, and feature validation.")

    st.subheader("🖼️ Running on Limited System")
    st.image("Tela17.png")
    st.write("I configured the project to run on Linux systems using Docker, ensuring compatibility and development environment isolation.")

    st.subheader("🖼️ Running on Virtual Machine")
    st.image("Tela19.png")
    st.write("I implemented project tests on a virtual machine, validating software portability and proper operation in different environments.")

    st.subheader("🖼️ Consistency and Integrity")
    st.image("Tela20.png")
    st.write("I executed the project, confirming the functionality of implemented features and overall system stability.")

    st.subheader("🖼️ Integrity Assurance in Web Environment ")
    st.image("Tela21.png")
    st.write("I adapted and tested the system in a web environment, integrating front-end functionalities with Python and JavaScript to ensure accessibility and usability.")

    st.subheader("🖼️ Web Browser Validation")
    st.image("Tela22.png")
    st.write("I performed tests in the Firefox browser within a virtualized mobile environment, ensuring compatibility, stability, and a consistent interface experience for the end user.")

    st.subheader("🖼️ Feature Confirmed")
    st.image("Tela23.png")
    st.write("All system features were validated and are operating correctly across multiple platforms and browsers, ensuring reliability and consistency.")

    st.subheader("🖼️ Conclusion and Results")
    st.image("Tela24.png")
    st.write("The final project reflects complete full-stack development skills, including Python, JavaScript, interface design, system integration, and the use of Docker for isolated and multi-platform environments. It demonstrates technical growth, dedication, and the ability to deliver complete and functional solutions.")

# ==============================
# 👨‍💻 ABOUT ME
# ==============================
elif opcao == "About Me":
    st.title("👨‍💻 Hello! I'm Mikael, 23 years old – nice to meet you")

    st.write("""
    Systems Analysis and Development student (3rd semester), with knowledge in programming logic, databases, and data analysis. CPA-20 certified (ANBIMA) and in the process of migrating to C-Pro R, adding financial market and investment product expertise. Analytical, organized, and problem-solving oriented profile, with interest in working in technology applied to the financial sector.
    """)

    st.write("Technical Skills:")
    st.write("""
    - Programming logic.  
    - Basic understanding of systems development.
    - Databases (basic/intermediate level).
    - Data analysis with Python.
    - Financial market fundamentals.
    - Financial mathematics.
    """)

    st.write("Soft Skills:")
    st.write("""
    - Analytical thinking.  
    - Organization and routine management.  
    - Professional communication.  
    - Teamwork.  
    - Proactivity and continuous learning.  
    """)

# ==============================
# 📜 CERTIFICATIONS
# ==============================
elif opcao == "Certifications":
    st.title("📜 Certifications")

    st.subheader("Data Analysis with Python")
    st.image("Certi (8).png")
    st.write("Anhanguera College | Sorocaba/SP — 2025")

    st.subheader("Financial Mathematics for Risk Analysis")
    st.image("Certi (2).png")
    st.write("Anhanguera College | Sorocaba/SP — 2025")

    st.subheader("International Business Planning and Development")
    st.image("Certi (9).png")
    st.write("Anhanguera College | Sorocaba/SP — 2025")

    st.subheader("CPA-20")
    st.image("Certi (6).png")
    st.write("Certification valid until 01/22/2028 — ANBIMA | Sorocaba/SP — 2025")

    st.subheader("CPA")
    st.image("Certi (0).png")
    st.write("Migration process in progress — ANBIMA | Sorocaba/SP — 2026")

    st.subheader("C-Pro R")
    st.image("Certi (0).png")
    st.write("Migration process in progress — ANBIMA | Sorocaba/SP — 2026")


# ==============================
# 💼 EXPERIENCE
# ==============================
elif opcao == "Experience":
    st.title("💼 Professional Experience")

    st.subheader("BENASSI SP | Sorocaba/SP — PRODUCE PROMOTER — 04/2024 to 01/2026")
    st.image("Exp (1).png")
    st.write("""
   Predominantly worked night shifts, with occasional morning support.
   Responsible for receiving and unloading trucks, and merchandise inspection.
   Price verification, system entries, and record checking, ensuring compliance.
   Product pricing execution, creation of promotions, and preparation of physical signage.
   Customer service on the sales floor.
   Support for asset security and participation in store opening and closing processes.
   Assembly, standardization, and organization of produce displays, following exposure, quality, and product turnover criteria.
   Preparation of display layout and strategic replenishment, ensuring visual presentation and accessibility according to store standards.
    """)

    st.subheader("Princesa Supermercado Cosméticos | Sorocaba/SP — STOCK CLERK (Temporary) — 09/2023 to 01/2024")
    st.image("Exp (3).png")
    st.write("""
   Responsible for stock organization and control, conducting periodic counts and system checks, identifying discrepancies and reporting to management for corrective action.
   Labeling and product coding, verifying barcodes and updating records.
   Control of expiration dates, losses, and damages, ensuring stored product compliance.
   Standardization and improvement of shelf organization, with alignment and communication with the team.
   Support for asset security and participation in store opening and closing processes.
    """)

    st.subheader("Higa Atacadista | Sorocaba/SP — MERCHANDISE STOCKER — 11/2022 to 05/2023")
    st.image("Exp (4).png")
    st.write("""
   Worked in restocking and organizing merchandise on shelves, islands, and promotional areas, according to product turnover and expiration dates.
   Organization of shelves and displays, facilitating access to high-demand items.
   Updating and replacing price tags according to pricing guidelines.
   Verification of expiration dates and replacement of non-compliant products.
   Organization of carts, pallets, and platforms, ensuring proper circulation and store visual standards.
   Customer service support, checking stock to locate products.
    """)

    st.subheader("Supermercado Tauste | Sorocaba/SP — BAGGER — 01/2022 to 10/2022")
    st.image("Exp (2).png")
    st.write("""
   Assisted in bagging merchandise, separating by category and preserving product integrity.
   Assisted customers in transporting purchases to vehicles in the parking lot.
   Assembly and separation of orders for home delivery, according to online and in-store requests.
   Supported cashiers in price identification, avoiding service delays.
    """)

# ==============================
# 💼 Thank You
# ==============================
elif opcao == "Thank You":
    st.title("🙏 Thank You")

    st.write("""
    Thank you for taking the time to review my portfolio and certifications.
    I hope the information presented demonstrates my skills, dedication,
    and interest in continuing to learn and develop technological solutions.
    """)
    st.image("Adeus2.png")