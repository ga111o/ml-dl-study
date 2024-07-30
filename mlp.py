import random


def sigmoid(x):
    return 1 / (1 + 2.718281 ** (-x))


def sigmoid_diff(x):
    sig = sigmoid(x)
    return sig * (1 - sig)


def init(
    inputValue: int = 1,
    inputValue2: int = 1,
    input_layer_node_num: int = 2,
    hidden_layer_node_num: int = 4,
    hidden_layer_num: int = 2,
    output_layer_node_num: int = 1,
):
    weight_input2hidden = []
    weight_hidden = []
    weight_hidden2output = []

    # weight_input2hidden
    for _ in range(input_layer_node_num):
        temp = []
        for _ in range(hidden_layer_node_num):
            temp.append(random.random())
        weight_input2hidden.append(temp)

    # weight_hidden2output
    for _ in range(output_layer_node_num):
        temp = []
        for _ in range(hidden_layer_node_num):
            temp.append(random.random())
        weight_hidden2output.append(temp)

    # weight_hidden
    for _ in range(hidden_layer_num):
        one_hidden_layer = []
        for _ in range(hidden_layer_node_num):
            temp = []
            for _ in range(hidden_layer_node_num):
                temp.append(random.random())
            one_hidden_layer.append(temp)
        weight_hidden.append(one_hidden_layer)

    print(
        f"""
input to hidden
{weight_input2hidden}
===============================

hidden
{weight_hidden}
===============================

hidden to output
{weight_hidden2output}
        """
    )


init()
