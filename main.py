import numpy as np
import math
import random
import time
import matplotlib.pyplot as plt

def Xgate(input):
    return input @ np.array([[0, 1], [1, 0]])

def Hgate(input):
    sqroot = 1/math.sqrt(2)
    return input @ np.array([[sqroot, sqroot], [sqroot, sqroot * -1]])

def CNOTgate(input):
    return input @ np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

def createstatevector(n):
    one = random.randint(0, 1)
    two = 1 if one == 0 else 1
    three = random.randint(0, 1)
    four = 1 if three == 0 else 1
    statevector = np.kron(np.array([one, two]), np.array([three, four]))
    for i in range (n - 2):
        first = random.randint(0, 1)
        second = 1 if first == 0 else 1
        statevector = np.kron(statevector, np.array([first, second]))
    return statevector

def createtensor(n):
    vec = createstatevector(n)
    return np.reshape(vec, (2, -1))

def matmulsimulation(n):
    #this is ssomething
    vec = createstatevector(n)
    for i in range (0, n * 2 - 4, 2):
        vec[i : 2 + i] = Xgate(vec[i : 2 + i])
        vec[i : 2 + i] = Hgate(vec[i : 2 + i])
        vec[i : 4 + i] = CNOTgate(vec[i : 4 + i])
    return vec 

def runtime():
    #plot the runtime of your code as a function of the number of qubits.
    #what does this mean!
    bitarraymatrix = []
    timearraymatrix = []
    bitarraytensor = []
    timearraytensor = []
    for i in range (3, 30):
        bitarraymatrix.append(i)
        start = time.time()
        matmulsimulation(i)
        end = time.time()
        timearraymatrix.append(end - start)
    
    for i in range (3, 30):
        bitarraytensor.append(i)
        start = time.time()
        tensorsimulation(i)
        end = time.time()
        timearraytensor.append(end - start)

    plt.plot(bitarraymatrix, timearraymatrix)
    plt.title("time vs number of qubits for matrix")
    plt.xlabel("number of qubits")
    plt.ylabel("time taken (s)")
    plt.show()

    plt.plot(bitarraytensor, timearraytensor)
    plt.title("time vs number of qubits for tensor")
    plt.xlabel("number of qubits")
    plt.ylabel("time taken (s)")
    plt.show()

def tensorsimulation(n):
    vec = createtensor(n)
    for i in range (0, len(vec) - 1):
        vec[:, i] = Xgate(vec[:, i])
        vec[:, i] = Hgate(vec[:, i])
        cnotvec = np.kron(vec[:, i], vec[:, i + 1])
        outvec = CNOTgate(cnotvec.T).T
        vec[:, i] = outvec[0:1]
        vec[:, i+1] = outvec[1:2]
    return vec

def main():
    runtime()


if __name__ == "__main__":
    main()