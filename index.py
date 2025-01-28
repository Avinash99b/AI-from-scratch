#How a neuron works
#Neuron is a simple unit which takes input, does some computation and produces an output
#In this example, we have 3 inputs and 3 weights and 1 bias

#How exactly are we simulating a neuron?

#We take inputs as features of a dataset
#Weights are the parameters which the model will learn, they are adjusted during training
#Bias is a constant which helps the model in learning the patterns in the data

#Eg:- In a dataset, we have 3 features, we will have 3 weights for each feature and 1 bias

#Why do we need weights and bias?

#Think of weights as a parameter which is adjusted to output a specific value

#Bias is a constant which offsets the value of the output after the weights have been multiplied with the inputs

#The weight and bias components are adjusted during training to minimize the loss function

inputs = [1,2,3]
weights = [1,2,3]
bias = 2

# Output = weight * input + bias
#Eg:- i1*w1 + i2*w2 + i3*w3 + bias

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias

print(output)

#Output = 1*1 + 2*2 + 3*3 + 2 = 16
