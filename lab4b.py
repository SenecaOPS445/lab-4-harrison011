#!/usr/bin/env python3

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from 
    # both l1 and l2

    lt1 = set(l1)
    lt2 = set(l2)
    l3 = lt1.union(lt2)
    return list(l3)


def match_lists(l1, l2):
    # match_lists will return a list that contains all values found 
    # in both l1 and l2
    l3 = []
    for item1 in l1:
        for item2 in l2:
            if item1 == item2:
                l3.append(item1)
    return l3

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different 
    # values, which are not shared between the lists
    l3 = join_lists(l1,l2)
    l4 = match_lists(l1,l2)
    l5 = []
    for item3 in l3:
        if item3 not in l4:
            l5.append(item3)
    return l5    

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))