def subarray_sum(nums, target):
    
    _hash = {}
    
    _hash[-1]=0
    running_sum = 0
    prev_numbers = 0

    '''for index, num in enumerate(nums):
        print(running_sum)
        running_sum += num 
        exceeding = running_sum - target

        if index == 0: 
            _first = num
        if running_sum == target:
            return [_hash[_first], index]
        
        if running_sum > target:
            if exceeding in _hash:
                return [_hash[exceeding+1], index]
            if exceeding in _hash and _hash[exceeding] == 0:
                return [_hash[exceeding+1], index]
            return []
        
        _hash[num] = index'''
    
    

    for index, num in enumerate(nums):
        running_sum += num
        if running_sum == target:
            return [0, index]
        
        if num == target:
            return [index, index]

        if running_sum > target:
            exceeding = running_sum - target
            if exceeding in _hash:
                return [_hash[exceeding]+1,index]
            return []

        _hash[running_sum] = index



nums = [1, 2, 3, 4, 5, 6]
target = 4
print ( subarray_sum(nums, target) )

''''
nums = [2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )



nums = []
target = 0
print ( subarray_sum(nums, target) )'''



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
