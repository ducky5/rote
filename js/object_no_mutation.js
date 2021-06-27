const MATH_CONSTANTS = {
  PI: 3.14
}
// prevent object mutation
Object.freeze(MATH_CONSTANTS)

MATH_CONSTANTS.PI = 99 // line made obsolete by line 5
console.log(MATH_CONSTANTS)
