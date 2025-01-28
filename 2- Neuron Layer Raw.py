# Modeling 3 neurons in a layer

inputs = [1, 2, 3]

# Weights for each neuron
weights1 = [1, 2, 3]
weights2 = [4, 5, 6]
weights3 = [7, 8, 9]

# Bias for each neuron
bias1 = 2
bias2 = 3
bias3 = 4

# Output = weight * input + bias

output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + bias3]

print(output)
