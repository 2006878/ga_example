import streamlit as st
import numpy as np
import pygad
import matplotlib.pyplot as plt

import streamlit as st

st.set_page_config(
    page_title="Alocação de Recursos",
    page_icon="📈"
)

# Ocultar elementos desnecessários da interface
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    section[data-testid="stSidebar"] ul {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <h1 style="color: #4CAF50; font-weight: bold; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
        🚀 Otimize o investimento no seu projeto de Inovação
    </h1>
    <h3 style="color: #555;">
        Maximize o impacto social e econômico com Algoritmos Genéticos
    </h3>
    """,
    unsafe_allow_html=True
)

# 1. Inputs do usuário
n_areas = st.number_input("Número de áreas para alocar:", min_value=1, max_value=10, value=3, step=1)

area_names = []
for i in range(n_areas):
    name = st.text_input(f"Nome da área #{i+1}:", value=f"Área {i+1}")
    area_names.append(name)

col1, col2 = st.columns(2)
with col1:
    custos = []
    for i in range(n_areas):
        c = st.number_input(f"Custo por unidade (R$) - {area_names[i]}:", min_value=0.0, value=1000.0, step=100.0)
        custos.append(c)
with col2:
    impactos = []
    for i in range(n_areas):
        imp = st.number_input(f"Impacto por unidade - {area_names[i]}:", min_value=0.0, value=10.0, step=1.0)
        impactos.append(imp)

orcamento_total = st.number_input("Orçamento total disponível:", min_value=0.0, value=20000.0, step=1000.0)

if st.button("Calcular melhor alocação"):

    custos = np.array(custos)
    impactos = np.array(impactos)

    # Função fitness adaptada para PyGAD >= 2.20.0
    def fitness_func(ga, solution, solution_idx):
        investimento = np.array(solution)
        custo_total = np.sum(investimento * custos)
        if custo_total > orcamento_total:
            return -1
        impacto_total = np.sum(investimento * impactos)
        return impacto_total

    gene_space = range(0, 21)  # Máximo 20 unidades por área para dar margem maior

    ga_instance = pygad.GA(
        num_generations=50,
        num_parents_mating=4,
        fitness_func=fitness_func,
        sol_per_pop=10,
        num_genes=n_areas,
        gene_space=gene_space,
        mutation_percent_genes=20,
        keep_parents=2
    )

    ga_instance.run()

    solution, fitness, _ = ga_instance.best_solution()
    custo_final = np.sum(solution * custos)

    st.subheader("Resultado")
    for i in range(n_areas):
        st.write(f"**{area_names[i]}:** {int(solution[i])} unidades")
    st.write(f"Impacto total estimado: {fitness:.2f}")
    st.write(f"Custo total: R${custo_final:.2f}")
    st.write(f"Orçamento disponível: R${orcamento_total:.2f}")

    # Plot da evolução do fitness
    fig, ax = plt.subplots()
    ax.plot(ga_instance.best_solutions_fitness, marker="o", color="blue")
    ax.set_title("Evolução do Impacto ao longo das Gerações")
    ax.set_xlabel("Geração")
    ax.set_ylabel("Impacto")
    ax.grid(True)
    st.pyplot(fig)

    # Plot da distribuição final (pizza)
    fig2, ax2 = plt.subplots()
    ax2.pie(solution, labels=area_names, autopct="%1.1f%%", startangle=90)
    ax2.set_title("Distribuição Final dos Recursos")
    st.pyplot(fig2)

st.markdown(
    """
    <style>
    footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: #555;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
        border-top: 1px solid #ddd;
    }
    footer a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    <footer>
        Desenvolvido por <a href="https://www.mundodosdados.com.br/" target="_blank">Mundo dos Dados</a>
    </footer>
    """,
    unsafe_allow_html=True
)