/*
The indexOf() method returns the index of (the position of) the first occurrence of a specified text in a string:
*/
let str = "Please locate where 'locate' occurs!"
console.log(str.indexOf("locate"))


/*
The lastOfIndexOf method returns the index of the last occurrence of a specified text in a string
*/
console.log(str.lastIndexOf("locate"))


/*
The search method searches a string for a specified value and returns the position of the match:'
*/
console.log(str.search("locate"))

/*
The match() method searches a string for a match against a regular expression, and returns the matches , as an Array object.
*/
let text = "The rain in SPAIN stays mainly in the plain";
console.log(text.match(/ain/g));


/*
The include() method returns true if a string contains a specified value:
*/
let text2 = "Hello world, welcome to the universe.";
console.log(text2.includes('world'));

/*
The startsWith() method returns true if a string begins with a specified value, otherwise false.
*/
console.log(text2.startsWith("Hello"));

/*
The endsWith() method returns true if a string ends with a specified value, otherwise false:
*/
let text3 = "John Doe";
console.log(text3.endsWith("Doe"));
