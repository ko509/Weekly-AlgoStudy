
def solution(commands):
    answer = []
    parents = [[(r, c) for c in range(51)] for r in range(51)]
    table = [["EMPTY"] * 51 for _ in range(51)]

    # union-find 알고리즘
    def union_parents(r1, c1, r2, c2):
        parents[r2][c2] = parents[r1][c1]

    def find_parents(r ,c):
        if parents[r][c] == (r, c):
            return parents[r][c]
        pr, pc = parents[r][c]
        parents[r][c] = find_parents(pr, pc)
        return parents[r][c] # parents 가 가지고 있던 값을 리턴

    def PRINT(r, c):
        pr, pc = find_parents(r, c)
        answer.append(table[pr][pc])

    def UPDATE(r, c, value):
        pr, pc = find_parents(r, c) # ????
        table[pr][pc] = value

    def UPDATE2(value1, value2):
        # value1 을 가지고 있는 모든 셀 선택하기
        for i in range(1, 51):
            for j in range(1, 51):
                pr, pc = find_parents(i, j)
                if table[pr][pc] == value1:
                    table[pr][pc] = value2

    def MERGE(r1, c1, r2, c2):
        r1, c1 = find_parents(r1, c1)
        r2, c2 = find_parents(r2, c2)

        if (r1, c1) == (r2, c2):
            return
        if table[r1][c1] != "EMPTY":
            union_parents(r1, c1, r2, c2)
        else:
            union_parents(r2, c2, r1, c1)

    def UNMERGE(r, c):
        # parents 찾기
        pr, pc = find_parents(r, c)
        # parents 에 저장된 값
        original = table[pr][pc]

        merge_list = []
        for x in range(51):
            for y in range(51):
                px, py = find_parents(x, y)
                if (px, py) == (pr, pc):
                    merge_list.append((x, y))

        for x, y in merge_list:
            parents[x][y] = (x, y)
            if (x, y) != (r, c):
                table[x][y] = "EMPTY"
            else:
                table[x][y] = original

    for command in commands:
        cmd, *args = command.split()
        if cmd == "UPDATE":
            if len(args) == 3:
                r, c, value = args
                UPDATE(int(r), int(c), value)
            elif len(args) == 2: # 2
                value1, value2 = args
                UPDATE2(value1, value2)
        elif cmd == "MERGE":
            r1, c1, r2, c2 = map(int, args)
            MERGE(r1, c1, r2, c2)
        elif cmd == "UNMERGE":
            r, c = map(int, args)
            UNMERGE(r, c)
        else:
            r, c = map(int, args)
            PRINT(r, c)


    return answer