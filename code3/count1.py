fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
res = list()
counts = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.strip()
        words = line.split(' ')
        domain = words[1].split('@')
        res.append(domain[1])
        #print(domain[1])
    for word in res:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
