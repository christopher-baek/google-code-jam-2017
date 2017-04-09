def score(stalls, index):
    left_index = index
    for i in xrange(index - 1, -1, -1):
        if stalls[i] == 1:
            left_index = i
            break

    right_index = index
    for i in xrange(index + 1, len(stalls)):
        if stalls[i] == 1:
            right_index = i
            break

    left_score = index - left_index - 1
    right_score = right_index - index - 1

    return left_score, right_score


def choose_stall(stalls):
    # calculate left and right scores for each stall
    stall_scores = [None] * len(stalls)
    for i in xrange(0, len(stalls)):
        stall_scores[i] = score(stalls, i) if stalls[i] == 0 else None

    #print 'Stall Scores:', stall_scores


    # calculate the closest neighbor (min of scores)
    stall_closest_neighbor_scores = [None] * len(stalls)
    for i in xrange(0, len(stall_scores)):
        stall_closest_neighbor_scores[i] = min(stall_scores[i][0], stall_scores[i][1]) if stall_scores[i] is not None else None

    #print 'Stall Closest Neighbor Scores:', stall_closest_neighbor_scores


    # get stalls with farthest closest neighbor (s for which min(L, R) is maximal)
    farthest_neighbor = max(stall_closest_neighbor_scores)

    stall_options = [None] * len(stall_closest_neighbor_scores)
    for i in xrange(0, len(stall_closest_neighbor_scores)):
        stall_options[i] = farthest_neighbor if stall_closest_neighbor_scores[i] == farthest_neighbor else None

    #print 'Stall Options:', stall_options


    # if there is only one, occupy it
    if stall_options.count(farthest_neighbor) == 1:
        choice_index = 0
        for i in xrange(0, len(stall_options)):
            if stall_options[i] is not None and stall_options[i] == farthest_neighbor:
                choice_index = i
                break

        stalls[choice_index] = 1

        return max(stall_scores[choice_index][0], stall_scores[choice_index][1]), min(stall_scores[choice_index][0], stall_scores[choice_index][1])
    else:
        # calculate the max(L, R) scores
        stall_max_min_scores = [None] * len(stall_options)
        for i in xrange(0, len(stall_options)):
            stall_max_min_scores[i] = max(stall_scores[i][0], stall_scores[i][1]) if stall_options[i] is not None else None

        #print 'Second Chance Scores:', stall_max_min_scores

        # choose where the max(L, R) is maximal
        highest_max_min_score = max(stall_max_min_scores)

        # if there is only one, occupy it
        if stall_max_min_scores.count(highest_max_min_score) == 1:
            choice_index = 0
            for i in xrange(0, len(stall_max_min_scores)):
                if stall_max_min_scores[i] is not None and stall_max_min_scores[i] == highest_max_min_scores:
                    choice_index = i

            stalls[choice_index] = 1

            return max(stall_scores[choice_index][0], stall_scores[choice_index][1]), min(stall_scores[choice_index][0], stall_scores[choice_index][1])
        else:
            lowest_highest_max_min_score_index = 0
            for i in xrange(0, len(stall_max_min_scores)):
                if stall_max_min_scores[i] is not None and stall_max_min_scores[i] == highest_max_min_score:
                    lowest_highest_max_min_score_index = i
                    break

            stalls[lowest_highest_max_min_score_index] = 1

            return max(stall_scores[lowest_highest_max_min_score_index][0], stall_scores[lowest_highest_max_min_score_index][1]), min(stall_scores[lowest_highest_max_min_score_index][0], stall_scores[lowest_highest_max_min_score_index][1])

            
def solve(stall_count, person_count):

    stalls = [0 for i in xrange(0, stall_count + 2)]
    stalls[0] = 1
    stalls[-1] = 1

    for i in xrange(0, person_count):
        solution = choose_stall(stalls)

    return solution


def main():

    # read number of test cases
    t = int(raw_input())

    # process each test case
    for i in xrange(1, t + 1):
        (stall_count, person_count) = [int(s) for s in raw_input().split(' ')]
        solution = solve(stall_count, person_count)
        print 'Case #{}: {} {}'.format(i, solution[0], solution[1])


if __name__ == '__main__':
    main()

