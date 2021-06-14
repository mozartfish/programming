function foobar() {
  console.log("inside function");
}
foobar();

thing();
function thing() {
  console.log("thing function");
}

var foo = function () {
  console.log("inside a func");
};

function calc() {
  return "inside function";
}

var returned = calc();
console.log(returned);

function thingy(num1, num2) {
  return num1 + num2;
}

console.log(thingy(4, 5));
