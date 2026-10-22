import timeit
from typing import Callable

from bm import boyer_moore_search
from kmp import kmp_search
from rabin_karp import rabin_karp_search

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except UnicodeDecodeError:
        with open(filename, "r", encoding="cp1251") as file:
            return file.read()  

def benchmark_search_algorithm(search_function: callable, text: str, pattern: str, iterations: int = 1000):
    setup_code = f"from __main__ import {search_function.__name__}, text, pattern"
    stmt = f"{search_function.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup_code, globals={'text': text, 'pattern': pattern}, number=iterations)/iterations 

  

if __name__ == "__main__":  
    text = read_file(r"C:\Users\Unrea\Desktop\neoversity\test_kod\HW_algoritmi\стаття_2.txt")
    real_pattern = "зберігання даних"    
    fake_pattern = "відсутній підрядок"
    print() 

    results = []
    for pattern in [real_pattern, fake_pattern]:
        boyer_moore_time = benchmark_search_algorithm(boyer_moore_search, text, pattern)
        results.append(("Боєра-Мура", pattern, boyer_moore_time))
        kmp_time = benchmark_search_algorithm(kmp_search, text, pattern)
        results.append(("Кнута-Морріса-Пратта", pattern, kmp_time))
        rabin_karp_time = benchmark_search_algorithm(rabin_karp_search, text, pattern)
        results.append(("Рабіна-Карпа" , pattern, rabin_karp_time))
 
    print(f"Результати роботи алгоритмів Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа ")
    print()
    title = f"{'Алгоритм':<30} | {'Підрядок':<30} | {'Час виконання (секунди)':<25}"
    print("-" * len(title))
    print(title)
    print("-" * len(title))
    for result in results:
        algorithm, pattern, time_taken = result
        print(f"{algorithm:<30} | {pattern:<30} | {time_taken:<25.6f}")

    print("-" * len(title))    
    print()   
   
    