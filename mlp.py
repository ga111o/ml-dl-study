import random


def sigmoid(x):
    return 1 / (1 + 2.718281 ** (-x))


def sigmoid_diff(x):
    sig = sigmoid(x)
    return sig * (1 - sig)


def init(
    input_layer_node_num: int = 2,
    hidden_layer_node_num: int = 4,
    hidden_layer_num: int = 1,
    output_layer_node_num: int = 1,
):

    weight_input2hidden = []
    weight_hidden = []
    weight_hidden2output = []

    # weight_input2hidden
    for _ in range(input_layer_node_num):
        temp = []
        for _ in range(hidden_layer_node_num):
            temp.append(round(random.random(), 8))
        weight_input2hidden.append(temp)

    # weight_hidden2output
    for _ in range(output_layer_node_num):
        temp = []
        for _ in range(hidden_layer_node_num):
            temp.append(round(random.random(), 8))
        weight_hidden2output.append(temp)

    # weight_hidden
    for _ in range(hidden_layer_num):
        one_hidden_layer = []
        for _ in range(hidden_layer_node_num):
            temp = []
            for _ in range(hidden_layer_node_num):
                temp.append(round(random.random(), 8))
            one_hidden_layer.append(temp)
        weight_hidden.append(one_hidden_layer)

    print(
        f"""
        | input to hidden
        | {weight_input2hidden}
        | ===============================
        | 
        | hidden
        | {weight_hidden}
        | ===============================
        | 
        | hidden to output
        | {weight_hidden2output}
        """
    )
    return weight_input2hidden, weight_hidden, weight_hidden2output


def weighted_sum(
        input_param1: bool,
        input_param2: bool,
        weight_input2hidden: list,
        weight_hidden: list,
        weight_hidden2output: list,
        input_layer_node_num: int = 2,
        hidden_layer_node_num: int = 4,
        hidden_layer_num: int = 1,
        output_layer_node_num: int = 1
):

    input1 = 1 if input_param1 else 0
    input2 = 1 if input_param2 else 0

    input2hiddenActivated = []

    # 첫 번째 히든레이어 층
    for i in range(hidden_layer_node_num):
        weighted = (
            input1 * weight_input2hidden[0][i]) + (input2 * weight_input2hidden[1][i])

        activated = sigmoid(weighted)
        input2hiddenActivated.append(activated)

    print(input2hiddenActivated)

    # # 두 번째 이후 히든레이어 층

    # hidden to output

    final_summed = 0
    for i in range(hidden_layer_node_num):
        final_summed = weight_hidden2ouput[0][i] * input2hiddenActivated[i]

        print(final_summed)

    y_hat = sigmoid(final_summed)

    return y_hat


weight_input2hidden, weight_hidden, weight_hidden2ouput = init()

for i in range(1000):

    for k in range(4):

        y_hat = weighted_sum(True, True, weight_input2hidden,
                             weight_hidden, weight_input2hidden)
