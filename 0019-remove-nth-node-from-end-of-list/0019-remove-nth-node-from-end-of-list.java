/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode temp = head;
       int count = 0;
       if(head == null || head.next ==null){
        return null;
       } 
       while(temp!=null){
        temp = temp.next;
        count++;
       }
       if(count ==n){
        return head.next;
       }
       int i =1;
       temp = head;
       while (i<count-n){
        temp =temp.next;
        i++;
       }
       if(temp.next!=null){
        temp.next=temp.next.next;
       }
       return head;
    }
}