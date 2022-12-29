def missing_positive(nums):
    n=1
    s=set(nums)
    while n in s:
        n=n+1
    return n

print(missing_positive([1,5,3]))       