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