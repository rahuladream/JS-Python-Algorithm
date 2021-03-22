class Solution:
    def addTwoNumbers(self, l1, l2):
        
        num1 = self.reverse(l1)
        # Reverse first array
        num2 = self.reverse(l2)
        # Reverse second array

        totalNum = str(num1 + num2)
        res = None
        for char in totalNum:
            res = ListNode(val = int(char), next=res)
        return res

    
    def reverse(self, l):

        num = ""
        prev = None
        while l:
            num += str(l.val)
            next = l.next
            l.next = prev
            prev = l
            l = next
        return int(num[::-1])
        
