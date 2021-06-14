var age = 15;

var person = {
  name: "lord voldemort",
  age: 27,
};

// console.log(person.prototype);
console.log(person.__proto__);
console.log(person.toString());

// think of prototype as parent
Object.prototype.greet = function () {
  console.log("Hello, There");
};

person.greet();

var foobar = Object.create(person);
console.log(foobar.name);
foobar.greet();
var foo = Object.create(person);
foo.name = "harold";
foo.greet();

