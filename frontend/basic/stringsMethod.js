// The lenght property returns the lenght pf a string

let txt = "jvKONMVKNVKLNVKLEFNVKEFVKLNVKNVKLNVK";
let = lenght = txt.length;
console.log(lenght)


 /* Extracting string parts
There are 3 methods for extracting a part of string

slice (start,end)
subscripting(start,end)
substr(start,length)

Javascript string slice
slice() extracts a part of a string and returns the extracted part in a new string
The method takes 2 parameters: the start position, and the end position (end not included)
*/

let str = "Apple, Banana, Kiwi"
let part = str.slice(7,14)
console.log(part)


/*
Note: Javascript counts positions from zero.
First position is 0.
Second position is 1.

if a parameter is negative, the position is counted from the end of the string.
This example slices out a position of a string from position -12 to position -6
*/

let part2 = str.slice(-14,-6)
console.log(part2)


/*
Javascript string substring()
substring() is similar to slice().
The difference is that start and end values less than 0 are treated as 0 in substring()
*/

let part3 = str.substring(-7,13);
console.log(part3)


/*
Javascript string substr()
The difference is that the record parameter specifies the lenght of the extracted part.
*/
let part4 = str.substr(7);


/*
Replacing string content 
The replace() method replaces a specified value with another value in a string.
*/

let text = "Please visit Microsoft";
let newText = text.replace("Microsoft", "W3Schools");
console.log(newText);

/*
By default, the replace() method replaces only the first match
*/

/*
To replace all matches, use a regular expressions a /g flag (global matches)
*/
let text2 = "Please visit Microsoft and Microsoft";
let newText2 = text2.replace(/Microsoft/g, "Sadyr");
console.log(newText2)


/*
Converting ti Upper and Lower case
A string is converted tu upper case with toUpperCase();
A string is converted to lower case with toLowerCase();
*/
let text3 = "Hello world";
let text5 = text3.toUpperCase();
console.log(text5)


let text6 = "Hello World";
let text7 = text6.toLocaleLowerCase();
console.log(text7)

/*
Javascript string concat()
concat() joins two or more strings:
*/
let text8 = "Hello";
let text9 = "World";
let text10 = text8.concat("hh ", text9);
console.log(text10)


/*
Javascript string trim()
The trim() method removes whitespace from both of a string:
*/
let tex1 = "      Hello worldmmmmmm k  "
let tex2 = tex1.trim();
console.log(tex2) 

/*
Javascript string trimStart()
The trimStart() method works like trim , but removes whitespace only from the start 
of a string.
*/

let tex3 = "   Hello world    ";

let tex4 = tex3.trimStart();
console.log(tex4)


/*
javascript string trimEnd()
The trimEnd() method works like trim() , but removes whitespace only from the end of a string.
*/

let te = "   Hello world     "
let te2 = te.trimEnd();
console.log(te2)


/*
Javascript string split()
A string can be converted to an array with the split() method:
*/

let t = 'Hello ';
console.log(t.split(" "))


