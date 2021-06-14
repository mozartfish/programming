var person = {
  name: "bob",
  age: 15,
  details: {
    hobbies: ["sports", "cooking"],
    location: "USA",
  },
  greet: function () {
    // console.log("hello");
    console.log("Hello, I am " + this.name);
  },
};
console.log(person);
// dot notation
console.log(person.name);
// array notation for dynamic creation
console.log(person["name"]);
console.log(person.details.hobbies);
person.greet();
console.log(typeof person);
console.log(typeof person.name);
person.name = "harold";
console.log(person);

// alternative object generation
var anotherPerson = new Object();
anotherPerson.age = 27;
anotherPerson.name = "Lord Voldemort";
console.log(anotherPerson);

// using the person prototype 
var foobar = Object.create(person);
anotherPerson.name = "the foobar";
console.log(foobar.age);
