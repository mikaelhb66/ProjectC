import streamlit as st

st.set_page_config(page_title="Apresentando Mikael", layout="wide")

# MENU LATERAL (Projeto Acadêmico primeiro)
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ["Projeto Acadêmico", "Quem sou eu", "Certificações", "Experiência"],
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
    Estudante de Análise e Desenvolvimento de Sistemas (3º semestre), com conhecimentos em lógica de programação, banco de dados e análise de dados. Certificado CPA-20 (ANBIMA) e em processo de migração para C-Pro R, agregando visão de mercado financeiro e produtos de investimento. Perfil analítico, organizado e orientado à solução de problemas, com interesse em atuar em tecnologia aplicada ao setor financeiro.."
    """)

    st.markdown("---")

    # 🎥 VÍDEO COM TÍTULO E DESCRIÇÃO
    st.subheader("🎥 Demonstração em Vídeo")
    st.write("Veja abaixo um vídeo demonstrativo do funcionamento do sistema, destacando suas principais funcionalidades.")
    st.video("https://youtu.be/seu_link_aqui")
    st.write("O vídeo mostra a navegação pelo sistema, incluindo telas de cadastro, consulta e relatórios, ilustrando a experiência completa do usuário.")

    st.markdown("---")

    # 🖼️ IMAGENS COM TÍTULO E DESCRIÇÃO
    st.subheader("🖼️ Inicio do Projeto")
    st.image("Tela01.png")
    st.write("Desenvolvi este projeto em Python utilizando Visual Studio Code, aplicando boas práticas de programação desde a concepção inicial.")

    st.subheader("🖼️ Primeira Versão")
    st.image("Tela02.png")
    st.write("Criei a primeira versão funcional, priorizando lógica e eficiência, demonstrando habilidade em desenvolvimento backend em Python.")

    st.subheader("🖼️ Versão Interface")
    st.image("Tela03.png")
    st.write("Implementei uma interface inicial, demonstrando capacidade de transformar programas de console em soluções com interação visual..")

    st.subheader("🖼️ Versão Final")
    st.image("Tela04.png")
    st.write("Integrei funcionalidades completas com interface intuitiva, garantindo usabilidade e experiência do usuário.")

    st.subheader("🖼️ Funcionalidades")
    st.image("Tela05.png")
    st.write("Configurei e testei todas as funcionalidades do sistema, assegurando confiabilidade e performance do software.")

    st.subheader("🖼️ Versão Web")
    st.image("Tela06.png")
    st.write("Adaptei o projeto para web, aumentando acessibilidade e permitindo uso em múltiplas plataformas.")

    st.subheader("🖼️ Logo Web")
    st.image("Tela07.png")
    st.write("Desenvolvi identidade visual para o projeto, destacando atenção ao design e apresentação profissional.")

    st.subheader("🖼️ Login")
    st.image("Tela08.png")
    st.write("Explorei integração com JavaScript para enriquecer a experiência web, demonstrando versatilidade em linguagens front-end.")

    st.subheader("🖼️ Funcionalidades Web")
    st.image("Tela09.png")
    st.write("Nessa situação eu começei a mecher com javascrip para fazer as funcionalidaes da versão Web.")

    st.subheader("🖼️ Funcionalidade ")
    st.image("Tela10.png")
    st.write("Organizei telas de funcionalidades destacando ações-chave do sistema, focando em interface clara e eficiente.")

    st.subheader("🖼️ Funcionalidade Cadastro")
    st.image("Tela11.png")
    st.write("Desenvolvi a tela de cadastro, aplicando validações e garantindo consistência de dados.")

    st.subheader("🖼️ Funcionalidade consulta ")
    st.image("Tela12.png")
    st.write("Implementei consultas dinâmicas, proporcionando acesso rápido a informações armazenadas.")

    st.subheader("🖼️ Google Shell Editor")
    st.image("Tela16.png")
    st.write("Utilizei ferramentas avançadas de edição e execução de código, otimizando o processo de desenvolviment")

    st.subheader("🖼️ Rodar em Sistema mas como?")
    st.image("Tela17.png")
    st.write("Configurei o projeto para rodar em sistemas Linux utilizando Docker, garantindo compatibilidade e isolamento do ambiente de desenvolvimento.")

    st.subheader("🖼️ Rodanddo em maquina virtual")
    st.image("Tela19.png")
    st.write("Implementei testes do projeto em uma máquina virtual, validando a portabilidade do software e o correto funcionamento em diferentes ambientes..")

    st.subheader("🖼️ Funciona e podemos ver rodando")
    st.image("Tela20.png")
    st.write("Realizei a execução do projeto, confirmando o funcionamento das funcionalidades implementadas e a estabilidade do sistema..")

    st.subheader("🖼️ Testando versão Web ")
    st.image("Tela21.png")
    st.write("Adaptei e testei o sistema em ambiente web, integrando funcionalidades front-end com Python e JavaScript para garantir acessibilidade e usabilidade.")

    st.subheader("🖼️ Navegador web")
    st.image("Tela22.png")
    st.write("Validei a execução do projeto em navegadores, garantindo experiência consistente para o usuário final..")

    st.subheader("🖼️ Está funcionando")
    st.image("Tela23.png")
    st.write("Confirmei que todas as funcionalidades do sistema estão operando corretamente em diferentes plataformas e navegadores.")

    st.subheader("🖼️ Final , Estudo e trabalho duro valeu a pena")
    st.image("Tela24.png")
    st.write("O projeto final demonstra evolução técnica, dedicação e aprendizado contínuo, evidenciando habilidades em programação Python, desenvolvimento web, integração de interfaces gráficas e uso de Docker para ambientes isolados e multiplataforma.")

# ==============================
# 👨‍💻 QUEM SOU EU
# ==============================
elif opcao == "Quem sou eu":
    st.title("👨‍💻 Quem sou eu & 💡 Competências")
    
    st.write("""
    Sou estudante de **Análise e Desenvolvimento de Sistemas**, com interesse em tecnologia aplicada ao mercado financeiro.
    """)
    
    st.write("Minhas principais competências incluem:")
    st.write("""
    - **Python** – desenvolvimento de scripts, automações e projetos.  
    - **Lógica de programação** – resolução de problemas e implementação de algoritmos eficientes.  
    - **Banco de dados** – manipulação e consulta de dados com SQL.  
    - **Análise de dados** – interpretação e organização de informações para tomada de decisão.  
    - **Matemática financeira** – cálculos aplicados a investimentos e produtos financeiros.  
    """)


# ==============================
# 📜 CERTIFICAÇÕES
# ==============================
elif opcao == "Certificações":
    st.title("📜 Certificações")

    # Certificação 1
    st.subheader("Análise de Dados com Python")
    st.image("Certi (8).png")  # coloque o nome do arquivo da imagem da certificação
    st.write("Faculdade Anhanguera | Sorocaba/SP — 2025")

    # Certificação 2
    st.subheader("Matemática Financeira para Análise de Riscos")
    st.image("Certi (2).png")
    st.write("Faculdade Anhanguera | Sorocaba/SP — 2025")

    # Certificação 3
    st.subheader("Planejamento e Desenvolvimento de Negócios Internacionais")
    st.image("Certi (9).png")
    st.write("Faculdade Anhanguera | Sorocaba/SP — 2025")

    # Certificação 4
    st.subheader("CPA-20")
    st.image("Certi (6).png")
    st.write("Certificação válida até 22/01/2028 — ANBIMA | Sorocaba/SP — 2025")

    # Certificação 5
    st.subheader("CPA")
    st.image("Certi (0).png")
    st.write("Processo Migração em andamento — ANBIMA | Sorocaba/SP — 2026")

    # Certificação 6
    st.subheader("C-Pro R")
    st.image("Certi (0).png")
    st.write("Processo Migração em andamento — ANBIMA | Sorocaba/SP — 2026")


# ==============================
# 💼 EXPERIÊNCIA
# ==============================
elif opcao == "Experiência":
    st.title("💼 Experiência Profissional")

    # Experiência 1
    st.subheader("BENASSI SP | Sorocaba/SP — PROMOTOR HORTIFRÚTI — 04/2024 a 01/2026")
    st.image("Exp (1).png")  # imagem/logo da empresa
    st.write("""
   Atuação predominante no turno da madrugada, com apoio eventual no período da manhã.
   Responsável pelo recebimento e descarregamento de caminhões, conferência de mercadorias.
   Conferência de preços, lançamentos e verificação registros no sistema, assegurando conformidade.
   Execução de precificação de produtos, criação de ofertas e elaboração de cartazes físicos.
   Atendimento ao cliente no salão de vendas.
   Apoio à segurança patrimonial e participação nos processos de abertura e fechamento da loja.
   Montagem, padronização e organização de bancas de hortifrúti, seguindo critérios de exposição, qualidade e giro de produtos.
   Preparação do layout de exposição e reposição estratégica, garantindo apresentação visual e acessibilidade conforme padrões da loja.
    """)

    # Experiência 2
    st.subheader("Princesa Supermercado Cosméticos | Sorocaba/SP — ESTOQUISTA (Temporário) — 09/2023 a 01/2024")
    st.image("Exp (3).png")
    st.write("""
   Responsável pela organização e controle de estoque, com realização de contagens periódicas e conferência sistêmica, identificando divergências e reportando à gerência para tomada de ações corretivas.
   Execução de etiquetagem e codificação de produtos, com verificação de códigos de barras e atualização de registros.
   Controle de vencimentos, perdas e avarias, assegurando conformidade dos produtos armazenados.
   Padronização e melhoria da organização de prateleiras, com alinhamento e comunicação junto à equipe.
   Apoio à segurança patrimonial e participação nos processos de abertura e fechamento da loja.
    """)

    # Experiência 3 (opcional)
    st.subheader("Higa Atacadista | Sorocaba/SP — REPOSITOR DE MERCADORIAS — 11/2022 a 05/2023")
    st.image("Exp (4).png")
    st.write("""
   Atuação em reposição e organização de mercadorias em gôndolas, ilhas e pontos extras, conforme giro e validade dos produtos.
   Organização de prateleiras e expositores, facilitando acesso aos itens de maior saída.
   Atualização e troca de etiquetas de preços conforme orientações de precificação.
   Verificação de prazos de validade e substituição de produtos fora do padrão.
   Organização de carrinhos, paletes e plataformas, garantindo circulação adequada e padrão visual da loja.
   Apoio ao atendimento ao cliente, com consulta ao estoque para localização de produtos.
    """)

    # Experiência 3 (opcional)
    st.subheader("Supermercado Tauste | Sorocaba/SP — EMPACOTADOR — 01/2022 a 10/2022")
    st.image("Exp (2).png")
    st.write("""
   Apoio ao empacotamento de mercadorias, com separação por categoria e preservação da integridade dos produtos.
   Auxílio aos clientes no transporte de compras até veículos no estacionamento.
   Montagem e separação de pedidos para entregas domiciliares, conforme solicitações on-line e presenciais.
   Apoio ao caixa na identificação de preços, evitando atrasos no atendimento.
    """)
