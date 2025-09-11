class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            print(count[num])

        sorted_count = dict(sorted(count.items(), key=lambda item : item[1], reverse = True))

        res = list(sorted_count.keys())

        for _ in range(len(res) - k):
            res.pop()

        return res        

# More efficient way:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        for _ in range(k):
            res.append(arr.pop()[1])

        return res        
