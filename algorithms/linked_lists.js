// FRONTS - Singly Linked Lists

// Add Front
// Write a method that accepts a value and create a new node, assign it to 
// the list head, and return a pointer to the new head node.

// Remove Front
// Write a method to remove the head node and return the new list head node. 
// If the list is empty, return null.

// Front
// Write a method to return the value (not the node) at the head of the list. 
// If the list is empty, return null.

// Contains
// Sam thinks Tad might be somewhere in a very long line waiting to attend 
// the Superman movie. Given a ListNode pointer and a val, return whether val 
// is found in any node in the list.


// node class:
class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

// singly linked list class
class SLL{
    // constructor accepts value to create head node
    constructor(value){
        this.head = null;
    }

    addFront(value) {
        if (this.head == null){  // if list is empty
            this.head = new Node(value);
            return this        
        }
        else { // if list has a head
            var prevHead = this.head;  // store the current head
            this.head = new Node(value);  //create new head
            this.head.next = prevHead; //link prev head
            return this
        }    
    }

    removeFront(){
        if (this.head == null){ // if list is empty
            return this
        }
        else {
        this.head = this.head.next; 
        return this
        }
    }

    front(){
        return this.head.value;
    }

    contains(value){
        var runner = this.head;
        while(runner){
            if (runner.value == value){
                return true;  //if match, return true
            }
            runner = runner.next; // increment the runner
        } 
        return this
    }


//Length
// July 20, 2013: about 5000 people wait in line for a chance to audition 
// for American Idol. Create a function that accepts a pointer to the first 
// list node, and returns number of nodes in that SList.
    
    length(){
        var runner = this.head;
        var count = 0;
        while (runner) {
            count +=1;
            runner = runner.next
        }
        return count;
    }


// Display
//Create display(node) for debugging that returns a string containing all list 
// values. Build what you wish console.log(myList) did!

    display(){
        var runner = this.head;
        var nodeCount = 0;
        while (runner){
            console.log('Node:', nodeCount, 'Value:', runner.value);
            nodeCount += 1;
            runner = runner.next;
        }
        return this;
    }

// Max/Min/Average
// SList: Max
// Create function max(node) to return list’s largest val.

    max(){
        var runner = this.head;
        var max = this.head.value;
        while (runner){
            if (runner.value > max){
                max = runner.value;
                console.log(max)
            }
            runner = runner.next;
        }
        console.log('Max =', max);
        return max;
    }


// SList: Min
// Create min(node) to return list’s smallest val.

    min(){
        var runner = this.head;
        var min = this.head.value;
        while (runner){
            if (runner.value < min){
                min = runner.value;
            }
            runner = runner.next;
        }
        console.log('Min =', min);
        return min;
}


// SList: Average
// Create average(node) to return average val.   

    average(){
        var runner = this.head;
        var sum = 0;
        while (runner) {
            sum += runner.value;
            runner = runner.next;
        }
        var avg = sum/this.length();
        console.log(sum, avg);
        return avg;
    }


// Back/Remove/Add
// SList: Back
// Create a function that accepts a ListNode pointer and returns the last value in the list.

    back(){
        var runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        console.log(runner.value);
        return runner.value;
    }


// SList: Remove Back
// Create a standalone function that removes the last ListNode in the list and returns the new list.

    removeBack(){
        var runner = this.head;
        while(runner.next.next) {
            runner = runner.next;
        }
        runner.next = null;
        this.display();
        return this;
    }

// SList: Add Back
// Create a function that creates a ListNode with given value and inserts it at end of a linked list.    

    addBack(value){
        var runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = new Node(value);
        this.display();
        return this;
    }

//////////////////////

// SList: Second to Last Value
// Create a standalone function that, given a pointer to the first node in a 
// singly linked list, will return the second-to-last value in that list. 
// What will you return if the list is not long enough?

    secondLast(){
        var runner = this.head;
        if (this.head == null || this.head.next == null){
            var message = 'This list is less than 2 nodes long.';
            console.log(message)
            return message;
        }
        else {
            while (runner.next.next){
                runner = runner.next;
            }
            console.log(runner.value);
            return runner.value;
        }
    }



// SList: Delete Given Node
// Create ListNode method removeSelf() to disconnect (remove) itself from 
// linked lists that include it. Note: the node might be the first in a list 
// (it won’t be the last), and you do NOT have a pointer to the previous node. 
// Also, don’t lose any subsequent nodes pointed to by .next.

    removeSelf(node){
// if node first val:
        if (this.head == null){
            return this
        }
        else if (node == this.head){
            this.removeFront();
        }
        else {
            while (runner.next) {
                if (node == runner)
            }
        }

// if node last value
removeBack(){
    var runner = this.head;
    while(runner.next.next) {
        runner = runner.next;
    }
    runner.next = null;
    this.display();
    return this;
}

    }




// SList: Copy
// Given a pointer to a singly linked list, return a copy of that list. Do not 
// return the same list, but instead make a copy of each node in the list and 
// connect them in the same order as the original.



// SList: Filter
// Given a headNode, a lowVal and a highVal, remove from the list any nodes that 
// have values less than lowVal or higher than highVal. Return the new list.






}   

var my_list = new SLL();

my_list.addFront(7).addFront(3).addFront(-28).addFront(11).addFront(63).removeFront().front()
console.log(my_list)
my_list.contains(3)
my_list.display()
my_list.max()
my_list.min()
my_list.average()
my_list.back()
my_list.removeBack().addBack(18)
my_list.secondLast()

var new_list = new SLL();
new_list.secondLast()
