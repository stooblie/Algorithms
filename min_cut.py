import string
import random
import traceback
import re

handle = open('kargerMinCut.txt','r').readlines()
data = [x.replace('\r\n','') for x in handle]
data = [x.split('\t') for x in data]
dictionary = dict()
for x in data: 
    a=x[0]
    b=x[1:len(x)-1]
    dictionary[a] = b
    
smallest_cut = None
count = 0
    
def contraction(data, limit):
    global smallest_cut, count

    if len(data) == 2:
        count += 1
        
        print data
        
        min_cuts = len(data.values()[0])
        
        if smallest_cut is None:
            smallest_cut = min_cuts
        if min_cuts < smallest_cut:
            smallest_cut = min_cuts
        
        if count == limit:
            print 'The smallest cut is: ', smallest_cut
            exit()
        contraction(dictionary, limit)
        
    first = random.choice(data.keys())
    second = random.choice(data[first])
    
    print '=> First random key: ', first
    print '=> Second random key: ', second
    print 'Length of remaining nodes: ', len(data)
    
    second_key = None
    if any('-{}*'.format(second) in x for x in data.keys()):
        print 'Ajusting the second key.'
        key = [key for key in data.keys() if '-{}*'.format(second) in key]
        second_key = key[0]
    else:
        second_key = second
    print 'Adjusted second_key is: ', second_key
    
    if first == second_key: contraction(data, limit)       
    
    new_key = '-{}*-{}*'.format(first, second_key)
    data[new_key] = data[first]+data[second_key]
    
    lst_keys = re.split('([*-]*[-*]+)', new_key)
    lst_keys = filter(lambda x: x.isdigit(), lst_keys)
    #print 'This is the list of keys in the new entry: ', lst_keys
    
    for i in lst_keys:
        while i in data['-{}*-{}*'.format(first, second_key)]: data['-{}*-{}*'.format(first, second_key)].remove(i)
    
    #print 'Connections in merged nodes -{}*-{}*: '.format(first, second_key), data['-{}*-{}*'.format(first, second_key)]
    del data[first]
    del data[second_key]
    contraction(data,limit)
    
contraction(dictionary, 500)
        
        
    