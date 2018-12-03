def generate_adjency_matrix():
    with open(r'in.txt', 'r') as file:
        len_x, len_y = next(file).split(' ')
        if len_x > len_y:
            return None
        next(file)
        adj_array = []
        s = next(file)
        while True:
            for e in s.split(' '):
                adj_array.append(int(e))
            try:
                s = next(file)
            except StopIteration:
                break
        header = adj_array[:int(len_x)+1]
        bias_adj_ranges = [header[i+1]-header[i] for i in range(len(header)-1)]
        adj_mat = {}
        for head_index in range(len(header) - 1):
            adj_mat[head_index] = [adj_array[header[head_index] - 1 + bias] - 1 for bias in range(bias_adj_ranges[head_index])]
        return adj_mat, int(len_y)


def write_result(lst):
    print(lst)


def find_matching(adj_mat):
    result_vector = [-1 for i in range(len(adj_mat))]
    return result_vector


def main():
    adj_mat, len_y = generate_adjency_matrix()
    x_dict = dict.fromkeys(adj_mat.keys(), -1)
    y_dict = {i: -1 for i in range(len_y)}
    if adj_mat:
        write_result(find_matching(adj_mat))


if __name__ == '__main__':
    main()
