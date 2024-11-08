import numpy as np
import math
import random
import time
import matplotlib.pyplot as plt

#qubit 1 -> x gate -> cnot control
#qubit 2 -> h gate -> cnot affect

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

def matmulsimulation(n):
    #this is ssomething
    vec = createstatevector(n)
    for i in range (0, n * 2 - 4, 2):
        vec[n : 2 + n] = Xgate(vec[n : 2 + n])
        vec[n : 2 + n] = Hgate(vec[n : 2 + n])
        vec[n : 4 + n] = CNOTgate(vec[n : 4 + n])
    print(vec)
    

def runtimematmul():
    #plot the runtime of your code as a function of the number of qubits. 
    #what does this mean! 
    bitarray = []
    timearray = []
    for i in range (3, 10):
        bitarray.append(i)
        start = time.time()
        matmulsimulation(i)
        end = time.time()
        timearray.append(end - start)
    plt.plot(bitarray, timearray)
    

def main():
    #idk something 
    runtimematmul()


if __name__ == "__main__":
    main()