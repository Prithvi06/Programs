test_str = 'wangoes is best . wangoes also provide training now training help understand better '
# initializing replace mapping
repl_dict = {'wangoes': 'It', 'training': 'They'}
test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)
print(res)