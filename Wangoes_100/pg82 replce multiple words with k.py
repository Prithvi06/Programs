test_str = 'wangoes technology  is best for  and webdevelopment ERP'
word_list = ["best", 'ERP', 'for']

repl_wrd = 'wangoes'

res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])
print("String after multiple replace : " + str(res))