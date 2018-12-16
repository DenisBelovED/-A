def generate_adjency_matrix():
    with open('in.txt', 'r') as file:
        next(file)
        adj_mat = [list(map(int, s.split())) for s in file]
    return adj_mat


def write_result(res):
    with open('out.txt', 'w') as file:
        file.write(str(res))


def find_max_profit(adj_mat):
    return adj_mat


def main():
    adj_mat = generate_adjency_matrix()
    write_result(find_max_profit(adj_mat))


if __name__ == '__main__':
    main()
