import numpy as np
import time
import math
np.random.seed(0)
import matplotlib.pyplot as plt
#sizes = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
sizes = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
Hr_values = []
H_values = []

for size in sizes:
    randnums = np.random.random(size)
    randnums = randnums/np.sum(randnums)
    
    start1 = time.time()
    sum = 0
    a = 0.999999
    for i in randnums:
        sum+=i**a
    Hr = (1/(1-a))*math.log(sum)
    end1 = time.time()
    
    start2 = time.time()
    H = 0
    for i in randnums:
        H-= i*math.log(i)
    end2 = time.time()
    print(H, Hr)
    Hr_values.append(end1-start1)
    H_values.append(end2-start2)

plt.plot(sizes, H_values)
plt.plot(sizes, Hr_values)
plt.xlabel("Number of Samples n")
plt.ylabel("time taken (s)")
plt.legend(["Entropy (Shannon)","Entropy (Renyi)", "u1 Gradient Play","u2 Gradient Play"])
plt.title("Time taken Vs Sampple Size, a = 0.999999")
plt.savefig("entropy-comparison",  dpi = 300)
plt.close()
plt.show()

plt.plot(sizes, H_values)
plt.plot(sizes, Hr_values)
plt.xlabel("Number of Samples n")
plt.ylabel("Time taken (s)")
plt.legend(["Entropy (Shannon)","Entropy (Renyi)"])
plt.title("Time taken Vs Sample Size, a = 0.999999")
plt.savefig("entropy-comparison",  dpi = 300)
plt.close()

for i in range(len(H_values)):
    H_values[i]*=16
    Hr_values[i]*=16

plt.plot(sizes, H_values)
plt.plot(sizes, Hr_values)
plt.xlabel("Number of Samples n")
plt.ylabel("Time taken (s)")
plt.legend(["I (Shannon)","I (Renyi)",])
plt.title("Time taken Vs Sample Size, a = 0.999999")
plt.savefig("I-comparison",  dpi = 300)
plt.close()
'''
sizes = [5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

a_mat = [0.1, 0.5, 0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999, 0.9999999, 0.99999999]
#finding errors
for size in sizes:
    for a in a_mat:
        randnums = np.random.random(size)
        randnums= randnums/np.sum(randnums)
        start1 = time.time()
        sum = 0
        
        for i in randnums:
            sum+=i**a
        Hr = (1/(1-a))*math.log(sum)
        end1 = time.time()
    
        start2 = time.time()
        H = 0
        for i in randnums:
            H-= i*math.log(i)
        end2 = time.time()
        #print(H, Hr)
        print(a, size, abs(H-Hr))
'''
#make graph comparing the estimator
#something to have accuracy wrt to the the a
#make a simple graph that you can calculate
#show proof of concept, not a large model, but an ok model
#ie combine nodes and make new graph 
#--talk about limitations
#----too difficult to implement the better algorithms
#----issues in python environment
#----other things, try to make the discussion fruitful4