// 1. Biggie Size:

function biggieSize(arr){
    for(i=0; i<=arr.length; i++){
        if (arr[i] > 0){
            arr[i]='big';
        }
    }
    return arr;
}

console.log(biggieSize([-1,3,5,-5]))


// 2. Print Low, Return High

function lowHigh(arr){
    var low = arr[0];
    var high = arr[0];

    for(i=0; i<arr.length; i++){
        if(arr[i] > high){
            high = arr[i];
        }
        else if(arr[i] < low){
            low = arr[i];
        }
    }
    console.log(low); 
    return high;
}

console.log(lowHigh([-1,3,5,-5]))


// 3. Print One, Return Another

function printAndReturn(arr){
    console.log(arr[(arr.length - 2)]);
    for(i=0; i<arr.length; i++){
        if(arr[i] % 2 !=0){
            return arr[i];
        }
    }
}

console.log(printAndReturn([2,3,5,-5]))


// 4. Double Vision

function double(arr){
    var newArr = [];

    for(i=0; i<arr.length; i++){
        newArr.push(arr[i]*2);
    }
    return newArr;
}

console.log(double([1,2,3]))


// 5. Count Positives

function countPositives(arr){
    var count = 0;

    for(i=0; i<arr.length; i++){
        if(arr[i]>0){
            count++;
        }
    }
    arr[(arr.length-1)] = count;
    return arr;
}

console.log(countPositives([-1,1,1,1]))


// 6. Evens and Odds

function evensOdds(arr){
    var countEven = 0;
    var countOdd = 0;
    var newArr =[];

    for(i=0; i<arr.length; i++){
        if(arr[i] % 2 == 0){
            newArr.push(arr[i]);
            countOdd = 0;
            countEven ++;
            if(countEven == 3){
                newArr.push("Even more so!");
            }
        }
        else{
            newArr.push(arr[i]);
            console.log
            countEven = 0;
            countOdd ++;
            if(countOdd == 3){
                newArr.push("That's odd!")
            }
        }
    }
    return newArr;
}

console.log(evensOdds([2,-1,3,5,6,8,3,2,4,6,1]))


// 7. Increment the Seconds

function incrementOddIndices(arr){
    for (i=0; i<arr.length; i++){
        if(i % 2 != 0){
            arr[i] = arr[i] + 1;
        }
        console.log(arr[i]);
    }
    return arr;
}

console.log(incrementOddIndices([-1,1,1,3]))


// 8. Previous Lengths

function previousLengths(arr){
    for(i=arr.length-1; i>0; i--){
        arr[i] = arr[i-1].length;
    }
    return arr;
}

console.log(previousLengths(["hello", "dojo", "awesome"]))


// 9. Add Seven

function addSeven(arr){
    newArr = [];

    for(var i=0; i<arr.length; i++){
        newArr.push(arr[i]+7);
    }
    return newArr;
}

console.log(addSeven([1,2,3]))


// 10. Reverse Array

function reverse(arr){
    var temp = [];

    for (var i = 0; i<arr.length/2; i++){
        temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    return arr;
}

console.log(reverse([3,1,6,4,2]))


// 11. Outlook: Negative

function allNegative(arr){
    var newArr = [];

    for (var i=0; i<arr.length; i++){
        if(arr[i] <= 0){
            newArr.push(arr[i]);
        }
        else{
            newArr.push(arr[i]*(-1));
        }
    }
    return newArr;
}

console.log(allNegative([1,-3,5]))


// 12. Always Hungry

function alwaysHungry(arr){
    var wasFed = false;

    for(var i=0; i<arr.length; i++){
        if(arr[i] == 'food'){
            console.log("yummy");
            wasFed = true;
        }    
    }
    if(wasFed == false){
        console.log("I'm hungry");
    }
    return wasFed;
}

console.log(alwaysHungry(['notfood', 'food', 'food']))
console.log(alwaysHungry(['notfood', 'notfood', 'notfood']))


// 13. Swap Towards the Center

function swapTowardCenter(arr){
    var temp = [];

    for(var i=0; i<arr.length/2; i+=2){
        temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    // return arr;
}

console.log(swapTowardCenter([1,2,3,4,5,6]))


// 14. Scale the Array

function scaleArray(arr, factor){

    for(var i=0; i<arr.length; i++){
        arr[i] = arr[i]*factor;
    }
    return arr;
}

console.log(scaleArray([1,2,3], 3))
