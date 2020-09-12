// 189 ROTATE ARRAY
// Given an array, rotate the array to the right by k steps, where k is non-negative.

// Follow up:

// 	Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
// 	Could you do it in-place with O(1) extra space?


//  
// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Constraints:


// 	1 <= nums.length <= 2 * 10^4
// 	It's guaranteed that nums[i] fits in a 32 bit-signed integer.
// 	k >= 0


//////////////////////

// pop() and unshift() method

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]

var rotate = function(nums, k) {
    k = k % nums.length;
    
    while (k < 0) {
        nums.unshift(nums.pop());
        k--;
    }
};



//////////////////////
// reverse() array method:

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]

var rotate = function(nums, k) {
    // find modulus to eliminate redundant rotations
    k = k % nums.length;
    
    // reverse full array --> 7,6,5,4,3,2,1
    // reverse 0 - k-1 --> 5,6,7,4,3,2,1
    // reverse k - nums.length-1 --> 5,6,7,1,2,3,4

    reverse(nums, 0, nums.length-1);
    reverse(nums, 0, k-1) ;   
    reverse(nums, k, nums.length-1);
};

var reverse = function(nums, start, end) {
    while (start < end) {
        let temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}



// 217 Contains Duplicate

// Given an array of integers, find if the array contains any duplicates.

// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:

// Input: [1,2,3,1]
// Output: true

// Example 2:

// Input: [1,2,3,4]
// Output: false

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let numsSet = new Set(nums);
    return numsSet.size < nums.length;
}




// 136 Single Number

// Given a non-empty array of integers, every element appears twice except for one. Find that single one.

// Note:

// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Example 1:

// Input: [2,2,1]
// Output: 1


// Python:

// class Solution:
//     def singleNumber(self, nums: List[int]) -> int:
//         return 2 * sum(set(nums)) - sum(nums)


// Javascript 1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let set = new Set();
    
    // 'for variable of iterables' syntax is used with sets
    for (let num of nums){
        if (set.has(num)){
            set.delete(num);
        }
        else{
            set.add(num);
        }
    }
    return Array.from(set)[0];
};


// 2)

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    // 2 * (a+b+c) - (a+a+b+b+c) = c
    // get set from nums:
    let numSet = new Set(nums);
    
    // get sum of set, and sum of nums
    
    sumSet = findSum(Array.from(numSet));
    sumNums = findSum(nums);
    
    // return result of above equation:
    return (2 * sumSet) - sumNums
};

var findSum = function(arr) {
    let sum = 0;
    
    for (var i = 0; i < arr.length; i++){
        sum = sum + arr[i];
    }
    return sum;
}