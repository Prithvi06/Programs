String="wangoes technology"
all_freq = {}
for i in String:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("maximun time character present in stirng=",max(all_freq,key=all_freq.get))