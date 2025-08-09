# Exemplo de Algoritmo Genético com PyGAD — Alocação de Recursos em Hub de Inovação

Este projeto é um exemplo prático sobre **Algoritmos Genéticos (AG)** usando a biblioteca [PyGAD](https://pygad.readthedocs.io/).  

---

## Sobre o Algoritmo Genético

Um **Algoritmo Genético** é uma técnica de otimização inspirada no processo evolutivo natural. Ele trabalha com uma população de soluções candidatas (indivíduos), que evoluem ao longo de várias gerações para encontrar a melhor solução possível para um problema.

**Principais conceitos:**
- **População:** conjunto de soluções candidatas.
- **Genes:** partes que formam cada solução (como variáveis do problema).
- **Fitness:** função que mede a qualidade de cada solução.
- **Seleção:** escolha dos melhores para reprodução.
- **Crossover:** combinação dos genes dos pais para gerar filhos.
- **Mutação:** pequenas alterações nos genes para manter diversidade.

---

## Objetivo do Código

Este exemplo simula a alocação de um orçamento limitado entre três áreas de um Hub de Inovação:  
1. Capacitação de pessoas  
2. Infraestrutura  
3. Eventos e networking  

Cada área tem um custo por unidade de investimento e gera um impacto social/econômico estimado.  

O algoritmo genético encontra a melhor combinação de investimentos para **maximizar o impacto total dentro do orçamento disponível**.

---

## Estrutura do Código

1. **Dados do problema:** custos e impactos por unidade, orçamento total.  
2. **Função de fitness:** avalia o impacto total da alocação, penalizando ultrapassar o orçamento.  
3. **Configuração do PyGAD:** parâmetros do AG, tamanho da população, número de gerações, espaço de busca.  
4. **Execução do AG:** roda o algoritmo e evolui soluções.  
5. **Resultados:** imprime a melhor alocação encontrada, impacto e custo.  
6. **Visualizações:**  
   - Gráfico da evolução do impacto ao longo das gerações.  
   - Gráfico pizza da distribuição final dos recursos.

---

## Como instalar e rodar o exemplo

### Requisitos

- Python 3.7 ou superior  
- pip (gerenciador de pacotes Python)

### Passos

1. Clone ou baixe este repositório.  
2. Abra um terminal na pasta do projeto.  
3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
    ````

4. Instale as dependências:

   ```bash
   pip install pygad matplotlib numpy
   ```
5. Execute o script Python:

   ```bash
   python seu_arquivo.py
   ```

   *(Substitua `seu_arquivo.py` pelo nome do arquivo que contém o código.)*

### Observações

* Se estiver no Windows e tiver problemas para exibir gráficos, certifique-se de ter o `tkinter` instalado (geralmente já vem com o Python).
* No VS Code, use o modo **Run Interactive Window** para melhor visualização dos gráficos.

---

## O que você verá

* No terminal:

  * Melhor alocação de recursos (quantidade de unidades para cada área).
  * Impacto total alcançado.
  * Custo total da alocação.
* Gráficos (salvos como PNG no diretório):

  * Evolução do impacto ao longo das gerações (`evolucao_fitness.png`).
  * Distribuição final dos recursos (`distribuicao_recursos.png`).

---

## Referências

* [Documentação oficial PyGAD](https://pygad.readthedocs.io/)
* [Introdução a Algoritmos Genéticos (Wikipedia)](https://pt.wikipedia.org/wiki/Algoritmo_gen%C3%A9tico)

---

**Autor:** Tairone Amaral
**Data:** 09/082025
