const person = {
    name:'Sadyr',
    age:25,
    isProgrammer:true,
    languages:['ru','kz','ug','en'],
    'complex key':'complex value',
    ['key_'+(1+3)]:'Compiled key',
    
    greet(){
        console.log('greet ftom person')
    },
    info() {
        console.log('this:',this)
        console.info(' Информация про челоувека',this.name)
    },
    

}


/* person.info() */
/* const logger = {
    keys(obj) {
        console.log('Object keys: ', Object.keys(this))
    }
} */

function keysAndValues(obj) {
     let s = Object.keys(obj)
     s.forEach(key => {
        console.log('key: ',key)
        console.log('value: ',obj[key])
     });
     console.log(s)
}



keysAndValues(person)
/* const bound = logger.keys.bind(person)
bound() */
/* logger.keys.call(person)
 *//* const ageKey = 'age'
console.log(person.name)
console.log(person['age'])
console.log(person['complex key'])
console.log(person)
person.greet()

person.age++
person.languages.push('by')
console.log(person)

/* const name = person.name
const age = person.age
const languages = person.languages */
/* const {name,age,languages} = person
console.log(name,age,languages)

 */ 

/* for (let key in person) {
    if (person.hasOwnProperty(key)) {
        console.log('key:',key)
        console.log('value:',person[key])
    }  
}
 */
/* const keys = Object.keys(person)
console.log(keys)
keys.forEach((key) => {
    console.log('key:',key)
    console.log('value:',person[key])

}) */

