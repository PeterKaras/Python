import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def scatter_ploting(X: [float], Y: [float], name: str) -> None:
    plt.scatter(X, Y, color = "b")
    plt.title(name)
    plt.xlabel("X labels")
    plt.ylabel("Y labels")
    plt.show()
    
def full_plotting(X: [float], Y: [float], Y_hat: [float], name: str) -> None:
    plt.scatter(df.loc[:,"X"], df.loc[:,"Y"], color = "b")
    plt.plot(X,Y_hat, color = "red", alpha = 1)
    plt.title(name)
    plt.xlabel("X labels")
    plt.ylabel("Y labels")
    plt.show()
    
def cost_function(Y: [float], Y_hat: [float]) -> ([float],[float]):
    SSres = Y - Y_hat
    SStot = Y - Y.mean()
    return SSres, SStot

def d_projection_scatter(X: [float], Y: [float], Z: [float]) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z)
    plt.show()
    
def d_projection(X: [float], Y: [float], Z: [float], Y_hat: [float]) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z)
    ax.plot_surface(X, Y, Y_hat)
    plt.show()

df = pd.read_csv("data_1d.csv", delimiter=",", names= ["X", "Y"])
df1 = pd.read_csv("data_2d.csv", delimiter=",", names= ["X", "Y", "Z"])

num_values = df.isnull().sum()
num_values_1 = df1.isnull().sum()

#DF1
scatter_ploting(df["X"], df["Y"], "1D")

X = np.array(df.loc[:,"X"])
Y = np.array(df.loc[:,"Y"])

deno = (X.dot(X) - X.mean()*X.sum())

a = (X.dot(Y) - Y.mean() * X.sum()) / deno
b = (X.dot(X)*Y.mean() - X.mean() * Y.dot(X)) / deno

Y_hat = a*X + b

full_plotting(df["X"], df["Y"], Y_hat, "1D")

SSres,SStot = cost_function(Y, Y_hat)

r2 = 1 - SSres.dot(SSres) / SStot.dot(SStot)
print("Effectivness of model is:",r2,"- R-Squared")

X_new = np.array(df1.loc[:,["X","Y"]])
Y_new = np.array(df1.loc[:,"Z"])

#DF1
scatter_ploting(df1["X"], df1["Y"], "2D")
scatter_ploting(df1["X"], df1["Z"], "2D")
scatter_ploting(df1["Y"], df1["Z"], "2D")
d_projection_scatter(df1["X"], df1["Y"], df1["Z"])

w = np.linalg.solve(X_new.T.dot(X_new), X_new.T.dot(Y_new))

Y_hat = X_new.dot(w)
Y_hat1 = np.expand_dims(Y_hat, axis = 1)

#d_projection(X_new[:,0], X_new[:,1], Y_new, Y_hat1)
SSres,SStot = cost_function(Y_new, Y_hat)
r2 = 1 - SSres.dot(SSres) / SStot.dot(SStot)
print("Effectivness of model is:",r2,"- R-Squared")