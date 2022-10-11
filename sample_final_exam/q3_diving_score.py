"""
Question 3
Diving Scores
"""

name = ['Kim', 'Algi', 'Ndomo', 'Zhang', 'Raj', 'Bemet', 'Lee']
score = [9.4, 8.7, 9.1, 8.9, 9.0, 9.3, 9.5]
medal = ['Gold', 'Silver', 'Bronze']

# create new lists to populate sorted data
sorted_name = []
sorted_score = []

# rearrange data
while len(name) != 0:
    highest_score = max(score)  # get max score
    list_node = score.index(highest_score)  # get index of the highest score

    # append node to new lists
    sorted_name.append(name[list_node])
    sorted_score.append(score[list_node])

    # remove node from old lists
    name.pop(list_node)
    score.pop(list_node)

node_length = 8
list_length = len(sorted_name)

# print headers
print('Diver'.ljust(node_length) + 'Score'.ljust(node_length) + 'Medal')

# print scores in descending order
i = 0
for d in range(list_length):
    if i < 3:
        print('%s%s%s' % (sorted_name[d].ljust(node_length), str(sorted_score[d]).ljust(node_length), medal[i]))
        i += 1
    else:
        print('%s%.1f' % (sorted_name[d].ljust(node_length), sorted_score[d]))

print()

print(f"{'Diver':<8}{'Score':<8}{'Medal'}")
i = 0
for d in range(list_length):
    if i < 3:
        print(f"{sorted_name[d]:<8}{str(sorted_score[d]):<8}{medal[i]}")
        i += 1
    else:
        print(f"{sorted_name[d]:<8}{str(sorted_score[d]):<8}")
