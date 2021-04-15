import sys
list = [64, 25, 12, 22, 11]

# Loop through all list elements
for i in range(len(list)):

    # Find the minimum element in remaining list
    min_elem = i
    for j in range(i+1, len(list)):
        if list[min_elem] > list[j]:
            min_elem = j

    # Swap the minimum element with the first element
    list[i], list[min_elem] = list[min_elem], list[i]

print(list)
