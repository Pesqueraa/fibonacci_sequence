#Este programa consiste en relizar la secuencia de Fibonacci para tantos valores como se indique en range()
# La función `fibonacci_naive(n)` implementa el algoritmo de Fibonacci utilizando la definición recursiva y un enfoque naive.
def fibonacci_naive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)
# Utilizo un diccionario llamado memo para almacenar los resultados de las llamadas recursivas a la función fibonacci_memoization()
# La función `fibonacci_memoization(n, memo={})` implementa el algoritmo de Fibonacci utilizando la definición recursiva y un enfoque de memoización.
def fibonacci_memoization(n, memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]

# La secuencia se imprime en la salida estándar.
# Imprime los primeros 10 números de la secuencia de Fibonacci usando la implementación naive.
print([fibonacci_naive(i) for i in range(10)]) 
# Imprime los primeros 10 números de la secuencia de Fibonacci usando la implementación de memoización.
print([fibonacci_memoization(i) for i in range(10)]) 