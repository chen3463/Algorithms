/*
Description
Ugly number is a number that only have prime factors 2, 3 and 5.

Design an algorithm to find the Nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Note that 1 is typically treated as an ugly number.
*/


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, 1)
        num_set = set([1])

        for _ in range(n):
            curr_num = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_num = factor * curr_num
                if new_num not in num_set:
                    num_set.add(new_num)
                    heapq.heappush(heap, new_num)
        return curr_num
