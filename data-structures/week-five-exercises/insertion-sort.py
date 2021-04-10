def insertion_sort(list):

    # loop through list from 1 to len(list)
    for i in range(1, len(list)):

        key = list[i]

        # Check if current element is greater then the key, move to one position ahead of their current position if so
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key


list = [12, 11, 13, 5, 6]
insertion_sort(list)
print(list)
