/*const myNumber = 42;

localStorage.removeItem('number')
console.log(localStorage.getItem('number'))
localStorage.setItem('number',myNumber)
console.log(localStorage.getItem('number'))
localStorage.clear()*/

const object = {
    name: 'Max',
    age:20
}
/*localStorage.setItem('person',JSON.stringify(object))*/
const raw = localStorage.getItem("person")
const person = JSON.parse(raw)
person.name = 'Vladilen'
console.log(person.name)


