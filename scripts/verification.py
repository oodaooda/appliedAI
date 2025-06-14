import numpy as np
import time
import matplotlib.pyplot as plt
'''
logits = np.array([2.0, 1.0, 0.1])
times = []
sizes = [10, 100, 1000, 10_000, 100_000]

def sofmax():
    for z_i in logits:    
        x = (np.exp(z_i) ) / (np.sum(np.exp(logits)))
        print(x)
     
logits = np.array([2.0, 1.0, 0.1])

def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)


for size in sizes:
    test_input = np.random.rand(size)
    start = time.time()
    _=softmax(test_input)
    end = time.time()
    times.append(end - start)
    
probs = softmax(logits)
print(probs)

plt.plot(sizes, times, marker ='o')
plt.xlabel(('Input Size'))
plt.ylabel('Execution Time (Seconds)')
plt.title('Softmax execution Time Vs Insput Size (CPU)')
plt.grid(True)
plt.show()
'''
for x in range(10):
    startTime = time.time()
    x = x * x * np.exp(x)
    endTime = time.time()
    totalTime = startTime - endTime
    print(x)    
    print(f"{totalTime:.10f}")
