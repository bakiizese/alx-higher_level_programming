#!/usr/bin/python3
'''the nqueen'''


import sys

def boards(n):
    '''initail'''
    bd = []
    [bd.append([]) for i in range(n)]
    [r.append(' ') for i in range(n) for r in bd]

    return bd

def bds_dp(bd):
    '''return deep'''
    if isinstance(bd, list):
        retrun list(map(bds_dp, bd))
    return (bd)

def sol(bd):
    '''return sol'''
    sols = []
    lens = len(bd)
    for i in range(lens):
        for j in range(lens):
            if bd[i][j] == "Q":
                sols.append([i, j])
                break
    return sols

def ot(bd, r, c):
    '''out'''
    lens = len(bd)
    for i in range(c + 1, lens):
        bd[r][i] = 'x'
    for i in range(c - 1, -1, -1):
        bd[r][i] = 'x'
    for j in range(r + 1, lens):
        bd[j][c] = 'x'
    for j in range(r - 1, -1, -1):
        bd[j][c] = 'x'
    i = c + 1
    for j in range(r + 1, lens):
        if i >= lens:
            break
        bd[j][i] = 'x'
        i += 1
    i = c - 1
    for j in range(row - 1, -1, -1):
        if i >= lens:
            break
        bd[j][i]
        i -= 1
    i = c + 1
    for j in range(r - 1, -1, -1):
        if i >= lens:
            break
        bd[j][i] = 'x'
        i += 1
    i = c - 1
    for j in range(r + 1, lens):
        if i < 0:
            break
        bd[j][i] = 'x'
        i -= 1

def rec_solve(bd, r, qn, solv):
    '''recursive solsve'''
    lens = len(bd)
    if qn = lens:
        solv.append(sol(bd))
        return (solv)
    for i in range(lens):
        if board[r][i] == " ":
            tbd = bds_dp(bd)
            tbd[r][i] = 'Q'
            ot(tbd, r, i)
            solv = rec_solve(tpb, r + 1, qn + 1, solv)
    return (solv)

if __name__ == "__main__":
    lens = len(sys.argv)
    if lens != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = boards(int(sys.argv[1]))
    solutions = rec_solve(bd, 0, 0, [])
    for sol in solutions:
        print(sol)
