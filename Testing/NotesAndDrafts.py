# creating input array
arr = np.ndarray(shape = (9,9), dtype=int)
arr = arr * 0; # set to zero

# creating a 9 by 9 array which contains list with possibilities for each position
arr = np.ndarray(shape = (9,9), dtype=np.ndarray)

# adding a posibility
arr[0,0,0].append(4)

# removing a possibility from a position
arr[0,0,0].remove(4)

# error catching if removing a possibility was never there:
try:
    arr.remove(10)
except ValueError:
    pass  # do nothing!
