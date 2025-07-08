



def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0) #Create a new node with value 0
        root = head 
        carry = 0 
        while l1 or l2: #Run until both lists are 0
            
            v1 = l1.val if l1 else 0 #Get the value from the current node, if the list is empty, use 0
            v2 = l2.val if l2 else 0 #same for l2
            
            s = v1 + v2 + carry #Sum the both values and carry
            carry = s//10 #Update the carry with the tens digit
            
            head.next = ListNode(s%10) #taking the last digit of the sum (units digit)
            head = head.next 
            
            if l1: #if l1 is not empty, move to the next node
                l1 = l1.next 
            if l2:
                l2 = l2.next 
                
        if carry:
            head.next = ListNode(carry) #if there is a carry add it to the end of the list
            
        return root.next 