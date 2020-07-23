// Fronts

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
            return this;            
        }
        else { // if list has a head
            var prevHead = this.head;
            this.head = new Node(value);
            this.head.next = prevHead;
            return this;
        }    
    }

    removeFront(){
        if (this.head == null){
            return this;
        }
        else {
        this.head = this.head.next;
        return this;
        }
    }

    front(){
        if (this.head == null){
            console.log(this.head.value)
            return this.head.value;
        }
    }
}



var my_list = new SLL();
my_list.addFront(7).addFront(3)
my_list.removeFront().removeFront().removeFront()
my_list.front()
console.log(my_list)

// Add Front
// Write a method that accepts a value and create a new node, assign it to 
// the list head, and return a pointer to the new head node.

// Remove Front
// Write a method to remove the head node and return the new list head node. 
// If the list is empty, return null.

// Front
// Write a method to return the value (not the node) at the head of the list. 
// If the list is empty, return null.