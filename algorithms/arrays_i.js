// ToDo1
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


//########################


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


//########################


// To Do 2
// Reverse
// Given a numerical array, reverse the order of values, in-place. The reversed array should have 
// the same length, with existing elements moved to other indices so that order of elements is reversed. 
// Working ‘in-place’ means that you cannot use a second array – move values within the array that you 
// are given. As always, do not use built-in array functions such as splice().

function reverseArray(arr){
    for (var i = 0; i < (arr.length-1)/2; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    console.log(arr);
}
reverseArray([4,2,1,3,5])


// Rotate
// Implement rotateArr(arr, shiftBy) that accepts array and offset. Shift arr’s 
// values to the right by that amount. ‘Wrap-around’ any values that shift off 
// array’s end to the other side, so that no data is lost. Operate in-place: 
// given ([1,2,3],1), change the array to [3,1,2]. Don’t use built-in functions.

function rotateArr(arr, shiftBy){
    while (shiftBy > 0){
        var temp = arr[arr.length-1]
        for (var i = arr.length-1; i>=0; i--){
            arr[i] = arr[i-1];
        }
        arr[0] = temp;  
        shiftBy--;     
    }
    console.log(arr)
}

rotateArr([1,2,3],1)

// Second: allow negative shiftBy (shift L, not R).

function rotateArr(arr, shiftBy){
    if (shiftBy > 0){
        while (shiftBy > 0){
            var temp = arr[arr.length-1]
            for (var i = arr.length-1; i>=0; i--){
                arr[i] = arr[i-1];
            }
            arr[0] = temp;  
            shiftBy--;     
        }
        console.log(arr)
        return arr;
    }
    else {
        while (shiftBy < 0){
            var temp = arr[0]
            for (var i = 0; i<arr.length; i++){
                arr[i] = arr[i+1];
            }
            arr[arr.length-1] = temp;  
            shiftBy++;     
        }
        console.log(arr)
        return arr;
    }
}

rotateArr([1,2,3],-1)


// Third: minimize memory usage. With no new array, handle arrays/shiftBys in the millions.

// Fourth: minimize the touches of each element.

function rotateArr(arr, shiftBy){
    if (arr.length-1 % shiftBy ==0){
        return arr;
    }
    else if (shiftBy > 0){
        while (shiftBy > 0){
            var temp = arr[arr.length-1]
            for (var i = arr.length-1; i>=0; i--){
                arr[i] = arr[i-1];
            }
            arr[0] = temp;  
            shiftBy--;     
        }
        console.log(arr)
        return arr;
    }
    else {
        while (shiftBy < 0){
            var temp = arr[0]
            for (var i = 0; i<arr.length; i++){
                arr[i] = arr[i+1];
            }
            arr[arr.length-1] = temp;  
            shiftBy++;     
        }
        console.log(arr)
        return arr;
    }
}

rotateArr([1,2,3,4,5,6],2)


// Filter Range
// Alan is good at breaking secret codes. One method is to eliminate values that 
// lie within a specific known range. Given arr and values min and max, retain 
// only the array values between min and max. Work in-place: return the array 
// you are given, with values in original order. No built-in array functions.


function filterRange(arr, min, max){
    var count = 0;
    var index = 0
    for (var i = 0; i <arr.length; i++ ){
        if(arr[i] >= min && arr[i] <= max){
            arr[index] = arr[i]  
            index++
            count++
        }  
    }
    count = arr.length-count
    for (i = 0; i <= count-1; i++){
        console.log(arr)
        arr.pop()
    }
    return arr
}
filterRange([3,7,-5,11,4,19,2,8],0,7)

// Concat
// Replicate JavaScript’s concat(). Create a standalone function that accepts 
// two arrays. Return a new array containing the first array’s elements,
// followed by the second array’s elements. Do not alter the original arrays. 
// Ex.: arrConcat( ['a','b'], [1,2] ) should return new array ['a','b',1,2].

function arrConcat(arr1, arr2){
    var newArr = [];
    for (var i = 0; i < arr1.length; i++){
        newArr.push(arr1[i]);
    }
    for (var j = 0; j < arr2.length; j++){
        newArr.push(arr2[j]);
    }
    console.log(arr1);
    console.log(arr2);
    console.log(newArr);
}

arrConcat(['a','b'],[1,2])