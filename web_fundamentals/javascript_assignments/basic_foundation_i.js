// 1. Get 1-255:

function arrayOfNumbers(num1, num2){
    var arr = [];
    for(i=num1; i<=num2; i++){
        arr.push(i);
    }
    return arr;
}
console.log(arrayOfNumbers(1,255));


// 2. Get even 1000 

function getEvenSum(num1, num2){
    var sum = 0;
    for(var i=num1; i<=num2; i++){
        if(i % 2 == 0){
            sum = sum + i;
        }
    }
    return sum;
}
console.log(getEvenSum(1, 1000));


// 3. Sum odd 5000

function getOddSum(num1, num2){
    var sum = 0;
    for(var i=num1; i<=num2; i++){
        if(i % 2 != 0){
            sum = sum + i;
        }
    }
    return sum;
}
console.log(getOddSum(1, 5000));


// 4. Iterate an Array; 

function sumArray(arr){
    var sum = 0;
    for(i=0; i<arr.length; i++){
        sum = sum + arr[i];
    }
    return sum;
}
var testArr = [-5,2,5,12];
console.log(sumArray(testArr));


// 5. Find max

function findMax(arr){
    var max = arr[0];
    for(i=0; i<arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}
var testArr = [-3,3,5,7];
console.log(findMax(testArr));


// 6. Find average

function getAvg(arr){
    var sum = 0;
    for(i=0; i<arr.length; i++){
        sum = sum + arr[i];
    }
    var avg = (sum / arr.length);
    return avg;
}
var testArr = [1,3,5,7,20];
console.log(getAvg(testArr));


// 7. Array odd

function createOddArray(num1, num2){
    var newArr = [];
    for(i=num1; i<=num2; i++){
        if(i % 2 != 0){
            newArr.push(i);
        }
    }
    return newArr;
}
console.log(createOddArray(1, 50));


// 8. Greater than Y

function countGreaterThan(arr, y){
    var count = 0;
    for(i=0; i<arr.length; i++){
        if (arr[i]> y){
            count++
        }
    }
    return count;
}
var testArr = [1, 3, 5, 7];
console.log(countGreaterThan(testArr, 3));


// 9. Squares

function squares(arr){
    for(i=0; i<arr.length; i++){
        arr[i] = (arr[i] * arr[i]);
    }
    return arr;
}
var testArr = [1,5,10,-2];
console.log(squares(testArr));


// 10. Negatives

function swapNegatives(arr){
    for(i=0; i<arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0;
        }
    }
    return arr;
}
var testArr = [1,5,10,-2];
console.log(swapNegatives(testArr));


// 11. 

function arrMaxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = 0;
    for(i=0; i<arr.length; i++){
        sum = sum + arr[i];
        if(arr[i] < min){
            min = arr[i];
        }
        else if(arr[i] > max){
            max = arr[i];
        }
    }
    var avg = (sum / arr.length);
    var arrNew = [max, min, avg];
    return arrNew;
}
var testArr = [1,5,10,-2];
console.log(arrMaxMinAvg(testArr));


// 12. Swap values

function firstLastSwap(arr){
    var temp = arr[(arr.length-1)];
    arr[(arr.length-1)] = arr[0];
    arr[0] = temp;
    return arr;
}
var testArr = [1,5,10,-2];
console.log(firstLastSwap(testArr));


// 13. Number to String

function numToString(arr){
    for(i=0; i<arr.length; i++){
        if(arr[i]<0){
            arr[i] = 'Dojo';
        }
    }
    return arr;
}
var testArr = [-1,-3,2];
console.log(numToString(testArr));
