# Oxalic
<center>
  <img src="assets/ab_Oxalic-04.png" alt="Oxalic logo" width="240">
</center>

### No more rusty development concepts

Documenting and prototyping the conceptual Oxalic programming language

## The Purpose of Oxalic
Inspired by the talk *"The Post JavaScript Apocalypse"* by Douglas Crockford.

It doesn't use camel case or under bar variable names, but rather uses spaces for splitting characters in the variable name.

The current prototype only translates to Python 3, and how it does it could do with a lot of work, but it is currently mostly functional for a pretty shitty prototype.

There are no keywords, just programming.

## Limitations:
Most common functionality in programming languages do not work. With the "no keywords" philosophy it is extrememely difficult to transpile into Python (or even assembly if I dare tried to do it).

## Why in Python to Python?
Python is great for prototyping, and since this is not a production system, Python was selected. It's simple, easy to write a quick and dirty codegen system.

## Do you know how to make proper compilers?
No, this project is my first real implementation of a "compiler" of sorts. Even then, it's made with no knowledge of how ones actually work, so it's going to look kinda sucky, and function poorly.

## Hello, world!
```oxa
to whom : "world";
["Hello," to whom "!"];
```