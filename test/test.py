urls_set = []
urls_set.append('http://www.baidu.com')
urls_set.append('http://www.baidu.com')
urls_set.append('http://www.bidu.com')
urls_set.append('http://www.abc.com')
print(urls_set)
my_list = set(urls_set)
print(my_list)
my_list = sorted(set(urls_set), key=lambda x: urls_set.index(x))
print(my_list)