import tensorflow as tf
import numpy as np

mat1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype = 'int32')
mat2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype = 'int32')

print (mat1)
print (mat2)

mat1 = tf.constant(matrix1)
mat2 = tf.constant(matrix2)
matrix_product = tf.matmul(matrix1, matrix2)
print(matrix_product)
