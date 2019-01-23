def array_count9(nums):
    count = 0
    for item in nums:
        if item == 9:
            count = count + 1
    return count


def first_last6(nums):
    return nums[-1] == 6 or nums[0] == 6


def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


def make_pi():
    return [3, 1, 4]


def common_end(a, b):
    return a[-1] == b[-1] or a[0] == b[0]


def sum3(nums):
    return sum(nums)


def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


def reverse3(nums):
    return [nums[2], nums[1], nums[0]]


def max_end3(nums):
    if nums[0] > nums[2]:
        return [nums[0], nums[0], nums[0]]
    return [nums[2], nums[2], nums[2]]


def sum2(nums):
    return sum(nums[:2])


def middle_way(a, b):
    return [a[1], b[1]]


def make_ends(nums):
    return [nums[0], nums[-1]]


def has23(nums):
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3


def count_evens(nums):
    num = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            num = num + 1
    return num


def big_diff(nums):
    largest = 0
    for i in range(len(nums)):
        largest = max(largest, nums[i])
    smallest = largest
    for i in range(len(nums)):
        smallest = min(smallest, nums[i])
    return largest - smallest


def centered_average(nums):
    return (sum(nums)-max(nums)-min(nums))/(len(nums)-2)


def has22(nums):
    twos = 0
    for i in range(len(nums)):
        if nums[i] == 2:
            twos = twos + 1
        else:
            twos = 0
        if twos == 2:
            return True
    return False
