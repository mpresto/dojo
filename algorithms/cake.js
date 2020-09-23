// ReverseWords

function reverseWords(message) {

    // Decode the message by reversing the words
    
    // reverse entire array
    reverse(message, 0, message.length-1);

    let startidx = 0;
    for (let i=0; i<=message.length; i++){
        if (i === message.length || message[i] === ' '){
            reverse(message, startidx, i-1);
            startidx = i+1;
        }
    }

  }

function reverse(arr, start, end) {
    while (start < end) {
        let temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
  }



reverseWords([ 'c', 'a', 'k', 'e', ' ',
'p', 'o', 'u', 'n', 'd', ' ',
's', 't', 'e', 'a', 'l' ])




// 

function mergeArrays(myArray, alicesArray) {

    // Combine the sorted arrays into one large sorted array
    
    // create a new array
    const orders = [];
    
    // find stopping point --> the length that 'orders' will be:
    const ordersLength = myArray.length + alicesArray.length;
    
    // create two pointers, 1 for each array:
    let p1 = 0;
    let p2 = 0;
    
    // exceptions: if one array is empty?
    if (myArray.length == 0){
      return alicesArray;
    }
    
    if (alicesArray.length == 0){
      return myArray;
    }
    
  
    for (let i=0; i<ordersLength; i++){
      if (myArray[p1] <= alicesArray[p2]){
        orders.push(myArray[p1]);
        console.log(myArray[p1]);
        p1++;
      }
      else{
        orders.push(alicesArray[p2]);
        console.log(alicesArray[p2]);
        p2++;
      }
    }
  
    return orders;
  }



  // MergedArrays

  function mergeArrays(myArray, alicesArray) {

    // Combine the sorted arrays into one large sorted array
    
    // create a new array
    const orders = [];
    
    // find stopping point --> the length that 'orders' will be:
    const ordersLength = myArray.length + alicesArray.length;
    
    // create two pointers, 1 for each array:
    let p1 = 0;
    let p2 = 0;
    
    // exceptions: if one array is empty?
    if (myArray.length == 0){
      return alicesArray;
    }
    
    if (alicesArray.length == 0){
      return myArray;
    }
    
  
    for (let i=0; i<ordersLength; i++){
      
      if (p1>=myArray.length){
        orders.push(alicesArray[p2]);
        p2++;
      }
      
      else if (p2>=alicesArray.length){
        orders.push(myArray[p1]);
        p1++;
      }
      
      else if (myArray[p1] <= alicesArray[p2]){
        orders.push(myArray[p1]);
        console.log(myArray[p1]);
        p1++;
      }
      
      
      else {
        orders.push(alicesArray[p2]);
        p2++;
      }
    }
  
    return orders;
  }
  


  // HIGHEST SCORE

  function sortScores(unorderedScores, highestPossibleScore) {
  
    // if no unorderedScores, return [];
  
    // Array of 0s at indices 0..highestPossibleScore
    const scoreCounts = new Array(highestPossibleScore + 1).fill(0);
    // 00000000000000000000000000...
  
    //Populated scoreCounts with count of scores
    for (let s = 0; s < unorderedScores.length; s++){
      scoreCounts[unorderedScores[s]]++;
    }
    
    // console.log(scoreCounts);
    
    // create array to hold ordered values
    ordered = [];
    
    // iterate through scoreCounts and push index to new array per the count
    for (let c = highestPossibleScore; c >= 0; c--){
      const count = scoreCounts[c];
      
        for (time = count; time > 0 ; time--){
          ordered.push(c);
        }
    }
     return ordered;
  }
  

  // Merge Sorted Arrays

  function mergeArrays(myArray, alicesArray) {

    // Combine the sorted arrays into one large sorted array
    let p1 = 0;
    let p2 = 0;
    let all = [];
    let allLength = myArray.length + alicesArray.length
    
    for (i=0; i<allLength; i++){
      if (p1 >= myArray.length){
        all.push(alicesArray[p2]);
        p2++;
      }
      else if (p2 >= alicesArray.length){
        all.push(myArray[p1]);
        p1++;
      }
      
      else if (myArray[p1] < alicesArray[p2]){
        all.push(myArray[p1]);
        p1++;
      }
      
      else {
        all.push(alicesArray[p2]);
        p2++;
      }
      
    }
  
    return all;
  }
  


  //Cafe Order Checker (is First Come First Served?)

  function isFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders) {

    // Check if we're serving orders first-come, first-served
  
    let tod = 0 // indext of takeOutOrders
    let dio = 0 // index of dineInOrders
    
    for (let i = 0; i < servedOrders.length; i++){
      // if orders aren't returning from the kitchen:
      if (servedOrders.length !== dineInOrders.length + takeOutOrders.length){
        return false
      }
      
      if (servedOrders[i] == takeOutOrders[tod]){
        tod++
        continue
      }
      
      else if (servedOrders[i] == dineInOrders[dio]){
        dio++
        continue
      }
      
      //else: 
      return false
    }
    
    //all has passed, so return true!
    return true
  }
  


  // Finding 2 movies to perfectly match flight length: 
  
  function canTwoMoviesFillFlight(movieLengths, flightLength) {

    // Determine if two movie runtimes add up to the flight length
    
    // movieLength1 + movieLength2 = flightLength
    // movieLength2 = flightlength - movieLength1
    
    // put movies we've seen so far into a set: 
    const seenMovies = new Set()
    
    for (i = 0; i < movieLengths.length; i++){
      // create variable to hold first movie length
      const firstMovie = movieLengths[i];
      
      // create variable to hold value of the second movie length
      const matchingSecondMovie = flightLength - firstMovie;
      
      //check if second movie length value exists in array
      if (seenMovies.has(matchingSecondMovie)){
        return true;
      }
      
      // add first movie to list to prevent watching the same movie twice
      seenMovies.add(firstMovie);
    }
  
    return false;
  }



  // Fibonacci --- recursive

  function fib(n) {

    // Compute the nth Fibonacci number
    // fib(0) = 0
    // fib(1) = 1
    // fib(n) = fib(n-1) + fib(n-2)
    
    if (n === 0 || n === 1){
      return n;
    }
    
    return fib(n-1) + fib(n-2);
  }
