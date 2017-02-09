package ReverseSecondHalfofLinkedList;

/**
 * Created by tom on 2/8/17.
 */

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
 }

public class Solution {
    public static ListNode reverseSecondHalfList(ListNode head){
        if (head == null || head.next == null){return head;}

        ListNode fast = head;
        ListNode slow = head;

        while (fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        System.out.println("live");
        ListNode pre = slow.next;
        ListNode mid = pre.next;
        ListNode aft = null;


        while (mid != null && mid.next != null){
            //System.out.println(pre.val);
            aft = mid.next;
            mid.next = pre;

            pre = mid;
            mid = aft;
        }

        System.out.println("live");

        mid.next = pre;

        slow.next.next = null;
        slow.next = mid;

        return head;
    }

    public static void main(String[] args){
        ListNode listnode1 = new ListNode(1);
        ListNode listnode2 = new ListNode(2);
        ListNode listnode3 = new ListNode(3);
        ListNode listnode4 = new ListNode(4);
        ListNode listnode5 = new ListNode(5);
        ListNode listnode6 = new ListNode(6);
        ListNode listnode7 = new ListNode(7);
        ListNode listnode8 = new ListNode(8);
        ListNode listnode9 = new ListNode(9);
        ListNode listnode10 = new ListNode(10);

        listnode1.next = listnode2;
        listnode2.next = listnode3;
        listnode3.next = listnode4;
        listnode4.next = listnode5;
        listnode5.next = listnode6;
        listnode6.next = listnode7;
        listnode7.next = listnode8;
        listnode8.next = listnode9;
        //listnode9.next = listnode10;


        Solution newclass = new Solution();
        newclass.reverseSecondHalfList(listnode1);

        ListNode p = listnode1;
        while (p != null){
            System.out.println(p.val);
            p = p.next;
        }
    }
}
