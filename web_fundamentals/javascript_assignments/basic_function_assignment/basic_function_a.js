// TOTAL NUMBER OF CORRECT PREDICTIONS: 13/15

//1. Predicted output: 35
function a(){
    return 35;
}
console.log(a())
// Actual output: 35


// 2. Predicted output: 8
function a(){
    return 4;
}
console.log(a()+a());
//Actual output: 8


// 3. Predicted output: 6
function a(b){
    return b;
}
console.log(a(2)+ a(4));
//Actual output: 6


//4. Predicted output: 3, 9
function a(b){
    console.log(b);
    return b*3;
}
console.log(a(3));
// Actual output: 3, 9


// 5. Predicted output: 40
function a(b){
    return b*4;
    console.log(b);
}
console.log(a(10));
//Actual output: 40


//6. Predicted output: 4
function a(b){
    if(b<10) {
        return 2; 
    }
    else {
        return 4; 
    }
    console.log(b);
}
console.log(a(15));
//Actual output: 4


//7. Predicted output: 10,3, 30
function a(b, c){
    return b*c;
}
console.log(10,3);
console.log(a(3,10));
//Actual output: 10,3, 30


//8. Predicted output: 3, 4
function a(b){
    for(var i=0; i<10; i++){
        console.log(i);
    }
    return i;
}
console.log(3);
console.log(4);
//Actual output: 3, 4


// 9. Predicted output: 2, 5, 8, 11
function a(){
    for(var i=0; i<10; i++){
        i = i+2;
        console.log(i)
    }
}
a();
//Actual output: 2, 5, 8, 11


// 10. Predicted output: 0,1,2,3...7,8,9,0,0,1,2,...8,9,0
function a(b, c){
    for(var i=b; i<c; i++){
        console.log(i);
    }
    return b*c;
}
a(0,10);
console.log(a(0,10));
// Actual output: 0,1,2,3...7,8,9,0,1,2...8,9,0

// 11. Predicted output: none (function not called)
function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(j)
        }
        console.log(i);
    }
}
//Actual output: none


// 12. Predicted output: none 
function a(){
    for(var i=0; i<10; i++){
        for(var j=0; j<10; j++){
            console.log(i,j);
        }
        console.log(j,i);
    }
}
// Actual output: none


// 13. Predicted output: 10 (scope!)
var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
console.log(z);
// Actual output: 10


// 14. Predicted output: 15, 10 (scope!)
var z = 10;
function a(){
    var z = 15;
    console.log(z);
}
a();
console.log(z); 
// Actual output: 15, 10


// 15. Predicted output: 15
var z = 10;
function a(){
    var z = 15;
    console.log(z);
    return z;
}
z = a();
// console.log(z);
// Actual output: 15, 15
