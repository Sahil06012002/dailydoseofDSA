function lenOfCycle(head){
    slow = head
    fast = head
    let cycleExists = false
    while(fast != null && fast.next != null){
        slow = slow.next
        fast = fast.next.next
        if (slow == fast){
            cycleExists = true
            break
        }
    }
    counter = 1
    if(cycleExists){
        slow = slow.next
        while(slow != fast){
            slow = slow.next 
            counter += 1
        }
    }

}