class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        answer = 0

        for num in nums:
            current_sum += num

            need = current_sum - k

            if need in prefix_count:
                answer += prefix_count[need]

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return answer