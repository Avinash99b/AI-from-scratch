import numpy as np

# Modeling 3 neurons in a layer

inputs = [1, 2, 3]

# Converting the raw code

weights = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

biases = [2, 3, 4]

neurons_output = np.dot(weights, inputs) + biases

print(neurons_output)

neurons_output = np.dot(inputs,weights) + biases

print(neurons_output)
