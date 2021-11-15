import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 40

class Data:
    def __init__(self):
        self.X = None
        self.Y = None
    
    def generate_data(self):
        pass
    
X = np.zeros((200, 2))
X[:50] = np.random.random((50, 2)) / 2 + 0.5 # (0.5-1, 0.5-1)
X[50:100] = np.random.random((50, 2)) / 2

K = np.array([1, 2, 3])
print(K.dot(K),"\n", K.T)


#X[100:150] = np.random.random((50, 2)) / 2 + np.array([[0, 0.5]]) # (0-0.5, 0.5-1)
#X[150:] = np.random.random((50, 2)) / 2 + np.array([[0.5, 0]])