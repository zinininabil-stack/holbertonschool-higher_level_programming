#!/usr/bin/node

const x = process.argv[2];
const num = parseInt(x);

if (isNaN(num)) {
  console.log("Not a number");
} else {
  for (let i = 0; i < num; i++) {
    console.log("C is fun");
  }
}