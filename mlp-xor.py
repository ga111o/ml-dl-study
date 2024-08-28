import math
import random


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_diff(x):
    return x * (1 - x)


def initialize_weights(input_size, hidden_size, output_size):
    weights_input_hidden = [
        [random.random() for _ in range(hidden_size)] for _ in range(input_size)
    ]
    weights_hidden_output = [random.random() for _ in range(hidden_size)]

    return weights_input_hidden, weights_hidden_output


def forward_propagation(inputs, weights_input_hidden, weights_hidden_output):
    hidden_layer_activation = [0] * len(weights_input_hidden[0])

    for i in range(len(weights_input_hidden)):
        for j in range(len(weights_input_hidden[0])):
            hidden_layer_activation[j] += inputs[i] * \
                weights_input_hidden[i][j]

    hidden_layer_output = []
    for x in hidden_layer_activation:
        hidden_layer_output.append(sigmoid(x))

    output_layer_activation = 0
    for i in range(len(hidden_layer_output)):
        output_layer_activation += hidden_layer_output[i] * \
            weights_hidden_output[i]

    output = sigmoid(output_layer_activation)

    return hidden_layer_output, output


def back_propagation(
    inputs,
    hidden_layer_output,
    output,
    expected_output,
    weights_input_hidden,
    weights_hidden_output,
    learning_rate,
):

    output_error = expected_output - output
    output_delta = output_error * sigmoid_diff(output)

    hidden_error = []
    for i in range(len(hidden_layer_output)):
        hidden_error.append(output_delta * weights_hidden_output[i])

    hidden_delta = []
    for i in range(len(hidden_layer_output)):
        hidden_delta.append(
            hidden_error[i] * sigmoid_diff(hidden_layer_output[i]))

    for i in range(len(weights_hidden_output)):
        weights_hidden_output[i] += (
            learning_rate * output_delta * hidden_layer_output[i]
        )

    for i in range(len(weights_input_hidden)):
        for j in range(len(weights_input_hidden[0])):
            weights_input_hidden[i][j] += learning_rate * \
                hidden_delta[j] * inputs[i]


def train_mlp(
    inputs, outputs, input_size, hidden_size, output_size, learning_rate, epochs
):
    weights_input_hidden, weights_hidden_output = initialize_weights(
        input_size, hidden_size, output_size
    )

    for epoch in range(epochs):
        for i in range(len(inputs)):
            hidden_layer_output, output = forward_propagation(
                inputs[i], weights_input_hidden, weights_hidden_output
            )
            back_propagation(
                inputs[i],
                hidden_layer_output,
                output,
                outputs[i],
                weights_input_hidden,
                weights_hidden_output,
                learning_rate,
            )

    return weights_input_hidden, weights_hidden_output


inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 1, 1, 0]


input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 30000


weights_input_hidden, weights_hidden_output = train_mlp(
    inputs, outputs, input_size, hidden_size, output_size, learning_rate, epochs
)


for input_data in inputs:
    _, output = forward_propagation(
        input_data, weights_input_hidden, weights_hidden_output
    )
    print(f"input: {input_data}, output_hat: {output:.1f}")
