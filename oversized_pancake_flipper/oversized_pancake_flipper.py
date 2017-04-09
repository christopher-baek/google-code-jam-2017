

def flip(pancakes, start, spatula_size):
    for i in xrange(start, start + spatula_size):
        if pancakes[i] == '+':
            pancakes[i] = '-'
        else:
            pancakes[i] = '+'


def is_all_happy(pancakes):
    return pancakes.count('+') == len(pancakes)


def solve(pancake_data, spatula_size):
    pancakes = list(pancake_data)

    if is_all_happy(pancakes):
        return 0

    impossible = False
    flip_count = 0

    while not is_all_happy(pancakes) and not impossible:

        #print pancakes

        for i in xrange(0, len(pancakes)):
            if pancakes[i] == '+':
                continue

            if (i + spatula_size) > len(pancakes):
                #print 'This is impossible!'
                impossible = True
            else:
                #print 'Flipping', spatula_size, 'from', i
                flip(pancakes, i, spatula_size)
                flip_count += 1

            break

    if impossible:
        return 'IMPOSSIBLE'
    else:
        return flip_count


def main():

    # read number of test cases
    t = int(raw_input())

    # process each test case
    for i in xrange(1, t + 1):
        pancake_data, spatula_size = raw_input().split(' ')
        spatula_size = int(spatula_size)

        solution = solve(pancake_data, spatula_size)
        print 'Case #{}: {}'.format(i, solution)


if __name__ == '__main__':
    main()

