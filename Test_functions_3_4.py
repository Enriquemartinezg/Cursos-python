#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst
#Uncomment the line below when your function is done
print(append_size([23, 42, 108, 104]))

########################

#Write your function here
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

########################

#Write your function here
def larger_list(lst1, lst2):
  if (len(lst1) > len(lst2)):
    return lst1[-1]
  elif (len(lst2) > len(lst1)):
    return lst2[-1]
  return lst1[-1]
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 6]))

########################

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False
#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1], 2, 3))

########################

#Write your function here
def combine_sort(lst1, lst2):
  unsorted_list = lst1 + lst2
  sorted_list = sorted(unsorted_list)
  return sorted_list
#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

########################

#Write your function here
def every_three_nums(start):
  if start <= 100:
    return list(range(start,101,3))
  else:
    return []
#Uncomment the line below when your function is done
print(every_three_nums(100))

########################

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
#Elimina los elementos de indices entre start y end

#Uncomment the line below when your function is done
#print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))