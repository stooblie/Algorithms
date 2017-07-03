comparisons = 0

def choose_pivot(A, n):
    first = A[0]
    last = A[n-1]
    if (n % 2) == 0:
        middle = A[(n/2)-1]
    else:
        middle = A[(n/2)-(1/2)]
        
    lst = sorted([first, middle, last])
    return lst[1]

def partition(A, l, r):
    p = choose_pivot(A,r)
    p_index = A.index(p)
    
    temp = A[p_index]
    A[p_index] = A[l]
    A[l] = temp
    
    i = l + 1
    for j in range(i,r):
        if A[j] > p:
            continue
        elif A[j] < p:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i += 1
            
    temp = A[i-1]
    A[i-1] = A[l]
    A[l] = temp
    pos = A.index(p)
    print pos
    print A[:10]
    print A[(r-10):]
    return pos, A
            
def quicksort(A, n):
    global comparisons
    if n <= 1: return
    
    l = 0
    r = n
    comparisons += (n-1)
    pos, new_array = partition(A, l, r)
    quicksort(new_array[:pos], len(new_array[:pos]))
    quicksort(new_array[(pos+1):], len(new_array[(pos+1):]))

handle = open('QuickSort.txt', 'r').readlines()
handle = [int(x) for x in handle]
n = len(handle)

quicksort(handle, n)
print comparisons

