mylist = ["apple", "banana", "cherry","watermelon", "guava"]
tropical = ["mango", "pineapple", "papaya"]

def append_list(mylist):
    mylist.append("orange")
    print("append list\n")
    print(mylist)

def insert_to_list(mylist):
    mylist.insert(1,"orange")
    print("insert to list\n")
    print(mylist)

def extend_list(mylist, tropical):
    mylist.extend(tropical)
    print("extend list\n")
    print(mylist)

def remove_element(mylist):
    mylist.remove("cherry")
    print("remove list elements\n")
    print(mylist)

def pop_list(mylist,index):
    mylist.pop(index)
    print("pop list\n")
    print(mylist)

def clear_list(mylist):
    mylist.clear()
    print("clear list\n")
    print(mylist)

def sort_list(mylist):
    mylist.sort()
    print("sort list\n")
    print(mylist)

def copy_list(mylist):
    thislist = mylist.copy()
    print("copy list\n")
    print(thislist)

def list_method(mylist):
    thislist = list(mylist)
    print("copy using list method\n")
    print(thislist)

def count_list_items(mylist):
    occurence = mylist.count("apple")
    print("count list items\n")
    print(occurence)

def index_of_item(mylist):
    itm_index = mylist.index("watermelon")
    print("find index of first occurence of list item\n")
    print(itm_index)

def reverse_list(mylist):
    mylist.reverse()
    print("reverses the list\n")
    print(mylist)


append_list(mylist)
insert_to_list(mylist)
extend_list(mylist,tropical)
remove_element(mylist)
pop_list(mylist,1)
sort_list(mylist)
copy_list(mylist)
list_method(mylist)
count_list_items(mylist)
index_of_item(mylist)
reverse_list(mylist)