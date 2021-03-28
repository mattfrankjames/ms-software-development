def list_reverse(list):
  # Base case
  if len(list) == 0 or len(list) == 1: # If the array is empty, or only has one item, return it unchanged
    return list
 
  # Recursive case
  return [array[len(list) - 1]] + list_reverse(list[:len(list) - 1])
  # First element of the return is the last element of the list
  # Second element of the return calls the list_reverse function again with the last element removed and will run until all list items have been iterated over

# Driver Code
array = [1, 2, 3, 4, 9,0,7,6]
print(list_reverse(array))