# oxalic-doc
Documenting the conceptual Oxalic programming language

## The Purpose of Oxalic
Inspired by the talk *"The Post JavaScript Apocalypse"* by Douglas Crockford. Oxalic is an immutable programming language (that allows for mutability if the developer specifies), and it assumes that the user is stupid - as any developer should do anyways. It is a C-like programming language. It is to transpile into JavaScript, and only does strict checking through JavaScript's `===` operator, as type checking is important to remove bugs and issues. There is no `null` in oxalic, as null is the billion dollar mistake. Oxalic is currently designed to be an overlay to JavaScript, but if someone smarter than me makes a version for desktop, I will be excited.

## Syntax
```oxa
f main() {
  display("Hello, world!");
  
  # Variables
  var myInt   : 0;
  var myName  : "Kai Lyons";
  mut counter : 0;
  
  # If/Else
  if ( myInt = 0 ) {
    display("Hello, world!");
  } else {
    display("Goodbye, mars!);
  }
  
  # While
  while ( counter <= 10 ){
    display(counter)
  }
  
  # Try
  try {
    # Code to try
  } error {
    # Splits out an error
  }
}
```
