// To Do 1
// Let’s build a basic Binary Search Tree. These challenges start with the 
// following reference definitions:

function BTNode(value) {
    this.val = value;
    this.left = null;
    this.right = null;
}
function BST() {
    this.root = null;
    // add methods here...

    // BST: Add
    // Create an add(val) method on the BST object to add new value to the tree. 
    // This entails creating a BTNode with this value and connecting it at the 
    // appropriate place in the tree. Unless specified otherwise, BSTs can contain 
    // duplicate values.

    add(val){
        if(this.root) {  // if tree not empty
            var runner = this.root;
            while(runner) {
                if(val > runner.val) { // if val greater than root, go right
                    if(runner.right){
                        runner = runner.right;
                    } 
                    else { // if no existing right node, put new node here
                        runner.right = new Node(val);
                        return this
                    }
                } 
                else { // if val less than root, go left
                    if(runner.left){
                        runner = runner.left;
                    } 
                    else { // if not left node, put new node here
                        runner.left = new Node(val);
                        return this
                    }
                }
            }
        }
        this.root = new Node(val);
        return this
    }

    // BST: Contains
    // Create a contains(val) method on BST that returns whether the tree contains 
    // a given value. Take advantage of the BST structure to make this a much more 
    // rapid operation than SList.contains() would be.

    function contains(val){
        var runner = this.root;
            while (runner) {
                if (val == runner.val) {
                    return true;
                }
                if (val < runner.val) {
                    if (!runner.left) { // if no left node, val is not in the tree
                        return false;
                    }
                    runner = runner.left; // move left
                } else {
                    if (!runner.right) { // if no right node, val is not in the tree
                        return false;
                    }
                    runner = runner.right; // move right
                }
            }
            return false;
        }


    // BST: Min
    // Create a min() method on the BST class that returns the smallest value found in the BST.

    function min(){
        var runner = this.root;
        var min = this.root.value;
        while(runner.left) { // move left as left has lower vals
            if(runner.left.value < min) {
                min = runner.left.value;
            }
            runner = runner.left;
        }
        return min
    }

    // BST: Max
    // Create a max() BST method that returns the largest value contained in the binary search tree.

    function max(){
        var runner = this.root;
        var max = this.root.value;
        while(runner.right) { // move right as right has higher vals
            if(runner.right.value > max) {
                max = runner.right.value;
            }
            runner = runner.right;
        }
        return max
    }

    // BST: Size
    // Write a size() method that returns the number of nodes (values) contained in the tree.

    function size() {
        if (this.root === null) { // if empty, return 0
            return 0;
        }
        function sizeHelper(runner) { // if empty return 0
            if (!runner) {
                return 0;
            }
            // if not empty, node 1 makes count 1, then add a count for each successive node to left and right
            return 1 + sizeHelper(runner.left) + sizeHelper(runner.right);
        }
        return sizeHelper(this.root); // make chainable
    }

    
    // BST: Is Empty
    // Create an isEmpty() method to return whether the BST is empty (whether it contains no values).

    function isEmpty() {
        if(this.root) {
            return false
        }
        return true
    }

}


