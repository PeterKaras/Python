import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sortedcontainers import SortedList

N_train = 450
N_test = 75
K = 5

class Data:
    def __init__(self):
        self.train_X = np.ones((N_train,2))
        self.train_Y = np.ones((N_train,2))
        
        self.test_X = np.ones((N_test,2))
        self.test_Y = np.ones((N_test,2))
    
    def generate_data(self) -> None:

        self.train_X[: 150] = np.random.random(( 150,2))
        self.train_X[150: 300] = np.random.random((150,2)) + 0.7   
        self.train_X[300: 450] = np.random.random((150,2)) - 0.7   
        self.train_Y = np.array([0]*(150) + [1]* (150) + [2]* 150)
    
        self.test_X[:25] = np.random.random(( 25,2 ))
        self.test_X[25:50] = np.random.random(( 25,2 )) + 0.7
        self.test_X[50:75] = np.random.random(( 25,2 )) - 0.7
        self.test_Y = np.array([0]*25 + [1]* 25 + [2]* 25)
        
    def plotting(self, X: [float], Y: [float], name: str, colors: dict = {1:"red",0:"blue", 2: "black"}) -> None:
        for group, x in zip(Y,X):
            plt.scatter(x[0],x[1], c= colors[group])
            
        plt.xlabel("X labels")
        plt.ylabel("Y labels")
        plt.title(name)
        plt.show()
            
class Knn(Data):
    def __init__(self, k: int):
        self.k = k
        
    def fit(self, X: [float], Y: [float]) -> None:
        self.X = X
        self.Y = Y
        
    def predict(self, X: [float]):
        y = []
        
        for i, x in enumerate(X):
            sorted_list = SortedList()
            
            for j, xt in enumerate(self.X):
                difference = x - xt
                difference = difference.dot(difference)
                if len(sorted_list) < self.k:
                    sorted_list.add((difference, self.Y[j]))
                else:
                    if sorted_list[-1][0] > difference:
                        del sorted_list[-1]
                        sorted_list.add((difference, self.Y[j]))
                        
            targets = []
            for i in sorted_list:
                targets.append(i[1])
                
            ones = targets.count(1)
            zeros = targets.count(0)
            twos = targets.count(2)
            
            max_count = 1 if ones >= zeros else 0
            max_count = max_count if targets.count(max_count) >= twos else 2
            y.append(max_count)
            
        return np.array(y)                
    
    def accuracy(self, X: [float], Y: [float]) -> (float, [float]):
        T = self.predict(X)
        return (np.mean(T == Y), T)
        
if __name__ == '__main__':
    data = Data()
    data.generate_data()
    data.plotting(data.train_X, data.train_Y, "Beggining of Train")
    data.plotting(data.test_X, data.test_Y, "Beggining of Test")    
    
    knn = Knn(K)
    knn.fit(data.train_X, data.train_Y)
    acc, T = knn.accuracy(data.train_X, data.train_Y)
    print("train_accuracy:",acc)
    data.plotting(data.train_X, T, "Train")
    
    
    acc, T = knn.accuracy(data.test_X, data.test_Y)
    print("test_accuracy:",acc)
    data.plotting(data.test_X, T, "Test")
    
    