def find_duplicate(nums):
    """Faça o código aqui."""
    if not nums or not all(isinstance(num, int) and num >= 0 for num in nums):
        return False

    counts = {}
    for num in nums:
        if num in counts:
            return num
        counts[num] = 1
    return False
