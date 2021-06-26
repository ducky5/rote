// strict equality check
if (1 === '1') { // "===" data types must BE equal too
  console.log(true)
}
else {
  console.log(false)
}

// strict inequality check
if (1 !== '1') { // "!==" data types must NOT be equal too
  console.log(true)
}
else {
  console.log(false)
}

/* ternary operator
condition ? if-true : if-false
*/
1 === "1" ? console.log(true) : console.log(false)

// nested ternary operator
function natureOfNum(num) {
  return num > 0 ? "Positive" : num < 0 ? "negative" : "zero"
}
console.log(natureOfNum(1), natureOfNum(0), natureOfNum(-1))
