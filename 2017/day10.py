from functools import reduce

def wrap(nums, cur, l):
    nums = tuple(nums[cur:]) + tuple(nums[:cur]) # rotate
    nums = tuple(reversed(nums[:l])) + nums[l:] # reverse first part
    return nums[len(nums)-cur:] + nums[:len(nums)-cur] # rotate back

def knot(nums, lengths, cur=0, skip=0):
    for l in lengths:
        nums = wrap(nums, cur, l)
        cur = (cur + l + skip) % len(nums)
        skip += 1
    return nums, cur, skip

def compress(nums):
    blocks = (nums[i:i+16] for i in range(0,len(nums),16))
    dense = (reduce(lambda x,y: x^y, block, 0) for block in blocks)
    return ''.join(format(r,'02x') for r in dense)

def hash(s=''):
    lens = tuple(map(ord, s)) + (17,31,73,47,23)
    nums = range(256)
    cur = skip = 0
    for _ in range(64):
        nums, cur, skip = knot(nums, lens, cur, skip)
    return compress(nums)

if __name__ == '__main__':
    from aocd import data
    nums, *_ = knot(range(256), map(int, data.split(',')))
    print('part 1:', nums[0]*nums[1])
    print('part 2:', hash(data))
