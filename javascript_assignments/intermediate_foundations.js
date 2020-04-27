// Part 1

//1. Sigma 
function sigma(num){
    var sum = 0;
    for (var i=1; i<=num; i++){
        sum = sum + i;
    }
    return sum;
}
console.log(sigma(3));
console.log(sigma(5));


//2. Factorial
function factorial(num){
    var product = 1;
    for(var i=1; i<=num; i++){
        product = product*i;
    }
    return product;
}
console.log(factorial(3));
console.log(factorial(5));


//3. Fibonacci
function fibonacci(n){
    fib = [0, 1];
    for(var i=2; i<=n; i++){
        fib.push(fib[i-1] + fib[i-2]);
    }
   // console.log(fib); // log to make sure its summing correctly
    return fib[n];
}
console.log(fibonacci(0));
console.log(fibonacci(1));
console.log(fibonacci(2));
console.log(fibonacci(3));
console.log(fibonacci(5));
console.log(fibonacci(10));


//4. Array: Second to Last
var arr = [42, true, 4, "Liam", 7];
var arrShort = ['we were expecting null'];
function secondToLast(arr){
    if(arr.length>=2){
        return arr[arr.length-2];
    }
    else{
        return null;
    }
}
console.log(secondToLast(arr));
console.log(secondToLast(arrShort));


//5. Array: Nth-to-Last
function nthToLast(arr, n){
    if(arr.length>=2){
        return arr[arr.length-n];
    }
    else{
        return null;
    }
}
console.log(nthToLast([5,2,3,6,4,9,7],3));
console.log(nthToLast([1],3));


//6. Array: Second-Largest
function secondLargest(arr){
    var max = arr[0];
    var secondmax = null;
    for (var i=0; i<arr.length; i++){
        if(arr[i]>max){
        secondmax = max;
        max = arr[i];
        }
        // console.log(arr[i]<max && arr[i]>secondmax)
        if(arr[i]<max && arr[i]>secondmax){
            secondmax = arr[i];
        }
    }
    return secondmax;
}
console.log(secondLargest([42]));
console.log(secondLargest([42,1,4,3.14,7]));
console.log(secondLargest([2,5,4,6,-1,12,11,15,4,8,15,16,23,42]));


// //7. Double Trouble
function dupInPlace(arr){
    for (var i=arr.length-1; i>=0; i--){

        // // method 1 resulting in array of arrays: [ [ 4, 4 ], [ 'Ulysses', 'Ulysses' ], [ 42, 42 ], [ false, false ] ]
        // arr[i] = [arr[i], arr[i]];

        // method 2 using splice():
        arr.splice(i, 0, arr[i]);
    }
    return arr;
}
console.log(dupInPlace([4, "Ulysses", 42, false]));


// Part 2. 

//1. Fibonacci with Recursion

function fib(n){ // where n is the index I'm seeking a value for
   if(n<2){
       return n;
   }
   return fib(n-1) + fib(n-2);
}
console.log(fib(10));

