def modi(ls):
    target = (ls[0]).replace(' ', '', 1)
    friend = (ls[1]).replace(' ', '', 1)
    return target, friend

def modi2(ls):
    target = ls[0]
    friend = ls[1]
    ans = []
    for item in friend:
        ans.append(((target, item), friend))
    return ans


def modi3(ls):
    target1 = ls[0][0]
    target2 = ls[0][1]
    friend = ls[1]
    ans = []
    
    for item in friend:
        if (target1 == item) or (target2 == item):
            continue
        ans.append(item)
    
    return (target1, target2), ans
    
    

def common_friends(file_path):
    lines = sc.textFile(file_path)
    output1 = lines.map(lambda x: x.split('->'))
    output2 = output1.map(modi)
    
    output3 = output2.map(lambda x: (x[0], (x[1]).split(' ')))
    output4 = output3.flatMap(modi2)
    
    output5 = output4.map(modi3)
    output5 = output5.map(lambda x: (tuple(sorted(x[0])), sorted(x[1])))
    
    output6 = output5.reduceByKey(lambda x, y: x if len(x) < len(y) else y)
    return output6.collect()
    
common_friends("data/friends.txt")