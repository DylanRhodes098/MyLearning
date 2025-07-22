let arr1 = [1, 2, 3, 4, 5, 6]
let arr2 = [7, 8, 9, 10, 11, 12]
let obj1 = {"name": "dave", "age": 12}

// merging arrays
let arr3 = [...arr1, ...arr2]
console.log(arr3)

// merging objects
let obj2 = {...obj1,
    "name": "john",
    "heigh":40,
    "crime": "theif"
}
console.log(obj2);

//spread functions
let bigNum = Math.max(...arr1)
console.log(bigNum)