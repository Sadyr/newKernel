const heading = document.getElementById('hello')
/* const heading2 = document.getElementsByTagName("h2")
 */
/* const heading2 = document.getElementsByClassName('h2-class')
 */
const heading2 = document.querySelector('.h2-class')
console.log(heading2)
setTimeout( () => {
    addStylesTo(heading)
    },3000)


function addStylesTo(node) {
console.dir(heading.textContent)
node.textContent = "Changed from javascript"
node.style.color = 'red'
node.style.textAlign = 'center'
node.style.backgroundColor = 'black'

}

heading.onclick = () =>  {
    if (heading.style.color = 'red') {
        heading.style.color = '#000'
        heading.style.backgroundColor = '#fff'
    } else {
        heading.style.color = 'red'
        heading.style.backgroundColor = 'black'
    }
 }