definition for a singly-linked list
class ListNode:
	def__init__(slf,val=0,next=None):
		self.val = val
		self.next = next

class Solution:
	def getDecimalValue(self,head:ListNode) -> int:
		count =0
		nnode = head.next
		if head.val is not None:
			while (nnode):
				count+=1
				nnode = nnode.next
			nnode = head.next
			umm  =head.val * pow(2,count)
			while (nnode):
				count = count-1
				cumm = summ + (nnode.val *(pow(2,count)))
				nnode =  nnode.next
			return summ