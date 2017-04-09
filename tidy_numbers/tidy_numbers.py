

def digits_to_number(digits):
    string_digits = [str(i) for i in digits]
    string_number = ''.join(string_digits)
    return int(string_number)


def number_to_digits(number):
    number_string = str(number)
    number_string_digits = list(number_string)
    digits = [int(i) for i in number_string_digits]
    return digits


def is_tidy(digits):
    tidy = True

    for i in xrange(1, len(digits)):
        if digits[i] < digits[i - 1]:
            #print 'Not tidy because', digits[i], '<', digits[i - 1]
            tidy = False
            break

    return tidy

def solve_0(digits):
    for j in xrange(1, len(digits)):
        i = j - 1

        if digits[j] < digits[i]:
            digits[i] -= 1

            for k in xrange(j, len(digits)):
                digits[k] = 9

            break


def solve(last_number_counted):
    #print 'Input:', last_number_counted
    last_number_counted_digits = number_to_digits(last_number_counted)

#    if last_number_counted_digits[len(last_number_counted_digits) - 1] == 0:
#        new_last_number_counted = last_number_counted - 1
#        print 'New input:', new_last_number_counted
#        last_number_counted_digits = number_to_digits(new_last_number_counted)
#
#    for j in xrange(len(last_number_counted_digits) - 1, 0, -1):
#        i = j - 1
#
#        while last_number_counted_digits[i] > last_number_counted_digits[j]:
#            last_number_counted_digits[i] -= 1
#
#        print last_number_counted_digits

    while not is_tidy(last_number_counted_digits):
        #print last_number_counted_digits
        solve_0(last_number_counted_digits)


    return str(digits_to_number(last_number_counted_digits))
    

def main():

    # read number of test cases
    t = int(raw_input())

    # process each test case
    for i in xrange(1, t + 1):
        last_number_counted = int(raw_input())
        solution = solve(last_number_counted)
        print 'Case #{}: {}'.format(i, solution)


if __name__ == '__main__':
    main()

