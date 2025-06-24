#O(1) - константа

# def fimt_element(arr,elem):
#     for i in arr:
#         if i == elem:
#             return i
#     return print('Нету')


#O(long n)

def binare_search(arr,targer):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == targer:
            return print(mid)
        elif arr[mid] < targer:
            left = mid + 1
        else:
            right = mid - 1
    return print('Нету')

my_arr = [1,2,3,4,5]
binare_search(my_arr,3)