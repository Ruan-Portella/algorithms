def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 0:
        return False
    num_set = set()
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if num in num_set:
            return num
        num_set.add(num)
    return False
