var a = 5;
var b = 10;
console.log(a + b);

a += b;

console.log(a);

var c = "join ";
var d = 3;

console.log(c + d);

a -= b;

a *= b;

var e = 12;
var f = "2";

console.log(e / f);

e = 10;
f = 3;
console.log(e % f);

console.log(1 === 1);
console.log(1 == "1");
console.log(1 !== "1");

console.log(1 === 1 || 2 === 3 || 4 === 5);

// Ternary
a = 5;
b = 5;
if (a === b) {
  console.log("equal");
} else {
  console.log("not equal");
}

console.log(a == b ? "Equal" : "Not Equal!");

// Precedence
a = 5;
b = 6;

console.log((a + b) * 2);

