import random
import time
import sys
import json

# Adicionando algorithms/ ao caminho do sistema
sys.path.insert(0, './algorithms/')

# Funções de ordenação
from bubble import bubble_sort
from insertion import insertion_sort
from merge import merge_sort
from heap import heapsort
from quick import quick_sort

# Gera um vetor de tamanho size de acordo com o tipo escolhido pelo usuário
def generate_arr(t, size):
    if t == 1:  
        return list(range(size))
    elif t == 2:
        return list(range(size-1, -1, -1))
    elif t == 3:
        return [random.randint(0, size-1) for _ in range(size)]
    else:
        raise ValueError("Opção inválida!")

# Ordena o vetor com o algoritmo escolhido pelo usuário e calcula o tempo de execução
def run_sort(arr, sort_function):
    # Calcula o tempo de execução da função de ordenação escolhida pelo usuário
    start_time = time.time()
    comparisons = sort_function(arr)
    end_time = time.time()

    elapsed_time = (end_time - start_time) * 1000

    return elapsed_time, comparisons

# Lista com as opções de tamanho do vetor disponíveis
size_options = [100, 1000, 5000, 30000, 50000, 100000, 150000, 200000]

# Dicionário com as opções de tipo de vetor disponíveis
type_options = {
    1: "ascending",
    2: "descending",
    3: "random"
}

# Dicionário com o algoritmos de ordenação disponíveis
algorithms = {
    "bubble_sort": bubble_sort,
    "insertion_sort": insertion_sort,
    "merge_sort": lambda arr: merge_sort(arr, 0, len(arr) - 1),
    "heapsort": heapsort,
    "quick_sort": lambda arr: quick_sort(arr, 0, len(arr) - 1)
}

execution_data = {}

for algorithm_name, sort_function in algorithms.items():
    execution_data[algorithm_name] = {
        "execution_time": {},
        "comparisons": {}
    }

    for type_arr, type_name in type_options.items():
        execution_data[algorithm_name]["execution_time"][type_name] = []
        execution_data[algorithm_name]["comparisons"][type_name] = []

        for size_arr in size_options:
            arr = generate_arr(type_arr, size_arr)

            execution_times = []
            comparisons_arr = []
            for _ in range(3):
                execution_time, comparisons = run_sort(arr.copy(), sort_function)
                execution_times.append(execution_time)
                comparisons_arr.append(comparisons)

            average_execution_time = sum(execution_times) / len(execution_times)
            average_comparisons = sum(comparisons_arr) / len(comparisons_arr)

            execution_data[algorithm_name]["execution_time"][type_name].append(average_execution_time)
            execution_data[algorithm_name]["comparisons"][type_name].append(average_comparisons)

# Salva os dados em um arquivo JSON
with open('execution_data.json', 'w') as f:
    json.dump(execution_data, f)
