/* window.onload = () => {
    let input = document.querySelector("#input");
    input.oninput = function() {
        let value = this.value.trim()
        let list = document.querySelectorAll(".ul li");
        if(value) {
            list.forEach(elem => {
                elemLower = elem.innerText.toLowerCase()
                if (elemLower.search(value.toLowerCase())==-1) {
                    elem.classList.add('hide')
                }
            })
        } else {
            list.forEach(elem => {
                elem.classList.remove('hide')
            })
        }



    }

} */
 
/* let text = 'SADYR'.toLowerCase()
let basic = ' sadyr sauytov'.toLowerCase()
console.log(basic.search(text)) */



/* <script async src="https://cse.google.com/cse.js?cx=53821c8732ea24f12">
</script>
<div class="gcse-search"></div> */




 function search(){
    let input = document.querySelector("#input");
    input.oninput = function() {
        let value = this.value.trim()
        let list = document.querySelectorAll(".ul li");
        if(value) {
            list.forEach(elem => {
                elemLower = elem.innerText.toLowerCase()
                if (elemLower.search(value.toLowerCase())==-1) {
                    elem.classList.add('hide')
                }
                else {
                    elem.classList.remove('hide')
                  }
            })
        
        
        } else {
            list.forEach(elem => {
                elem.classList.remove('hide')
            })
        }



    }

}

search() 





<?php
            if(have_posts()) {
              while(have_posts()) {
                the_post();
               ?>
      <?php 
        $product_image = get_field( 'image' );
         $product_url = get_permalink() ; 
         $product_description = get_field( 'описание_товара' );
      ?>
      
        <?php the_title();?>
;?>
         <?php  echo $product_url  ?>
             
;?>
































