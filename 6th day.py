def find_zero_subarrays(arr):
    sum_dict = {}
    curr_sum = 0
    result = []

    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == 0:
            result.append((0, i))

        if curr_sum in sum_dict:
            for start_index in sum_dict[curr_sum]:
                result.append((start_index + 1, i))

        if curr_sum in sum_dict:
            sum_dict[curr_sum].append(i)
        else:
            sum_dict[curr_sum] = [i]

    return result


arr = [1, 2, -3, 3, -1, 2]
output = find_zero_subarrays(arr)
print(output)
