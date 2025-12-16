# y = "tech with yogi"
# words = y.split()
# rev = words[::-1]
# print(rev)

# def reverse_words(sentense):
#     return ' ' .join(sentense.split()[::-1])


# print(reverse_words("this is best game in india"))

# def reverse_words(sentsence):
#     return ' '.join(sentsence.split()[::-1])

# print(reverse_words("yogi is best name in india"))

# def reversed_words(sentence):
#     return ' '.join(sentence.split()[::-1])

# print(reversed_words("the name is good but not best of all time."))

numbers = [1, 2, 2, 3, 4, 4, 6]

new_numbers = []

for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
        
print(new_numbers)

print(numbers)

# numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)
