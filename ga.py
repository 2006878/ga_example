import numpy as np
import pygad
import matplotlib
import matplotlib.pyplot as plt

# ===== Força backend interativo no VS Code (se disponível) =====
try:
    matplotlib.use("TkAgg")  # Troque para "Qt5Agg" se usar Qt
except Exception:
    pass  # Se não funcionar, vai usar o backend padrão

# ================================
# 1. Dados do problema
# ================================
custos = np.array([2000, 3500, 1500])  # custo por unidade
impactos = np.array([8, 15, 6])        # impacto por unidade
orcamento_total = 20000

# ================================
# 2. Função de fitness (3 parâmetros exigidos pela 2.20.0)
# ================================
def fitness_func(ga_instance, solution, solution_idx):
    investimento = np.array(solution)
    custo_total = np.sum(investimento * custos)
    if custo_total > orcamento_total:
        return -1
    impacto_total = np.sum(investimento * impactos)
    return impacto_total

# ================================
# 3. Espaço de busca
# ================================
gene_space = range(0, 11)  # máximo 10 unidades por área

# ================================
# 4. Configuração do GA
# ================================
ga_instance = pygad.GA(
    num_generations=50,
    num_parents_mating=4,
    fitness_func=fitness_func,
    sol_per_pop=10,
    num_genes=3,
    gene_space=gene_space,
    mutation_percent_genes=20,
    keep_parents=2
)

# ================================
# 5. Executa o GA
# ================================
ga_instance.run()

# ================================
# 6. Resultados finais
# ================================
solution, fitness, idx = ga_instance.best_solution()
print("\n=== RESULTADO FINAL ===")
print(f"Melhor alocação encontrada: {solution}")
print(f"Impacto total: {fitness}")
print(f"Custo total: {np.sum(solution * custos)}")

# ================================
# 7. Evolução do fitness (gráfico sem legenda)
# ================================
fitness_history = ga_instance.best_solutions_fitness
plt.figure(figsize=(8, 5))
plt.plot(fitness_history, marker='o', color='blue')
plt.title("Evolução do Impacto ao longo das gerações")
plt.xlabel("Geração")
plt.ylabel("Impacto")
plt.grid(True)
plt.tight_layout()
plt.savefig("evolucao_fitness.png")
print("Gráfico salvo como evolucao_fitness.png")

# Tenta mostrar o gráfico se backend for interativo
try:
    plt.show()
except Exception:
    pass

# ================================
# 8. Gráfico extra - distribuição final de recursos
# ================================
plt.figure(figsize=(6, 6))
labels = ["Capacitação", "Infraestrutura", "Eventos"]
plt.pie(solution, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Distribuição final dos recursos")
plt.savefig("distribuicao_recursos.png")
print("Gráfico salvo como distribuicao_recursos.png")

try:
    plt.show()
except Exception:
    pass
