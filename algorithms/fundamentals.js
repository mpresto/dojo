// To Do 1

// // 1
// var myNumber = 42;
// var myName = 'monty';
// temp = [];

// temp = myNumber;
// myNumber = myName;
// myName = temp;

// console.log(myNumber)
// console.log(myName)

// // 2
// for (var i=-52; i<=1066; i++){
//     console.log(i)
// }

// // 3

// function beCheerful(){
//     console.log("good morning!")
// }

// for (var i=0; i<99; i++){
//     beCheerful()
// }

// // // 4
// for (var i=-300; i<=0; i++){
//     if (i==-6 || i==-3){
//         continue;
//     }
//     else{
//         console.log(i);
//     }
// }

// // 5
// var i=2000;
// while (i<=5280){
//     console.log(i);
//     i++;
// }

// // 6
// function birthday(a, b){
//     if (a==4 || b==4 && a==6 || b==6){
//         console.log("Hos did you know?");
//     }
//     else
//     {
//         console.log("Just another day...")
//     }
// }
// birthday(4,6)
// birthday(6,4)
// birthday(3,1)
// birthday(1,3)

// // 7
// function leapYear(num){
//     if (num % 400 == 0){
//         console.log("It's a leap year!");
//     }
//     else if (num % 100 == 0){
//         console.log("Not a leap year!");
//     }
//     else if (num % 4 == 0){
//         console.log("It's a leap year!");
//     }
//     else{
//         console.log("Not a leap year!")
//     }
// }

// leapYear(1900)

// // 8
// var count = 0;
// for (var i = 512; i <= 4096; i++){
//     if(i % 5 == 0){
//         console.log(i);
//         count++;
//     }
// }
// console.log(count)

// // 9
// var i = 0;
// while (i <= 60000){
//     if (i % 6 == 0){
//         console.log(i);
//     }
//     i++;
// }

// // 10
// for (var i = 1; i<=100; i++){
//     if (i % 10 == 0){
//         console.log("Coding Dojo");
//     }
//     else if (i % 5 == 0){
//         console.log("Coding");
//     }
//     else {
//         console.log(i);
//     }
// }

// // 11
// function whaddyaKnow(incoming){
//     console.log(incoming);
// }
// whaddyaKnow(10);

// 12
var sum = 0;
for (var i = -301; i <= 300; i+=2){
    console.log(i);
    sum = sum + i;
}
console.log(sum)