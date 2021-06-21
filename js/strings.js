var string = "Hello, "
var string_end = "World!"

// escape character
var string_with_quotes = "PMT stands for \"Personality Matching Tool\""
console.log(string_with_quotes)

// strings can be concatenated via the (+) sign
console.log(string + string_end)

// concatenating shortcut (same as str = str + string_end)
var str = "The_"
str += string_end
console.log(str)

// string length
var hello_length = "hello".length
console.log(hello_length)

// find nth character in string using bracket notation
console.log(str[3]) // should output "_"

// find last character in string
console.log(str[ str.length - 1 ])
