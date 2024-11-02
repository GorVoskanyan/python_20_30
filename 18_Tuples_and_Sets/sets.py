# my_set = {'a', 'a', 'a', 'b', 'c'}
# print(my_set)

# deleted = my_set.pop()
# my_set.clear()
# my_set.discard('w')
# my_set.remove('w')    # TypeError
# print(my_set)
# print(deleted)

# my_set.add('d')
# other_set = {1, 2, 3, 'b'}
# my_set.update(other_set)
# my_set += other_set     # TypeError
# print(my_set)

# empty = set()
# print(type(empty))


# s1 = {1, 2, 3, 4, 5}
# s2 = {3, 4, 5, 6, 7}

# s3 = s1.intersection(s2)
# s3 = s1 & s2
# s1.intersection_update(s2)
# print(s1)

# s3 = s1.difference(s2)
# s3 = s1 - s2
# s1.difference_update(s2)
# print(s1)

# s3 = s1.symmetric_difference(s2)
# s3 = s1 ^ s2
# s1.symmetric_difference_update(s2)
# print(s1)

# s3 = s1.union(s2)
# s3 = s1 | s2
# print(s3)


# s1 = {1, 2, 3}
# s2 = {1, 2, 3, 4, 5}

# print(s1.isdisjoint(s2))
# print(s2.issuperset(s1))
# print(s1.issubset(s2))


# words = ['this', 'is', 'a', 'test', 'of', 'lesson']
# letters = ['s', 'e']

# result = [word for word in words if set(word).issuperset(set(letters))]
# for word in words:
#     if set(word).issuperset(set(letters)):
#         result.append(word)

# result = [word for word in words if set(word).isdisjoint(set(letters))]
# print(result)

# my_frozen_set = frozenset({1, 2, 3})
# s = {1, 'a', True, my_frozen_set}
# print(s)