// This is a recursive function, and makes two child calls for each n, 
// therefore it has an exponential time cost --> O(2^n)
  

  // Fibonacci -- non-recursive 0(n) time and 0(1) space

  function fib(n) {

    // Compute the nth Fibonacci number
    // fib(0) = 0
    // fib(1) = 1
    // fib(n) = fib(n-1) + fib(n-2)
    // current = (current-1) + (current - 2)
    // current = (previous) + (prevPrevious)
    
    // edge case:
    if (n < 0) {
      throw new Error('Index cannot be negative.');
    }
    
    else if (n === 0 || n === 1){
      return n;
    }
  
    let prevPrev = 0; // 0th fibonacci
    let prev = 1;     // 1st fibonacci
    let current;      // declare current
    
    // start for loop at i = 1 because we know 0, 1
    for (let i = 1; i < n; i++){
      
      current = prev + prevPrev;
  
      // reassign the incrementation
      prevPrev = prev;
      prev = current;
    }
  
    return current;
  }

  

// Find Unique Integer --> Missing Drone Question
function findUniqueDeliveryId(deliveryIds) {

  // Find the one unique ID in the array

  // make a set from deliveryIds to get only unique numbers
  const delivSet = new Set (deliveryIds);
  
  // find the sum of the set, and the sum of deliveryIds
  const sumSet = Array.from(delivSet).reduce((a, b) => a+b, 0);
  const sumArr = deliveryIds.reduce((a, b) => a+b, 0);
  
  // use math: 2(a+b+c) - (a+a+b+b+c) = c
  return (2 * sumSet) - sumArr;
  
}

// or use XOR ^: 

function findUniqueDeliveryId(deliveryIds) {

  // // Find the one unique ID in the array
  
  //use XOR
  // set uniqueID to 0
  var uniqueDeliveryId = 500;
  
  //apply XOR operator to each deliveryId
  deliveryIds.forEach(deliveryId=> {
    uniqueDeliveryId ^= deliveryId;
  });
  
  return uniqueDeliveryId;
}


// Array of n + 1 numbers -- which number appears twice? 

function findRepeat(numbers) {

  // Find the number that appears twice
  
  //(n**2+n)/2 = sum
  //sum(array) - sum
  
  const n = numbers.length-1;
  const sum = (n**2 + n) / 2;
  const arrSum = numbers.reduce((a, b) => a + b);
  
  return arrSum - sum;

}