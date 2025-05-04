import random
import time

def geraVetor(tamanho, inicio=0, fim=10000):
    return [random.randint(inicio, fim) for _ in range(tamanho)]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        marcado = array[i]
        j = i - 1
        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marcado
    return array

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        esquerda = array[:mid]
        direita = array[mid:]
        
        merge_sort(esquerda)
        merge_sort(direita)
        
        i = j = k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1
        
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1
        
        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1
    
    return array

def particao(array, inicio, final):
    pivo = array[final]
    i = inicio - 1
    for j in range(inicio, final):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[final] = array[final], array[i + 1]
    return i + 1

def quick_sort(array, inicio, final):
    if inicio < final:
        posicao = particao(array, inicio, final)
        quick_sort(array, inicio, posicao - 1)
        quick_sort(array, posicao + 1, final)
    return array

tamanho = 10000
vetor = geraVetor(tamanho)


inicio = time.time()
bubble_sort(vetor.copy())
fim = time.time()
tempo_bubble = fim - inicio

inicio = time.time()
insertion_sort(vetor.copy())
fim = time.time()
tempo_insertion = fim - inicio

inicio = time.time()
merge_sort(vetor.copy())
fim = time.time()
tempo_merge = fim - inicio

inicio = time.time()
quick_sort(vetor.copy(), 0, len(vetor) - 1)
fim = time.time()
tempo_quick = fim - inicio

print(f'Bubble Sort: {tempo_bubble:.2f} segundos')
print(f'Insertion Sort: {tempo_insertion:.2f} segundos')
print(f'Merge Sort: {tempo_merge:.2f} segundos')
print(f'Quick Sort: {tempo_quick:.2f} segundos')
