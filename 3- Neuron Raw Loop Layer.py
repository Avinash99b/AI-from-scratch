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

#Converting the raw code

weights = [weights1, weights2, weights3]

biases = [bias1, bias2, bias3]


# Output = weight * input + bias

layer_output = []

for i in range(len(weights)):
    neuron_weights = weights[i]
    bias = biases[i]

    neuron_output = 0
    for j in range(len(neuron_weights)):
        weight = neuron_weights[j]
        neuron_input = inputs[i]

        neuron_output += neuron_input * weight

    neuron_output += bias

    layer_output.append(neuron_output)

print(layer_output)