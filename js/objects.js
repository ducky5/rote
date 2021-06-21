// a javascript object
var numbers = {
  // "property": value
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "excluded_0_3included": [1, 2, 3]
}

// accessing object values with (.) notation: object.property
console.log("]0;3]: " + numbers.excluded_0_3included)

// accessing object values with [] notation: object["property"]
console.log("]0;1]: " + numbers["one"])

// add a new property to object using (.) notation: object.new_property
numbers[1] = "one"
console.log(numbers)

// delete property from object
delete numbers[1]
console.log(numbers)

// function to check if object has property
function hasProperty(object, property) {
  if (object.hasOwnProperty(property)) {
    return "object has property \"" + property + "\""
  }
  else {
    return "object does not have property \"" + property + "\""
  }
}
console.log(hasProperty(numbers, "one"))
