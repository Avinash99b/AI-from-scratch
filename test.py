# Step 1: Initialize weights, bias, and hyperparameters
weights = [0.5, -0.6, 0.1]  # Random initial weights
bias = 0.2                  # Initial bias
learning_rate = 0.01        # Step size for adjustments

# Step 2: Define the dataset
inputs = [1.0, 2.0, -1.5]   # Input data
target = 1.0                # Desired output (ground truth)

# Step 3: Train the neuron without activation
print("Starting Training...")
for epoch in range(10000):  # Train for 10 steps to visualize slowly
    # Step 4: Forward pass (calculate output)
    weighted_sum = 0
    for w, i in zip(weights, inputs):
        weighted_sum += w * i  # Weighted sum
    output = weighted_sum + bias

    # Step 5: Calculate the error (difference from target)
    error = target - output

    # Step 6: Update weights and bias using gradient descent
    gradients = [error * i for i in inputs]  # Gradients for each weight
    print(f"Gradients {gradients}")
    weights = [w + learning_rate * g for w, g in zip(weights, gradients)]
    bias += learning_rate * error  # Update bias

    # Step 7: Print progress for visualization
    print(f"Epoch {epoch + 1}")
    print(f"  Weighted Sum (Output): {output:.4f}")
    print(f"  Error: {error:.4f}")
    print(f"  Updated Weights: {weights}")
    print(f"  Updated Bias: {bias:.4f}")
    print("-" * 30)
