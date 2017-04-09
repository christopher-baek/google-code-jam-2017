def occupy(stalls, stall_scores, stall_closest_neighbor_scores, index):
    # mark the stall occupied
    stalls[index] = 1

    # every index < should have the right score decremented one
    for i in xrange(index - 1, 0, -1):
        if stall_scores[i] is not None:
            old_score = stall_scores[i]
            new_right_score = old_score[1] - 1 if old_score[1] > 0 else 0
            new_score = (old_score[0], new_right_score)
            stall_scores[i] = new_score
            stall_closest_neighbor_scores[i] = min(new_score[0], new_score[1])

    # every index > should have the left score decremented one
    for i in xrange(index + 1, len(stall_scores) - 1):
        if stall_scores[i] is not None:
            old_score = stall_scores[i]
            new_left_score = old_score[0] - 1 if old_score[0] > 0 else 0
            new_score = (new_left_score, old_score[1])
            stall_scores[i] = new_score
            stall_closest_neighbor_scores[i] = min(new_score[0], new_score[1])


def choose_stall(stalls, stall_scores, stall_closest_neighbor_scores):

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

        occupy(stalls, stall_scores, stall_closest_neighbor_scores, choice_index)

        return choice_index, max(stall_scores[choice_index][0], stall_scores[choice_index][1]), min(stall_scores[choice_index][0], stall_scores[choice_index][1])
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

            occupy(stalls, stall_scores, stall_closest_neighbor_scores, choice_index)

            return choice_index, max(stall_scores[choice_index][0], stall_scores[choice_index][1]), min(stall_scores[choice_index][0], stall_scores[choice_index][1])
        else:
            lowest_highest_max_min_score_index = 0
            for i in xrange(0, len(stall_max_min_scores)):
                if stall_max_min_scores[i] is not None and stall_max_min_scores[i] == highest_max_min_score:
                    lowest_highest_max_min_score_index = i
                    break

            occupy(stalls, stall_scores, stall_closest_neighbor_scores, lowest_highest_max_min_score_index)

            return lowest_highest_max_min_score_index, max(stall_scores[lowest_highest_max_min_score_index][0], stall_scores[lowest_highest_max_min_score_index][1]), min(stall_scores[lowest_highest_max_min_score_index][0], stall_scores[lowest_highest_max_min_score_index][1])

            
def solve(stall_count, person_count):

    # initialize stalls
    stalls = [0 for i in xrange(0, stall_count + 2)]
    stalls[0] = 1
    stalls[-1] = 1

    # initialize stall scores
    stall_scores = [None]
    stall_closest_neighbor_scores = [None]

    left_score = 0
    right_score = stall_count - 1

    for i in xrange(0, stall_count):
        stall_scores.append((left_score, right_score))
        stall_closest_neighbor_scores.append(min(left_score, right_score))

        left_score += 1
        right_score -= 1

    stall_scores.append(None)
    stall_closest_neighbor_scores.append(None)

    for i in xrange(0, person_count):
        solution = choose_stall(stalls, stall_scores, stall_closest_neighbor_scores)
        stall_scores[solution[0]] = None
        stall_closest_neighbor_scores[solution[0]] = None
        
        #print stalls
        #print stall_scores

    return solution


def main():

    # read number of test cases
    t = int(raw_input())

    # process each test case
    for i in xrange(1, t + 1):
        (stall_count, person_count) = [int(s) for s in raw_input().split(' ')]
        solution = solve(stall_count, person_count)
        print 'Case #{}: {} {}'.format(i, solution[1], solution[2])


if __name__ == '__main__':
    main()

