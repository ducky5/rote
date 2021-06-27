var array = ["Me", "Myself", "I"]

// append elements to the array
array.push("MyPersonality", "MyMind")
console.log(array)

// a way to concatenate an array to string and still show that it's an array
console.log("\narray: ", JSON.stringify(array) + "\n")

// add elements to the beginning of the array
array.unshift("MySoul")
console.log(array)

// remove first element
array.shift()
console.log(array)

// remove last element
array.pop()
console.log(array)

// spread operator
let array2 = [...array]
console.log("array2 = " + JSON.stringify(array2))
