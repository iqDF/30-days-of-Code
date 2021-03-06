from sys import path
from os.path import dirname as dir
sys.path.append(dir(path[0]))

from utils.models import Node, LinkedList

class IterativeSolution:
    """
    Problem statement:
        Given (pointer/head of) a linked list, the task is to reverse the linked list.
        e.g: 1->2->3->4->NULL become 4->3->2->1->NULL  

    Approach: 
        1. Initialize three pointers prev as NULL, curr as head and next as NULL.
        2. Iterate trough the linked list. In loop, do following.
            1. Before changing next of current, store next node
                next = curr->next
            2. Now change next of current. This is where actual reversing happens
                curr->next = prev
            3. Move prev and curr one step forward
                prev = curr
                curr = next
    """
    def reverseList(self, A):
        """
        @param A : head node of linked list
        @return the head node in the linked list
        """
        prev, current = None, A
        while current.next:
            next = current.next
            current.next = prev
            prev, current = current, next
        
        current.next = prev
        return current



class RecursiveSolution:
    """
    Problem statement:
        Given (pointer/head of) a linked list, the task is to reverse the linked list.
        e.g: 1->2->3->4->NULL become 4->3->2->1->NULL  

    Approach: 
        1. Initialize three pointers prev as NULL, curr as head and next as NULL.
        2. Iterate trough the linked list. In loop, do following.
            1. Before changing next of current, store next node
                next = curr->next
            2. Now change next of current. This is where actual reversing happens
                curr->next = prev
            3. Move prev and curr one step forward
                prev = curr
                curr = next
    """

    def reverseList(self, A):
        """
        @param A: head node of linked list
        @return: the head node in the linked list
        """
        prev = None
        return self.reverse_recursive(A, prev)
    
    def reverse_recursive(self, current, prev):
        """ Recursive helper method

        @return: the head of reversed linked list
        """
        if not current:
            return prev
        head_reversed = self.reverse_recursive(current.next, prev)
        current.next = prev
        return head_reversed
