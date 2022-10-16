let carts = document.querySelectorAll('.addToCart');
let cartsDelete = document.querySelectorAll('.delete');
let objList = document.querySelectorAll('.card');
let products = [];
let  bb = document.getElementById

objList.forEach((el,idx) => {

    let title = el.childNodes[1].innerText;
    console.log(title);
    let productz = {title:title,
        tag:title,incart:0}
        products.push(productz)
});

console.log( products);


/*
let products = [
{
    title:'Яблоко',
    tag:'Яблоко',
    inCart:0
},
{
    title:'Банан',
    tag:'Банан',
    inCart:0
},
{
    title:'Апельсин',
    tag:'Апельсин',
    inCart:0
}
]
console.log( products)
*/

for (let i=0; i < carts.length; i++) {
    carts[i].addEventListener('click', () => {
        cartNumbers(products[i]);

    })
}








function onLoadCartNumbers() {
    let productNumbers = localStorage.getItem('cartNumbers');
    if(productNumbers) {
        document.querySelector('.cart-num').textContent = '';

    }


}

function cartNumbers(product) {
    let productNumbers = localStorage.getItem('cartNumbers');
    productNumbers = parseInt(productNumbers)
    if ( productNumbers) {
        localStorage.setItem('cartNumbers',productNumbers + 1);
       // document.querySelector('.cart-num').textContent = productNumbers + 1;

    } else {
        localStorage.setItem('cartNumbers',1);
       // document.querySelector('.cart-num').textContent = 1;
    }

    setItems(product);
}

function setItems(product) {
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);

    if(cartItems != null) {

        if(cartItems[product.tag] == undefined) {
            cartItems = {
                ...cartItems,
                [product.tag]:product

            }
        }
        cartItems[product.tag].inCart += 1;
    } else {
        product.inCart = 1;

        cartItems = {
           [product.tag]:product
   
       }

    }
    
    localStorage.setItem('productsInCart', JSON.stringify(cartItems))

}


function displayCart() {
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);
    let productContainer = document.querySelector('.products-container');

   /* console.log(cartItems)
    console.log(productContainer)*/

    if(cartItems &&  productContainer) {
        productContainer.innerHTML = '';
        console.log('This is products',cartItems)
        Object.values(cartItems).map(item => {
            productContainer.innerHTML += `
           <div class="products">
           <button onclick="deleteElement('${item.title}')" class="delete">x</button>
           <h5> ${item.title} </h5> <br>
           </div>\
            `
     })

} 

}

function update() {
    let items = localStorage.length
    let productContainer = document.querySelector('.products-container');

    if (items == 0) {
        
        productContainer.innerHTML ='<div class="product">Корзина пуста </div>';




        
    } else {
        console.log('str dont eq 0')
    }
}


function deleteElement(title){
  let cartItems = localStorage.getItem("productsInCart");
  cartItems = JSON.parse(cartItems);
  delete cartItems[title]
  localStorage.setItem('productsInCart', JSON.stringify(cartItems))
  displayCart();


}

function clearCart() {
    localStorage.clear("productsInCart");
    update();

}








onLoadCartNumbers();
displayCart();
