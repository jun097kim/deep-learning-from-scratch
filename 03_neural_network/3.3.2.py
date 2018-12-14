import numpy as np


A = np.array([[1, 2], [3, 4]])
print(A.shape)

B = np.array([[5, 6], [7, 8]])
print(B.shape)

print(np.dot(A, B))


A = np.array([[1,2,3], [4,5,6]])
print(A.shape)
B = np.array([[1,2], [3,4], [5,6]])
print(B.shape)
print(np.dot(A, B))


# 행렬 A의 1번째 차원의 원소 수와 행렬 B의 0번 째 차원의 원소 수가 같야아 함
C = np.array([[1,2], [3,4]])
print(C.shape)
print(A.shape)
# np.dot(A, C)


A = np.array([[1,2], [3,4], [5,6]])
print(A.shape)
B = np.array([7,8])
print(B.shape)
print(np.dot(A, B))
