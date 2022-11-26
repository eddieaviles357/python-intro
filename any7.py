def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    is_seven = False
    for num in nums:
        if num == 7:
            is_seven = True

    return is_seven


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
