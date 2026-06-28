import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        ans = []
        for num in nums:
            if num not in freq:
                freq[num] = 0
            else:
                freq[num] += 1
        heap = [(f, n) for n,f in freq.items()]
        heapq.heapify(heap)

        ans = [val[1] for val in heapq.nlargest(k, heap)]
        return ans