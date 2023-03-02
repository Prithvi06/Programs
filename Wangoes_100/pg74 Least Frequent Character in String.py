String="wangoes technology"
all_freq = {}
for i in String:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("minimum time character present in stirng=",min(all_freq,key=all_freq.get))
