input = ['cat', 'dog', 'tac', 'god', 'act']
dict = {}

for strVal in input:

    key = ''.join(sorted(strVal))
    print(key)
    if key in dict.keys():
        dict[key].append(strVal)
    else:
        dict[key] = []
        dict[key].append(strVal)

output = ""
for key, value in dict.items():
    print(' '.join(value))
    output = output + ' '.join(value) +' '

print(output)
