// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. 
//Do this without using any built-in array methods.

function pushFront(arr, a){
    arr[arr.length] = arr[arr.length-1]
    for (var i = arr.length-1; i>0; i--){
        arr[i] = arr[i-1];
    }
    arr[0] = a;
    console.log(arr);
}

pushFront([1,2,3,4,5], 0)


// Pop Front
// Given an array, remove and return the value at the beginning of the array. 
// Do this without using any built-in array methods except pop().

function popFront(arr){
    var returnVal = arr[0]
    for (var i = 0; i <= arr.length-1; i++){
        arr[i] = arr[i+1];
    }
    arr.pop();
    console.log(arr);
    return returnVal;
}

popFront([-9,3,3,7,5])


// Insert At
// Given an array, index, and additional value, insert the value into array at given index. 
// Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent 
// to insertAt(arr,0,val).

function insertAt(arr, idx, val){
    arr[arr.length] = arr[arr.length-1]
    for (var i = arr.length-1; i > idx; i--){
        arr[i] = arr[i-1];
    }
    arr[idx] = val;
    console.log(arr);
}

insertAt([1, -2, 5, 7, 0], 2, 3)


// Remove At
// Given an array and an index into array, remove and return the array value at that index. 
// Do this without using built-in array methods except pop(). Think of popFront(arr) as 
// equivalent to removeAt(arr,0).

function removeAt(arr, idx){
    var returnVal = arr[idx];
    for (var i = idx; i <= arr.length-1; i++){
        arr[i] = arr[i+1];
    }
    arr.pop();
    console.log(arr);
    return returnVal;
}

removeAt([1, -2, 5, 7, 0], 3)

// Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, 
// do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, 
// change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, 
// do this without using any built-in array methods.

function swapPairs(arr){
    var i = 0;
    if (arr.length % 2 == 0){
        for (var i = 0; i < arr.length; i+=2){
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
    }
    else {
        for (var i = 0; i < arr.length-1; i+=2){
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
    }
    console.log(arr);
}

swapPairs([1, -2, 5, 7, 0])


// Remove Duplicates
// Sara is looking to hire an awesome web developer and has received applications from 
// various sources. Her assistant alphabetized them but noticed some duplicates. Given a 
// sorted array, remove duplicate values. Because array elements are already in order, all 
// duplicate values will be grouped together. As with all these array challenges, do this 
// without using any built-in array methods.

function removeDupes(arr){
    noDupes = []
    for (var i = 0; i < arr.length; i++){
        if (arr[i] != arr[i+1]){
            noDupes.push(arr[i])
        }
        else {
            continue;
        }
    }
    console.log(noDupes)
}

removeDupes(['a', 'a', 'b', 'c', 'c', 'd', 'd', 'e'])

// Second: Solve this without using any nested loops.



// Min to Front
// Given an array of comparable values, move the lowest element to array’s front,
// shifting backward any elements previously ahead of it. Do not otherwise change 
// the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. 
// As always, do this without using built-in functions.

function minToFront(arr){
    var min = arr[0];
    var minIdx = 0;
    for (var i=1; i<arr.length; i++){
        if (arr[i] < min){
            min = arr[i];
            minIdx = i;
        }
    }
    for (var x = minIdx; x > 0; x--){
        var temp = arr[x];
        arr[x] = arr[x-1];
        arr[x-1] = temp;
    }
    console.log(arr);
    return arr;
}

minToFront([4,2,1,3,5])