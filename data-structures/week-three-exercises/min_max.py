def find_min_max(list_to_search):
    def inner_search(shortened_list, min, max):
        if shortened_list == []:
            return (min, max)
        elif shortened_list[0] > max:
            return inner_search(shortened_list[1:], min, shortened_list[0])
        elif shortened_list[0] < min:
            return inner_search(shortened_list[1:], shortened_list[0], max)
        else:
            return inner_search(shortened_list[1:], min, max)
    return inner_search(list_to_search[1:], list_to_search[0], list_to_search[0])

print(find_min_max([2,1,4,9,4.5]))