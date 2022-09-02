"""
# List comprehension
names = ['Josh', 'Josh Blumberg', 'Sally', 'Jane Doe']
full_names = []
for name in names:
    if ' ' in name:
        full_names.append(name)
print(full_names)

full_names = [name for name in full_names if ' ' in name]
"""
"""

sevens = []
all_numbers = range[1, 1001]
for num in all_numbers:
    if num % 7 == 0:
        sevens.append(num)

sevens = [num for num in all_numbers if num % 7 == 0]
print(sevens)
"""
"""

threes = []
all_numbers = range[1, 1001]
for num in all_numbers:
    if '3' in all_numbers:
        threes.append(num)

threes = [num for num in all_numbers if '3' in all_numbers]
print(threes)
"""
"""
sentence = 'The boy kicked the ball to the other side'
words = sentence.split()
lengths = {}
for word in words:
    lengths[word] = len(word)
    print(lengths)
lengths = {word : len(word) for word in words}
"""
