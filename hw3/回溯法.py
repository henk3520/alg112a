def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def permute(arr, start, end):
    if start == end:
        print(''.join(arr))
    else:
        for i in range(start, end + 1):
            swap(arr, start, i)
            permute(arr, start + 1, end)
            swap(arr, start, i)

def all_permutations(s):
    n = len(s)
    arr = list(s)
    print("所有排列：")
    permute(arr, 0, n - 1)

input_string = "12345"
all_permutations(input_string)
//參考chatgpt並修改
