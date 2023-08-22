def merge(dic1 , dic2):
    dic3 = {**dic1,**dic2}
    return dic3
dic1 = {'a': 'xie', 'b': 'jun', 'c': 'hui', 'd': 'shi', 'e': 'god'}
dic2 = {'a': 'xie', 'f': 'fam', 'g': 'asd', 'h': 'ptsd', 'e': 'god'}
dic3 = merge(dic1, dic2)
print(dic3)