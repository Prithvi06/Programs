input = 'ant magenta magnate tan gnamate'
input = input.split(" ")

for i in range(0, len(input)):
    input[i] = ''.join(sorted(input[i]))

freqDict={}
for val in input:
    if val not in freqDict:
        freqDict[val]=1
    else:
        freqDict[val]+=1
print(freqDict)
print(max(freqDict.values()))

