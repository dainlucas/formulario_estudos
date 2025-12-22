import streamlit as st
import data_manager as dm
from datetime import datetime

st.title("Relatório de Estudos")
aba1, aba2 = st.tabs(["💻 Relatório", "📅 Histórico"])

# Variaveis vazias para evitar erros
materias = []
foco = 0
comentario = ""
volume = 0
qualidade = 0
turno = ""


# INÍCIO DO FORMULÁRIO - ABA RELATÓRIO
with aba1:
    # Etapa 01 - Estudou ou não?
    status = st.radio(
        "Status do dia",
        ["Estudei", "Não estudei", "Descanso"]
    )

    # Etapa 02 - Estudou? Quais matérias? Que Turno?

    # Se estudou
    if status == "Estudei":
        materias = st.multiselect("Quais matérias?", ["Matemática", "Física", "Redação", "Português"])
        turno = st.radio("Turno predominante:", ["Manhã", "Tarde", "Noite"])

        # Etapa 03 - Escalas de volume, qualidade, foco de estudos
        volume = st.slider("Volume de conteúdo:", 1, 5, 3)
        qualidade = st.slider("Qualidade do aprendizado:", 1, 5, 3)
        foco = st.slider("Nível de Foco:", 1, 5, 3)

    # Se não estudou por falta
    elif status == "Não estudei":
        comentario = st.text_input("O que te impediu?")
    # Se não estudou por descanso
    else:
        comentario = st.text_input("Como está sua energia para amanhã?")

    # Satisfação de como foi o dia
    satisfacao = st.select_slider("Satisfação Geral com o dia:", options=["😡", "😐", "🤩"])

    # Tradutor dos emojis para números
    mapeamento_satisfacao = {"😡": 1, "😐": 2, "🤩": 3}

    # Botão de salvar e enviar os dados para data_manager.py
    if st.button("Salvar Relatório"):
        dados = {
            "Data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Status": status,
            "Volume": volume,
            "Qualidade": qualidade,
            "Materias": str(materias) if status == "Estudei" else "",
            "Foco": foco if status == "Estudei" else 0,
            "Satisfacao": mapeamento_satisfacao.get(satisfacao, 0),
            "Turno": turno,
            "Comentario": comentario
        }
        dm.salvar_dados(dados)
        st.success("Relatório salvo com sucesso!")

# ABA HISTÓRICO AQUI
with aba2:
    st.header("Seu histórico de progresso")
    if st.button("🗑️ Remover Último Registro"):
        if dm.remover_ultimo_registro():
            st.warning("Último registro removido!")
            st.rerun()  # Isso atualiza a página para o dado sumir da tabela na hora
        else:
            st.error("Não há registros para remover.")

    # carrega os dados
    df = dm.carregar_dados()

    # verifica se os dados existem
    if df is not None and not df.empty:
        # cálculos do pandas
        total_dias = len(df)

        # filtro de status == estudei
        df_estudo = df[df["Status"] == "Estudei"]
        # dias estudados
        dias_estudo = len(df_estudo)

        # cálculo da média de foco (se houver dias de estudos)
        media_foco = df_estudo["Foco"].mean() if dias_estudo > 0 else 0

        # cria e exibe as colunas com as métricas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Dias", total_dias)
        with col2:
            st.metric("Dias de Estudo", dias_estudo)
        with col3:
            st.metric("Foco médio", f"{media_foco:.1f}")

        # limpeza da coluna materias
        # O .astype(str) converte qualquer NaN em "nan" (texto), evitando o erro
        materias_series = df_estudo["Materias"].astype(str).str.strip("[]").str.replace("'", "").str.split(", ")

        # transforma cada item da lista em uma linha individual para as tabelas gráficas
        contagem_materias = materias_series.explode().value_counts()
        # Isso remove qualquer "texto vazio" que possa ter sobrado na limpeza
        contagem_materias = contagem_materias[contagem_materias.index != ""]

        # Transformamos a contagem em uma tabela real (DataFrame)
        df_grafico = contagem_materias.reset_index()
        # Damos nomes claros para as colunas
        df_grafico.columns = ['Matéria', 'Frequência']

        # 3. EXIBIÇÃO DO GRÁFICO
        st.subheader("Frequência por Matéria (Equilíbrio de Dados)")
        st.bar_chart(
            df_grafico,
            x="Matéria",
            y="Frequência",
            color="Matéria"
        )

        st.divider() # Linha para separar as métricas da tabela



        #exibe as tabelas
        st.dataframe(df)

    else:
        st.info("Ainda não há dados...")




