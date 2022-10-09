"""
Question 3
Diving Scores
"""

name = ['Kim', 'Algi', 'Ndomo', 'Zhang', 'Raj', 'Bemet', 'Lee']
score = [9.4, 8.7, 9.1, 8.9, 9.0, 9.3, 9.5]
medal = ['Gold', 'Silver', 'Bronze']

# print headers
node_length = 8
print('Diver'.ljust(node_length) + 'Dive'.ljust(node_length) + 'Medal')

# rearrange and print data
i = 0
while len(name) != 0:
    highest_score = max(score)  # get max score
    list_node = score.index(highest_score)  # get index of the highest score

    # print scores in descending order
    if i < 3:
        print('%s%s%s' % (name[list_node].ljust(node_length), str(score[list_node]).ljust(node_length), medal[i]))
        i += 1
    else:
        print('%s%.1f' % (name[list_node].ljust(node_length), score[list_node]))

    # remove node from lists
    name.pop(list_node)
    score.pop(list_node)
