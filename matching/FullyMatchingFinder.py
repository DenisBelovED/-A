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
        adj_mat = [[0 for g in range(int(len_y))] for i in range(int(len_x))]
        for head_index in range(len(header) - 1):
            for bias in range(bias_adj_ranges[head_index]):
                adj_mat[head_index][adj_array[header[head_index]-1+bias]-1] = -1
        return adj_mat


def write_result(lst):
    print(lst)


def find_matching(adj_mat):
    result_vector = [-1 for i in range(len(adj_mat))]
    for i in range(len(adj_mat)):
        result_vector, adj_mat = finder(result_vector, adj_mat, i)
    return result_vector


def main():
    adj_mat: list[list] = generate_adjency_matrix()
    if adj_mat:
        write_result(find_matching(adj_mat))


if __name__ == '__main__':
    main()
