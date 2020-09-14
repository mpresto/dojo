// To Do 1
// Remove Blanks
// Create a function that, given a string, returns all of that string’s contents, but 
// without blanks. If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

function removeBlanks(str){
   let wordArr = str.split(" ");
   console.log(wordArr.join(""))
   return wordArr;
}

removeBlanks(" Pl ayTha tF u nkyM usi c ")



// Get Digits
// Create a JavaScript function that given a string, returns the integer made from 
// the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return 
// the number 1357924680.

function getDigits(str){
    let wordArr = str.split("");
    let newArr = [];
    for (let i=0; i<str.length; i++){
        if (wordArr[i] =='0' || wordArr[i] == '1' || wordArr[i] == '2' || wordArr[i] == '3' || wordArr[i] == '4' || wordArr[i] == '5' || wordArr[i] == '6' || wordArr[i] == '7' || wordArr[i] == '8' || wordArr[i] == '9'){
        // if (typeof wordArr[i] === 'number'){
            newArr.push(wordArr[i]);
        }
    }
    console.log(newArr.join(''));
    return newArr;
}

getDigits("0s1a3y5w7h9a2t4?6!8?0")



// Acronyms
// Create a function that, given a string, returns the string’s acronym (first letters only, capitalized).
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 
// Given "Live from New York, it's Saturday Night!", return "LFNYISN".


function getAcronym(str){
    let wordArr = str.split(' ');
    let newArr = [];
    for (let i=0; i<wordArr.length; i++){
        newArr.push(wordArr[i][0]);
    }
    console.log(newArr.join('').toUpperCase());
    return newArr.join('').toUpperCase();
}

getAcronym("Live from New York, it's Saturday Night!")




// Count Non-Spaces
// Accept a string and return the number of non-space characters found in the string. 
// For example, given "Honey pie, you are driving me crazy", return 29 (not 35).

function countNonSpaces(str){
    let wordArr = str.split(' ');
    let count = wordArr.join('').length;
    console.log(count);
}

countNonSpaces("Honey pie, you are driving me crazy")



// Remove Shorter Strings
// Given a string array and value (length), remove any strings shorter than the length from the array.

function removeShortStrings(strArr, len){
    let newArr = [];
    for (let i=0; i<strArr.length; i++){
        if (strArr[i].length >= len){
            newArr.push(strArr[i]);
        }
    }
    console.log(newArr);
}

removeShortStrings(['Live', 'from', 'New', 'York,', "it's", 'Saturday', 'Night!'], 4)



console.log(1 + 2 + "3" + "4" + 5 + 6);



// To Do 2
// Reverse
// Implement reverseString(str) that, given string, returns that string with characters reversed.
// Given "creature", return "erutaerc". Tempting as it seems, do not use the built-in reverse()!

function reverseString(str){
    let arr = str.split('')
    for (let i=0; i<(arr.length-1)/2; i++){
        let temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    str = arr.join('')
    console.log(str);
    return str;
}

reverseString("creature")


// Remove Even-Length Strings
// Build a standalone function to remove strings of even lengths from a given array. For array containing
// ["Nope!","Its","Kris","starting","with","K!","(instead","of","Chris","with","C)","."], 
// change that same array to ["Nope!","Its","Chris","."].

function removeEven(arr){
    let count = 0;
    // loop through each element and check length
    for (let i = 0; i < arr.length; i++){
        // if length modulus 2 == 0 (ie, if its even)
        if (arr[i].length % 2 == 0){
            arr.remove(arr[i]);
            count ++;
        } 
    }
    for (each in count){
        arr.pop();
    }
    console.log(arr);
    return arr;
    
}

removeEven(["Nope!","Its","Kris","starting","with","K!","(instead","of","Chris","with","C)","."])



// Integer to Roman Numerals
// Given a positive integer that is less than 4000, return a string containing 
// that value in Roman numeral representation. In this representation, 
// I is 1, V is 5, X is 10, L = 50, C = 100, D = 500, and M = 1000. 
// Remember that 4 is IV, 349 is CCCIL and 444 is CDXLIV.



// Roman Numerals to Integer
// Sept 16, 2014 headline: “Ancient Computer Found in Roman Shipwreck”. 
// Comprising 30 bronze gears, its wooden frame features 2000 characters. 
// Given a string containing a Roman numeral representation of a positive integer, 
// return the integer. Remember that III is 3, DCIX is 609 and MXDII is 1492.