def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    while True:
        sorted = True
        for i in range(n - 1):
            if list_to_sort[i] > list_to_sort[i + 1]:
                sorted = False
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
        if sorted:
            break
        n -= 1
    return list_to_sort


num_list = [7,2,97,32,6,1,5]

print(bubble_sort(num_list))