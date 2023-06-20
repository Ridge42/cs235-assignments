from byu_pytest_utils import compile_cpp, max_score, test_files
import pytest
import subprocess as sp


@pytest.fixture(scope='module')
def maze_bin():
    return compile_cpp('maze.cpp', output_exec='maze')


def check_solution(maze_file, solution_file):
    with open(maze_file) as file:
        R, C, D = (int(dim) for dim in file.readline().split())
        maze = [space for line in file for space in line.split()]

    def maze_at(r, c, l):
        return maze[l * R * C + r * C + c]

    with open(solution_file) as file:
        assert file.readline().strip(
        ) == 'SOLUTION', f'{solution_file} must start with "SOLUTION"'
        path = [tuple(int(i) for i in line.split()) for line in file]

    for line, (r, c, l) in enumerate(path):
        assert maze_at(
            r, c, l) == '1', f'[Line {line + 2}]: {r} {c} {l} is not an open space'

    for line, ((r, c, l), (rp, cp, lp)) in enumerate(zip(path[1:], path[:-1])):
        assert abs(r - rp) + abs(c - cp) + abs(l -
                                               lp) == 1, f'[Line {line + 3}]: moving from {rp} {cp} {lp} to {r} {c} {l} is too far'

    assert path[0] == (0, 0, 0), '[Line 2]: the solution must start at 0 0 0'
    assert path[-1] == (R-1, C-1, D -
                        1), f'[Line {len(path) + 1}]: the solution must end at {R-1} {C-1} {D-1}'


@max_score(15)
def test_solvable1(maze_bin):
    sp.run([maze_bin, test_files / 'solvable1.maze.txt',
           'solvable1.solution.txt'], check=True)
    check_solution(test_files / 'solvable1.maze.txt', 'solvable1.solution.txt')


@max_score(15)
def test_solvable2(maze_bin):
    sp.run([maze_bin, test_files / 'solvable2.maze.txt',
           'solvable2.solution.txt'], check=True)
    check_solution(test_files / 'solvable2.maze.txt', 'solvable2.solution.txt')


@max_score(20)
def test_solvable3(maze_bin):
    sp.run([maze_bin, test_files / 'solvable3.maze.txt',
           'solvable3.solution.txt'], check=True)
    check_solution(test_files / 'solvable3.maze.txt', 'solvable3.solution.txt')


@max_score(15)
def test_unsolvable1(maze_bin):
    sp.run([maze_bin, test_files / 'unsolvable1.maze.txt',
           'unsolvable1.solution.txt'], check=True)
    with open('unsolvable1.solution.txt') as fin:
        assert fin.read().strip() == 'NO SOLUTION'


@max_score(15)
def test_unsolvable2(maze_bin):
    sp.run([maze_bin, test_files / 'unsolvable2.maze.txt',
           'unsolvable2.solution.txt'], check=True)
    with open('unsolvable2.solution.txt') as fin:
        assert fin.read().strip() == 'NO SOLUTION'


@max_score(20)
def test_unsolvable3(maze_bin):
    sp.run([maze_bin, test_files / 'unsolvable3.maze.txt',
           'unsolvable3.solution.txt'], check=True)
    with open('unsolvable3.solution.txt') as fin:
        assert fin.read().strip() == 'NO SOLUTION'
