from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Map each value to the index where it was seen; for every number,
    # check whether its complement has already been seen. O(n) time.
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(twoSum([3, 2, 4], 6))       # [1, 2]
    print(twoSum([3, 3], 6))          # [0, 1]
