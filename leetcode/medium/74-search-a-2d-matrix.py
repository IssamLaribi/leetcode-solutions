class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            for element in row:
                arr.append(element)

        def binarySearch(nums: List[int], target: int) -> int:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                print(mid)
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            return False

        return binarySearch(arr, target)
            
