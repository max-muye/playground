def solve_n_queens(n):
    def output(n):
        for i in n:
            for j in range(len(n)):
                if i != j:
                    print("O", end=" ")
                else:
                    print("X", end=" ")
            print()
        print()

    def backtrack(row, queens, count):
        if row == n:
            count[0] += 1
            output(queens)
            return

        for col in range(n):
            valid = True
            for prev_row in range(row):
                if queens[prev_row] == col or row - prev_row == abs(
                    col - queens[prev_row]
                ):
                    valid = False
                    break

            if valid:
                queens[row] = col
                backtrack(row + 1, queens, count)

    queens = [-1] * n
    count = [0]  # 使用列表存储计数，以便在递归中修改
    backtrack(0, queens, count)
    print(count[0])
    print()


while True:
    solve_n_queens(int(input()))
