// To Do 1

// Recursive Sigma

// Write a recursive function that given a number returns the sum of integers 
// from 1 to that number.
// Example: rSigma(5) = 15 (1+2+3+4+5); 
// rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.


function rSigma(num){
    if (num <= 0 ){
        return 0;
    }
    if (num == 1){
        return num;
    } else{
        return num + rSigma(num-1);
    }
  }

console.log(rSigma(5))

// Recursive Factorial
// Given num, return the product of ints from 1 up to num. If less than zero, 
// treat as zero. If not an integer, truncate. 
// Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). 
// Also, rFact(6.5) = 720 (1*2*3*4*5*6).


function rFact(num){
    if (num <= 0) {
        return 1;
    }
    else {
        return Math.floor(num) * rFact(Math.floor(num) - 1);
    }
}

console.log(rFact(3))
console.log(rFact(6.5))


///////////

// To Do 3
// Recursive Binary Search
// Given a sorted array and a value, recursively determine whether value is 
// found within array. 
// rBinarySearch([1,3,5,6],4) = false; 
// rBinarySearch([4,5,6,8,12],5) = true.

function rBinarySearch(arr, value) {
    var mid = Math.floor(arr.length/2)

    if(arr[mid] == value){
        return true;
    }
    else if(value < arr[mid] && arr.length > 1){ // if value is on the left side of arr
        return rBinarySearch(arr.slice(0, mid), value); //
    }
    else if(value > arr[mid] && arr.length > 1){ // if val on right side of arr
        return rBinarySearch(arr.slice(mid, arr.length), value);
    }
    else{
        return false;
    }
}

console.log(rBinarySearch([1, 3, 5, 6], 4));
console.log(rBinarySearch([4, 5, 6, 8, 12], 5));



// Greatest Common Factor
// Given two integers, create rGCF(num1,num2) to recursively determine the
// Greatest Common Factor (the largest integer dividing evenly into both). 
// Greek mathematician Euclid demonstrated these facts:
// gcf(a,b) == a, if a == b;
// gcf(a,b) == gcf(a-b,b), if a>b;
// gcf(a,b) == gcf(a,b-a), if b>a.

// Second: rework facts #2 and #3 to reduce stack consumption and expand 
// rGCF’s reach. You should  be able to compute rGCF(123456,987654).


function rGCF(num1, num2) {
    if (num1 == num2) {
        return num1;
    }
    if (num1 > num2) {
        return rGCF(num1-num2, num2);
    }
    if (num1 < num2) {
        return rGCF(num1, num2-num1);
    }
}

console.log(rGCF(3, 7));   
console.log(rGCF(18, 27)); 
console.log(rGCF(49, 14)); 
