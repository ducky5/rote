// function declaring(with parameters)
function hello_there(username) {
  console.log("hello there " + username + "!")
}

// function calling(with arguments)
hello_there("Duck")

var key = "\nmy-global-key"

function private() {
  // local variable takes precedence
  var key = "\nmy-local-key"
  return key
}

// note: a function without a return statement will return undefined
var function_key = private() // variable now contains what private() returns
console.log(function_key)
