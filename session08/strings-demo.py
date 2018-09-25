team = 'New England Patriots'
letter = team[1]  # The expression in brackets is called an index.
# print(letter)

# print(team[0])


# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)


team = 'New England Patriots'

# print(team)


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


# print(find(team, 'a'))


def count(s, letter):
    c = 0
    for each in s:
        if each == letter:
            c += 1
    return c


print(count(team, 'a'))  # should be 2

print(count(team, ' '))

new_team = team.upper()
print(new_team)
