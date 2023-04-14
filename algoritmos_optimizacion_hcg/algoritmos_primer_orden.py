import numpy as np

def steepest_descent(gradiente, punto_inicial : np.array, rho : float : maxiter : int) -> np.array: 
    """
    Funcion : steepest_descent 

    Argumentos :
        * gradiente : gradiente de las funcion a minimizar 
        * punto_inicial : Punto inicial para iniciar la busqueda (np.array)
        * rho : Tasa de aprendizaje (float)
        * maxiter : Número de interacciones (int) 
    """

    X = punto_inicial
    
    for it in range(maxiter):
        if it % 10 == 0: 
            print(f"Iteración{it}")

        #Utilizamos la regla de actualización
        X = X - rho*gradiente(*X)

    return X 
