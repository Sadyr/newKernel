/* 
// Function

// function declaration
function greet(name) {
    console.log('Привет', name)
}


// Function expression
const greet2 = function greet2(name) {
    console.log('Привет 2 ',name)
}


greet('Лена')
greet2('Лена')

console.dir( greet)
 */

// Аномнимные функции
/* let counter = 0
const iterval = setInterval(function(){
    console.log(++counter)
}, 1000)
 */

// Стрелочные функции


/* function greet(name) {
    console.log('Привет', name)
}

const arrow = (name) => {
    console.log(name)
}
arrow('Sadyr')

const pow = num => {
    return num ** 2
}
console.log(pow(5)) */


// Параметры по умолчанию

/* const sum = (a,b=1) => a + b

console.log(sum(41,7))
 */

/* 
function sumAll(...all
    console.log(all)
)
sumAll(1)
 */

function createMember(name) {
    return function(lastname) {
        console.log(name+lastname)
    }
}

const logWithLastName = createMember('Sadyr')
console.log(logWithLastName)
