var condition = true;
var anotherCondition = true;
if (condition) {
  console.log("true condition");
} else if (anotherCondition) {
  console.log("another condition");
} else {
  console.log("false condition");
}

var foo = 1;
if (foo) {
  console.log("true");
} else {
  console.log("false");
}

var bar = 8;
switch (bar) {
  case 1:
    console.log("is 1");
    break;
  case 8:
    console.log("is 8");
    break;
  default:
    console.log("default");
    break;
}

for (var i = 0; i < 5; i++) {
  console.log(i);
}

for (var i = 0; i < 5; i++) {
  for (var j = 0; j < 2; j++) {
    console.log(i * j);
  }
}

for (var i = 0; i < 5; i++) {
  if (i === 1) {
    break;
  }
  console.log(i);
}

for (var i = 0; i < 5; i++) {
  if (i == 1) {
    continue;
  }
  console.log(i);
}

for (var i = 0; i < 5; i++) {
  for (var j = 0; j < 2; j++) {
    if (i == 1) {
      continue;
    }
    console.log("inside inner loop, j = " + j);
  }
  console.log(i);
}

for (var i = 0; i < 5; i++) {
  for (var j = 0; j < 2; j++) {
    if (i == 1) {
      break;
    }
    console.log("inside inner loop, j = " + j);
  }
  console.log(i);
}

var array = [1, 2, 3, 4];
for (var i = 0; i < array.length; i++) {
  console.log(array[i]);
}

var number = 5;
while (number < 7) {
  console.log(number);
  number++;
}

var condition = true;
var j = 2;
while (condition) {
  if (i == 3) {
    condition = false;
    console.log(i);
  }
  console.log(condition);
}

condition = false;
do {
  console.log("Execute!");
} while (condition);
