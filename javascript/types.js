var a = 5;
var b = a;

// Primitive Types - strings, numbers, booleans etc
// Reference Types - objects

var c = { a: 5 };
d = c;

var aNum = 5;
console.log(aNum);
var anotherNum = aNum;
console.log(anotherNum);
aNum = 12;

var arr = [1, 2, 3];
console.log(typeof arr);
console.log(arr);
var anotherArr = arr;
console.log(anotherArr);

// Scope
var test = "hello";
console.group(test);

function localScope() {
  console.log(test);
}
localScope();
