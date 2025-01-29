import numpy as np


#3 Layer Neuron
class Neuron:
    weights = []
    inputs = []
    bias =0
    def __init__(self,bias):
        self.weights = np.random.rand(2,3)
        self.bias = bias

    def forward(self,inputs):
        self.inputs = inputs

        output = np.dot(self.weights,inputs)

        return output + self.bias



neuron = Neuron(0)

print(neuron.weights)
print(neuron.forward(np.array([[100,20,50]]).T))