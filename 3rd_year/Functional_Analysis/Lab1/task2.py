import numpy as np
import math

eps = 1e-4
def mtrx_decomposition (A: np.ndarray, B: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    A_T = A.T
    A_T_A = A_T @ A
    A_T_B = A_T @ B
    lambda_ = max(np.linalg.eig(A_T_A)[0])
    C = np.eye(A_T_A.shape[0]) - (A_T_A / lambda_)
    D = A_T_B / lambda_
    return C, D

def cube_norm(A: np.ndarray) -> float:
    return np.max(np.sum(np.abs(A), axis=1))

def vec_norm(A: np.array) -> float:
    return np.max(np.abs(A))

def aprior_estimate(eps: float,
                    alpha: float,
                    x0: np.array,
                    x1: np.array) -> int:
    n_aprior = math.ceil(math.log((eps * (1 - alpha)) / vec_norm(x1 - x0), alpha)) + 1
    return n_aprior

def F (X_n: np.array, C: np.ndarray, D: np.ndarray) -> np.array:
    return C.dot(X_n) + D

A = np.array ([[1.2, 0.2, 0.1], [0, 1, 0.1], [0.1, 0, 1.3]])
B = np.array ([1, 1, 1])

C,D = mtrx_decomposition (A, B)
alpha = cube_norm(C)
print (alpha)

n = A.shape[0]
x0 = np.zeros(n, dtype=float)
x1 = F (x0, C, D)

n_aprior = aprior_estimate (eps, alpha, x0, x1)
print (f"Априорная оценка числа итераций: n = {n_aprior}")

n = 0
while (alpha/(1 - alpha)) * vec_norm(x1 - x0) >= eps:
    x0, x1 = x1, F (x1, C, D)
    n += 1
print ("\nРезультаты итераций:")
print (f"Последняя итерация n = {n}")
print (f"x* = {x1}")