function Person(name, age) {
  (this.name = name), (this.age = age);
}

var harold = new Person("harold", 15);
var foobar = new Person("thing", 10);
