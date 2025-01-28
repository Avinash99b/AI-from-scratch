# Modeling a neuron with multiple inputs

inputs = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

weights = [1, 2, 3]

bias = 4

neuron_output = bias

for i in range(len(weights)):
    neuron_output += weights[i] * inputs[i]

print(neuron_output)
