# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = int("".join(str(n) for n in l1[::-1]))
        l2 = int("".join(str(n) for n in l2[::-1]))
        return [int(x) for x in str(l1 + l2)][::-1]


if __name__ == '__main__':
    a = Solution()
    print(a.addTwoNumbers([0], [0]))

        