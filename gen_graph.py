import json
import matplotlib.pyplot as plt

# Carregar o arquivo JSON
with open('execution_data.json') as file:
    data = json.load(file)

# Preparar os dados para cada algoritmo
algorithms = ['bubble_sort', 'insertion_sort', 'merge_sort', 'heapsort', 'quick_sort']
vector_types = ['ascending', 'descending', 'random']

for algorithm in algorithms:
    execution_times = data[algorithm]['execution_time']
    comparisons = data[algorithm]['comparisons']
    
    # Gráfico de linhas para tempo de execução
    plt.figure()
    plt.title(f'Tempo de execução - {algorithm}')
    plt.xlabel('Tamanho')
    plt.ylabel('Tempo')
    
    for vector_type in vector_types:
        times = execution_times[vector_type]
        plt.plot(range(1, len(times) + 1), times, label=vector_type)
    
    plt.legend()
    plt.savefig(f'./result/{algorithm}_execution_times.png')
    plt.show()

    # Gráfico de linhas para comparações
    plt.figure()
    plt.title(f'Comparações - {algorithm}')
    plt.xlabel('Tamanho')
    plt.ylabel('Comparações')
    
    for vector_type in vector_types:
        comps = comparisons[vector_type]
        plt.plot(range(1, len(comps) + 1), comps, label=vector_type)
    
    plt.legend()
    plt.savefig(f'./result/{algorithm}_comparisons.png')
    plt.show()
