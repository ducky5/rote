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
