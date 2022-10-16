/*
The JS method toString() converts an array to string of (comma separated) array values.
*/

const fruits = ["Banana", "Orange", "Apple", "Mango"];

console.log(fruits.toString());

/*
The join() method also joins array elements into a string
*/
console.log(fruits.join(" * "))

/*
When you work with arrays, it easy to rmove elements and add new elements.
Hte is what popping and pushing os:
Popping items out of an array, or pyshing items into an array.


 JS pop() method removes the last element from an array:
 */

 console.log(fruits.pop())
 console.log(fruits)

 /* JS push method adds a new element to an array (at the end):
 */
console.log(fruits.push("Kiwi"));
console.log(fruits)

/*
Shifting is equivalent to popping, but working on the first element instead of the last.
*/
/*
The shift() method removes the first array element and "shifts all other elements to a lower index"
*/
const listF = ["Banana", "Orange","Apple", "Mango"];
console.log(listF.shift())
console.log(listF)

/*
JavaScript unshift() method adds a new element to an array (at the beginning), and "unshifts" older elements:
*/
const listG = ["Banana", "Orange","Apple", "Mango"];
console.log(listG.unshift("Lemon"))
console.log(listG)

/*
Changing elements 
Array elements are accessed using their index number:
*/
const fru = ["Banana", "Orange","Apple", "Mango"];
console.log(fru[0]="Kiwi");
console.log(fru)

/*
JS array delete()
WARNING!!!
Array elements can be deleted using the js operator.
Using delete leaves undefined holes in the array.
Use pop() or shift() instead.
*/

const fr = ["Banana", "Orange","Apple", "Mango"];
console.log(delete fr[0]);
console.log(fr)

/*
Merging (Concatenating) Arrays
THe concat() method creates a new array by merging (concatenating) existing arrays:
*/
const myGirls = ["Cecile", "Lone"];
const myBoys = ["Emil", "Tobias", "Linus"];
console.log(myGirls.concat(myBoys));


/*
The concat() method does not change the existing arrays , it always a new array.
The concat() method can take any number of array arguments:
*/

const arr1 = ["Cecile","Lone"];
const arr2 = ["Emil", "tobieas","Linus"];
const arr3 = ["Robin", "Morgns"];
const myChildren = arr1.concat(arr2,arr3);
console.log(myChildren)


