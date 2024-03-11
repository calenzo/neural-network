import math
from random import uniform

from neural_network import NeuralNetwork

nn = NeuralNetwork(2, 3, 1)

# XOR Problem

dataset = {
    "inputs": [
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ],
    "outputs": [
        [0],
        [1],
        [1],
        [0],
    ]
}

train = True

if train:
    count = 1000
    for x in range(count):
        count -= 1
        index = math.floor(uniform(0, 4))
        nn.train(dataset.get("inputs")[index], dataset.get("outputs")[index])

    if nn.predict([0, 0])[0] < 0.04 and nn.predict([1, 0])[0] > 0.98:
        train = False
        print("Finished")
