
const subImage = document.querySelectorAll(".image-change-js");
const mainImage = document.querySelector(".main-image");
const mainImageContainer = document.querySelector(".main-image-layout");


subImage.forEach((item, index) => {

    var flag = true;
    if(flag){
        flag = false;
        biggerImage = mainImage.src
        console.log(biggerImage)
    }

    item.onmouseover = () =>{
        mainImage.src = item.src;
    }
    item.onmouseout= () =>{
        console.log("I am out!!!")
        mainImage.src = biggerImage
    }
});

var addToBtn = document.querySelector(".add-to-cart-btn1")

var item = true
addToBtn.addEventListener("click",function(){
    if (item == true){
        addToBtn.textContent = "ADDED"
    }
    else{
        addToBtn.textContent = "Add To cart"
    }
})




// mainImageContainer.onmouseover = function(event){
//     console.log("inside main image ");
//     x = event.offsetX                                         
//     y = event.offsetY
//     console.log(x)
//     console.log(y)

//     width = mainImageContainer.offsetWidth;
//     height = mainImageContainer.offsetHeight;

//     console.log(width)
//     console.log(height)

//     console.log(mainImageContainer.offsetLeft)
//     console.log(mainImageContainer.offsetTop)

//     posX = (x / width) * 100;
//     posY = (y / height) * 100;

//     // console.log(posX, posY)
//     mainImage.style.transform = "translate(-" + posX +"%,-"+ posY +"%) scale(2)";
   
// }
// mainImageContainer.onmouseleave = function(event){
//     console.log("inside main image ")
//     mainImage.style.transform = "translate(0%,0%) scale(1)";
// }








const replyBtn = document.querySelector(".comment-reply");
const  reply= document.querySelector(".reply");

replyBtn.addEventListener("click",function(){
    console.log('fang fang')
    // if(!reply.classList.contains('reply-show')){
        reply.classList.toggle('reply-show');
    // }
}); 