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
  
