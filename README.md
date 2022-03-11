# oxalic
Documenting the conceptual Oxalic programming language

## The Purpose of Oxalic
Inspired by the talk *"The Post JavaScript Apocalypse"* by Douglas Crockford.

## Syntax
```oxa
# Initalize Module
@my package;

# Function with return
add(a,b) : {
  a + b;
}

# Function without return
display(a) {
  [a];
}

[add(2,3)];
display("Smile more!");

my name : "Kai Lyons";

# Display hello world
["Hello, World!"];
  
# An if statement
my name = "John Doe" {
  ["True"];
} | my name = "Jane Eod" {
  ["Elif True"];
} | {
  ["False"];
} 

# "While" loop
count ten(counter) {
  counter = 10 {
    [counter];
  } | {
    [counter];
    newCounter : counter + 1;
    count ten(newCounter);
  }
}
count ten (0)
```
