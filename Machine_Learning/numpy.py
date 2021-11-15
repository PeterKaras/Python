import numpy as np

mat = np.random.randint(0,50,12)
mat1 = np.random.rand(2,2)

#ROW, COLUMN
mat_row = mat.reshape(1,-1)
mat_column = mat.reshape(-1,1)
mat_34 = mat.reshape(3,4)
mat_322 = mat.reshape(3,2,2)


a = np.array([[1,2,3], [4,5,6]])
sum_of_all = np.cumsum(a)

print(mat > 20, mat[mat > 20])