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


def pair_builder(result_vector, adj_mat, i):
    for v in range(len(adj_mat[i])):
        if adj_mat[i][v] == 1:
            for g in range(len(result_vector)):
                if result_vector[g] == v:
                    return g, v
    return None, None


def finder(result_vector, adj_mat, i):
    if result_vector[i] != -1:
        return result_vector, adj_mat

    for v in range(len(adj_mat[i])):
        if adj_mat[i][v] == -1:
            adj_mat[i][v] = 1
            result_vector[i] = v
            for e in range(len(adj_mat)):
                if adj_mat[e][v] == -1:
                    adj_mat[e][v] = 1
            return result_vector, adj_mat

    m_extended_chain = [i]
    ind = i
    while True:
        g, v = pair_builder(result_vector, adj_mat, ind)
        if g and v:
            m_extended_chain.append(v)
            m_extended_chain.append(g)
            ind = g
        else:
            break
    return m_extended_chain



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
