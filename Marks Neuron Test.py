import math

import numpy as np

inputs = [70, 80, 90]

weights = [0.1, 0.2, 0.3]

bias = 3

output = np.dot(weights, inputs) + bias

required_output = 1

adjustment = 0.01

for epoch in range(100):
    output = np.dot(weights, inputs) + bias
    print(output)

    error_gradient = output - required_output

    if int(output) == 1:
        print("values found")
        print(f"Weights: {weights}")
        print(f"Bias: {bias}")
        break

    if error_gradient > 0:
        for i in range(len(weights)):
            weights[i] -= error_gradient
    else:
        for i in range(len(weights)):
            weights[i] += error_gradient

print(output)
