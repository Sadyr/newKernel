/*
Array iteration methods operate on every array item.
The forEach() method calls a fucntion (a callback function) once for eache array elemetn
*/
const numbers = [45,4,9,16,25];
let txt = '';
numbers.forEach(myFunction);
function myFunction(value) {
    console.log(txt += value + "<br>");
}