/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let temp = head
    let slow = head 
    let fast = head

    while(fast != null && fast.next != null){
        slow = slow.next
        fast = fast.next.next
        if(slow == fast){
            while(temp != slow){
                temp = temp.next
                slow = slow.next
            }
            return temp
        }

    }
    return null
    
};

function splitNumber(n){
    let arr = []
    while(n != 0){
        arr.push(n % 10)
        n = Math.floor(n/10)
    }
    arr.reverse()
    console.log(arr)
}

splitNumber(123)
