# Relatório de Estudos - Vestibular Tracker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Um dashboard desenvolvido em **Python** e **Streamlit** para monitorar, registrar e analisar a performance de estudos para o Vestibular. 

O projeto atua como uma ferramenta de **Coleta de Dados (Data Collection)** estruturada, criando um dataset histórico robusto para futuras aplicações de **Machine Learning** (previsão de rendimento e otimização de rotina).

---

### 1. Coleta de Dados (ETL)
- **Formulário Dinâmico:** Interface intuitiva para registrar o dia (Estudo, Descanso ou Falta).
- **Métricas Subjetivas:** Sliders para quantificar "Foco", "Qualidade" e "Volume" de estudo (escala 1-5).
- **Categorização:** Registro de matérias estudadas e turno predominante.
- **Persistência:** Salvamento automático em arquivo `.csv` (append mode), garantindo histórico sem necessidade de banco de dados complexo.

### 2. Análise e Visualização (Dashboard)
- **KPIs em Tempo Real:** Cálculo automático de:
  - Total de dias registrados.
  - Consistência (Dias estudados).
  - Média de Foco.
- **Gráficos Interativos:**
  - **Distribuição de Matérias:** Gráfico de barras coloridas para identificar desbalanceamento no cronograma (Viés/Bias).
- **Gestão de Erros:** Botão de pânico para remover o último registro em caso de erro de digitação.

---

## Tecnologias

* **Python:** Linguagem base.
* **Streamlit:** Framework para criação do Web App.
* **Pandas:**
    * Manipulação de DataFrames.
    * Limpeza de dados (`.strip`, `.replace`, `.split`).
    * Tratamento de dados aninhados (`.explode`).
    * Tratamento de valores nulos e tipagem (`.astype`, `NaN handling`).
* **Visualização de Dados:** `st.bar_chart` e `st.metric`.

---

## Estrutura do Projeto

```text
/
├── app.py              # Interface principal (Front-end e Visualização)
├── data_manager.py     # Lógica de persistência (Back-end e Manipulação de Arquivos)
├── reports/            # Pasta onde o CSV é salvo automaticamente
│   └── dados_estudos.csv
└── README.md           # Documentação
