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
  