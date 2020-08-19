'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    all = []
    dups = []
    for i in arr:
        if i not in all:
            all.append(i)
        else:
            dups.append(i)
    
    for i in arr:
        if i not in dups:
            return i


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")