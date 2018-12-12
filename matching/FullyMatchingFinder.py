def generate_adjency_matrix():
    with open(r'in.txt', 'r') as file:
        len_x, len_y = next(file).split(' ')
        len_x = int(len_x)
        len_y = int(len_y)
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
        header = adj_array[:len_x + 1]
        bias_adj_ranges = [header[i + 1] - header[i] for i in range(len(header) - 1)]
        adj_mat = [[0 for j in range(len_y)] for i in range(len_x)]
        for head_index in range(len(header) - 1):
            for bias in range(bias_adj_ranges[head_index]):
                adj_mat[head_index][adj_array[header[head_index] - 1 + bias] - 1] = 1
        return adj_mat, len_y


def write_result(lst):
    print(lst)


# если есть незанятая вершина из Y, то вернёт её индекс, иначе вернёт -1
def select_free_vertex(adj_mat, x_i, res):
    for y_i in range(len(adj_mat[x_i])):
        if adj_mat[x_i][y_i] == 1:
            if not (y_i in res):
                return y_i
    return -1


def create_mt(adj_mat, res, x_i):
    y_i = adj_mat[x_i].index(1)  # возьмём первую попавшуюся вершину y_i
    x_j = res.index(y_i)  # будем смотреть, какой х_j с ней связан


# метод делает проверку для x, существует ли свободная вершина в Y
# если да, то result[x] = y
# иначе начинает строить увеличивающуюся M-цепь
def dfs_x(adj_mat, temp_res, x_i):
    if temp_res[x_i] == -1:  # проверяем, есть ли паросочетание
        y_i = select_free_vertex(adj_mat, x_i, temp_res)  # выбираем свободный y
        if y_i == -1:
            # свободного y нет, строим увеличивающуюся M-цепь
            mt_chain = []
        else:
            # свободный y есть, заносим его в ответ, и возвращаем изменённый массив паросочетаний
            temp_res[x_i] = y_i
            return temp_res
    else:
        # паросочетание есть, ничего не изменяем
        return temp_res


def find_matching(adj_mat):
    temp_res = [-1 for i in range(len(adj_mat))]
    for i in range(len(adj_mat)):
        temp_res = dfs_x(adj_mat, temp_res, i)
    return temp_res


def main():
    adj_mat, len_y = generate_adjency_matrix()
    if adj_mat:
        write_result(find_matching(adj_mat))


if __name__ == '__main__':
    main()
