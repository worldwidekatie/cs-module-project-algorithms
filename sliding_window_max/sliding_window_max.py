'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    low = 0
    high = k
    output = []
    while high <= (len(nums)):
        output.append(max(nums[low:high]))
        # print(nums[low:high])
        low += 1
        high += 1
        # print("--------------")
        # print(low)
        # print(high)
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
    print(f"Should be {3, 3, -1, 5, 5, 6, 7}")