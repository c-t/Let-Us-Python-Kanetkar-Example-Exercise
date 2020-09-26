def create_sent1(sub, ver, obj):
    lst = []
    for i in range(len(sub)):
        for j in range(len(ver)):
            for k in range(len(obj)):
                sent = sub[i] + ' ' + ver[j] + ' ' + obj[k]
                lst.append(sent)
    return lst

def create_sent2(sub, ver, obj):
    return [(s + ' ' + v + ' ' + o) for s in sub for v in ver for o in obj]

subjects = ['He', 'She']
verbs = ['loves', 'hates']
objects = ['TV serials', 'Netflix']

lst1 = create_sent1(subjects, verbs, objects)
for l in lst1:
    print(l)

print()
lst2 = create_sent2(subjects, verbs, objects)
for l in lst2:
    print(l)