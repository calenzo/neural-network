import math

from matrix import Matrix


def sigmoid(x: int, i, j):
    return 1 / (1 + math.exp(-x))


class NeuralNetwork:
    def __init__(self,
                 input_nodes: int,
                 hidden_nodes: int,
                 output_nodes: int,):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.bias_input_to_hidden = Matrix(self.hidden_nodes, 1)
        self.bias_input_to_hidden.randomize()
        self.bias_hidden_to_output = Matrix(self.output_nodes, 1)
        self.bias_hidden_to_output.randomize()

        self.weights_input_to_hidden = Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_input_to_hidden.randomize()

        self.weights_hidden_to_output = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_hidden_to_output.randomize()

        print(self.bias_input_to_hidden.data)
        print(self.bias_hidden_to_output.data)

    def feed_forward(self, arr: list):
        input_matrix = Matrix.array_to_matrix(arr)

        hidden = Matrix.multiply(self.weights_input_to_hidden, input_matrix)
        hidden = Matrix.add(hidden, self.bias_input_to_hidden)
        hidden.map(sigmoid)

        output = Matrix.multiply(self.weights_hidden_to_output, hidden)
        output = Matrix.add(output, self.bias_hidden_to_output)
        output.map(sigmoid)

        return output.data
