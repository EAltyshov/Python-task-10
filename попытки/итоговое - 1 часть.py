import collections

s1 = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя']
s2 = [item for item, count in collections.Counter(s1).items() if count > 1]
s3 = [x.lower() for x in s1]
s4 = [x.lower() for x in s2]
result=list(set(s3) ^ set(s4))

print(s2)

"""
def get_unique_name(s2):
    unique = []
    for name in s2:
        if name in unique:
            continue
        else:
            unique.append(name)
    return unique

print(get_unique_name(s2))

"""