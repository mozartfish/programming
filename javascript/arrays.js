var foo = [1, 2, 3, 4];
console.log(fooS);
console.log(foo[0]);
foo[1] = 100;

// looping
foo.forEach(function (element) {
  console.log(element);
});

// Push => add value at the end of the array
foo.push(10);

// Pop => removes and returns the last element
foo.pop();

// Shift => remove and return first element
foo.shift();

// Unshift => add element to the front of array
foo.unshift("hello");

foo[foo.indexOf("hello")] = "world";

// - start position and number of elements
var thing = foo.splice(2, 2);

console.log(thing);

// does not modify old array
var bar = foo.slice(2, 4);

// filter
console.log(
  foo.filter(function (value) {
    return value > 2;
  })
);

// reverse original array
console.log(foo.reverse());

// concat and join
var newArr = ["hello", "world"];

// creates a new combined single array
console.log(foo.concat(newArr));

// join joins array into string
console.log(array.join(newArr));

// reduce
var foobar = [1, 2, 3, 4, 5, 6];
console.log(
  foobar.reduce(function (total, value) {
    return total + value;
  })
);
