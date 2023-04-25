from random import choice, random, randint, randrange, sample, shuffle
from string import ascii_lowercase
from itertools import product

"""
Code representation:

repeat 5
{
a++
repeat 3
{
x++
}
b++
repeat 7
{
x++
y++
}
y++
z++
}
z++

into

[(5, ['a', (3, ['x']), 'b', (7, ['x', 'y']), 'y', 'z'), 'z']
"""

VARS = [''.join(u) for u in product(ascii_lowercase, repeat=4)]
LIMIT = 2 ** 20


def deep_shuffle(l):
    for k in l:
        if type(k) == list:
            deep_shuffle(k)
    shuffle(l)


def generate_code(num_vars, num_loops, MUL=1, RATIO=1/4, END_THRESHOLD=0, loop_weight=0.8, REP_LIMIT=10, DEPTH=0, max_depth=64):
    var = sample(VARS, num_vars)
    res = []
    n = 0

    # just throw in a few ++
    if 2 * MUL > LIMIT or DEPTH >= max_depth:
        res = []
        for _ in range(END_THRESHOLD):
            res.append(choice(var))
        deep_shuffle(res)
        return res

    while num_loops > 0:
        rand = random()
        # start a repeat block
        if rand < RATIO and 2 * MUL <= LIMIT and DEPTH < max_depth:
            rep = randint(2, min(REP_LIMIT, LIMIT // MUL))
            num_loops -= 1
            new_num_loops = randint(0, int(num_loops * loop_weight))
            new_code = generate_code(num_vars, new_num_loops, MUL * rep, RATIO, END_THRESHOLD, loop_weight, REP_LIMIT, DEPTH + 1, max_depth)
            if len(new_code) > 0:
                res.append((rep, new_code))
            num_loops -= new_num_loops
        # append some ++
        else:
            res.append(choice(var))
        n += 1

    if END_THRESHOLD > 0:
        while len(res) < END_THRESHOLD or any(type(k) != str for k in res[-END_THRESHOLD:]):
            res.append(choice(var))
    
    deep_shuffle(res)
    return res


def dump_code(code, prefix='', pad=''):
    res = ''
    for c in code:
        if type(c) == tuple:
            rep, new_code = c
            res += prefix + f'repeat {rep}\n'
            res += prefix + '{\n'
            res += dump_code(new_code, prefix + pad, pad)
            res += prefix + '}\n'
        else:
            res += prefix + f'{c}++\n'
    return res


def gen_deep():
    # deep recursion
    N = 100
    fn = 'q2_deep_recursion.in'
    with open(fn, 'w') as fout:
        fout.write(str(N) + '\n')
        for k in range(N):
            code = generate_code(20, 1000, RATIO=0.8, END_THRESHOLD=1, REP_LIMIT=3, max_depth=64, loop_weight=1)
            s = dump_code(code)
            fout.write(str(s.count('\n')) + '\n')
            fout.write(s)


def gen_light():
    N = 100
    fn = 'q2_light_recursion.in'
    with open(fn, 'w') as fout:
        fout.write(str(N) + '\n')
        for k in range(N):
            code = generate_code(20, 300, RATIO=0.25, END_THRESHOLD=5, loop_weight=k / 100)
            s = dump_code(code)
            fout.write(str(s.count('\n')) + '\n')
            fout.write(s)


def gen_no_repeat():
    N = 100
    fn = 'q2_no_repeat.in'
    with open(fn, 'w') as fout:
        fout.write(str(N) + '\n')
        for k in range(N):
            code = generate_code(100, 0, END_THRESHOLD=(k // 10 + 1) * 500, max_depth=0)
            s = dump_code(code)
            fout.write(str(s.count('\n')) + '\n')
            fout.write(s)


def gen_depth_one_repeat():
    N = 100
    fn = 'q2_depth_one_repeat.in'
    with open(fn, 'w') as fout:
        fout.write(str(N) + '\n')
        for k in range(N):
            code = generate_code((k // 10 + 1) * 10, 5000, RATIO=0.6, END_THRESHOLD=20, max_depth=1)
            s = dump_code(code)
            fout.write(str(s.count('\n')) + '\n')
            fout.write(s)


if __name__ == "__main__":
    gen_deep()
    gen_light()
    gen_no_repeat()
    gen_depth_one_repeat()
