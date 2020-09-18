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