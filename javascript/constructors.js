function Person() {
  this.name = "Harold";
}

var person = new Person();
// person.name = "Harold";
console.log(person.__proto__ == Person.prototype);
Person.prototype.greet = function () {
  console.log("Hello, I am ", +this.name);
};

Person.prototype.name = "Foobar";
// console.log(this);
person.name = 'gg'
person.greet();


