import datetime
import traceback
n = 100000

handle = open('IntegerArray.txt', 'r').readlines()
handle = [int(x) for x in handle]
q = handle[:(n/2)]
r = handle[(n/2):]

q_inversions = 0
print datetime.datetime.now()
for i in q:
    for number in q[(q.index(i)+1):]:
        if i > number:
            q_inversions += 1
print q_inversions

r_inversions = 0
for i in r:
    for number in r[(r.index(i)+1):]:
        if i > number:
            r_inversions += 1
print r_inversions

q_sorted = sorted(q)
r_sorted = sorted(r)
array = []
split_inversions = 0

i = 0
j = 0
for x in range(0,n):
    try:
        if q_sorted[i] < r_sorted[j]:
            array.append(q_sorted[i])
            i += 1
        elif q_sorted[i] > r_sorted[j]:
            array.append(r_sorted[j])
            j += 1
            split_inversions += len(q_sorted[i:])
        elif q_sorted[i] == r_sorted[j]:
            array.append([q_sorted(i), r_sorted[i]])
            i += 1
            j += 1
    except:
        traceback.print_exc()
        print i, j
print split_inversions
print "Sum equals" (split_inversions+q_inversions+r_inversions)
print datetime.datetime.now()    


    