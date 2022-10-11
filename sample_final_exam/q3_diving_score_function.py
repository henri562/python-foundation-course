"""
Question 3
Diving Scores
"""

name = ['Kim', 'Algi', 'Ndomo', 'Zhang', 'Raj', 'Bemet', 'Lee']
score = [9.4, 8.7, 9.1, 8.9, 9.0, 9.3, 9.5]
medal = ['Gold', 'Silver', 'Bronze']


def print_score(name_list, score_list, medals):
    # print headers
    node_length = 8
    print('Diver'.ljust(node_length) + 'Score'.ljust(node_length) + 'Medal')

    # rearrange data
    i = 0
    while len(name_list) != 0:
        highest_score = max(score_list)  # get max score
        list_node = score_list.index(highest_score)  # get index of the highest score

        # print scores in descending order
        if i < 3:
            print('%s%s%s' % (name_list[list_node].ljust(node_length),
                              str(score[list_node]).ljust(node_length), medals[i]))
            i += 1
        else:
            print('%s%.1f' % (name_list[list_node].ljust(node_length), score[list_node]))

        # remove node from lists
        name_list.pop(list_node)
        score_list.pop(list_node)


print_score(name, score, medal)
