def bubble_sort(list):
    n = len(list)

    # Loop through all list elements
    for i in range(n-1):
        # setting the range to n - 1 means the loop doesn't execute once more than it needs to

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater
            # than the next element
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(list)

print(list)
# for i in range(len(list)):
#     print("%d" % list[i]),
