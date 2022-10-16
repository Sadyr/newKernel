/*
if you have a list of items (a list of a car names, for example), storing the cars in single variables could look like this:
*/
let car1 = 'Saab';
let car2 = 'Volvo';
let car3 = 'BMW';

const cars = ["Saab", "Volvo", "BMW"];
console.log(cars);
console.log(cars[0]);
console.log(cars[1]);
console.log(cars[2]);

cars[0] = "Opel";
console.log(cars[0])
console.log(cars);


/*
Arrays are Objects
Arrays are special type of objects. The typeOf operstor in JS returns "object" for arrays
But, JS arrays are best described as arrays.
Arrays use numbers to access its "elements". In this example, person[0] returns John
*/
const person = ["John", "Doe", 46];
console.log(person[0]);

/*
Objects use names to access its "members", in this example, person.firstName returns John:
*/

const persona = {firstName:"Jrohn", lastName:"Doe", age:46};
console.log(persona.firstName);


/*
Array Elements Can Be Objects
JS variables can be objects . Arrays are special kinds of objects.
Because of this, you can have variables of different types in the same Array.
You can have objects in an Array. You can have functions in an Array. You can have arrays in an Array:
*/

/* myArray[0] = Date.now;
myArray[1] = myFunction;
myArray[2] = myCars;
console.log(myArray)
*/

 
/*
Array properties and methods
The real strength of js arrays are the built-in array properties and methods:
*/


cars.length // Returns the number of elements
cars.sort() // Sorts the array

/*
Array methods are covered in the next chapters.
*/

/*
The length property of an array returns the length of an array (the number of array elements).
*/
const fruits = ["Banana", "Orange", "Apple", "Mango"];
let length = fruits.length;
console.log(length);

/*
The length property is always one more than the highest array index.
*/
 
/*
Accessing the First Array element  and last element
*/
console.log(fruits[0]);
console.log(fruits[fruits.length-1]);

/*
Looping Array Elements
One way to loop through an array, is using a for loop:
*/
let fLen = fruits.length;
for (let i = 0; i < fLen; i++){
    console.log(fruits[i])
}

/*
You can also use the Array.forEach() function:
*/
let text = "<ul>";
fruits.forEach(myFunction);
text += "</ul>";
function myFunction(value){
    text += "<li>" + value + "</li>";
    console.log(text);
}


/*
The easiest way to add a new element to an array is using the push() method:
*/
fruits.push("Lemon");
console.log(fruits);

/*
New element can also be added to an array using the length property:
*/

fruits[fruits.length] = "Persic";
console.log(fruits);

/*
WARNING!
Adding elements with high indexes can create undefined "holes" in an array:
*/
fruits[8] = "Vinograd";
console.log(fruits);

