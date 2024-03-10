from neural_network import NeuralNetwork

NN = NeuralNetwork(1, 3, 1)

output = NN.feed_forward([
    0, 1
])

print("output - >", output)
