import re
import random

print('Random Talker Learning..')
with open('h_g_wells_time_machine.txt') as f:
    training_data = f.read()

training_data = training_data.replace('\n', '')
training_data = training_data.strip()
training_data = re.sub('[^a-zA-Z0-9 \n\.]', '', training_data)
training_data = re.sub('[\.\[..\]]', '. ', training_data)

words = training_data.split(' ')

memory = {}

for position in range(len(words)-2):
    key = words[position] + ' ' + words[position+1]
    if key in memory.keys():
        value = words[position + 2]
        if value is not None:
            memory[key] = list(set(memory[key] + [value]))
    else:
        value = words[position + 2]
        if value is not None:
            memory[key] = [value]

print(memory)
print('Random Talker Ready to play. (Type \'quit\' to end program)')

while True:
    starting_word = input('Type the starting word : ')
    if starting_word == 'quit':
        break

    learned_keys = list(memory.keys())
    random.shuffle(learned_keys)

    next_key = None
    end = False
    for full_key in learned_keys:
        if full_key.lower().startswith(starting_word.lower()):
            next_key = full_key

    if next_key is None:
        print('I do not know that word. Please give me a new word.')
        continue
    else:
        sentence = [starting_word]
        while not end:
            if len(sentence) > 100:
                end = True
            current_two_word = next_key.split(' ')
            sentence.append(current_two_word[1])
            if next_key in memory.keys():
                next_word = random.choice(memory[next_key])
                next_key = current_two_word[1] + ' ' + next_word
            else:
                end = True
    sentence = ' '.join(sentence)
    print('\n' + sentence + '\n')
    print()
