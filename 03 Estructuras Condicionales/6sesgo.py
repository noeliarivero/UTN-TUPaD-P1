from statistics import mode, median, mean 
import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = int(mode(numeros_aleatorios))
mediana = int(median(numeros_aleatorios))
media = int(mean(numeros_aleatorios))

if media>mediana and mediana>moda:
    print("Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. ")
elif media<mediana and median<moda:
    print("Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. ")
elif mediana==media==moda:
    print("Sin sesgo: cuando la media, la mediana y la moda son iguales. ")    
    