
console.log('bang bang');
const replyBtn = document.querySelector(".comment-reply");
const  reply= document.querySelector(".reply");

replyBtn.addEventListener("click",function(){
    console.log('fang fang')
    // if(!reply.classList.contains('reply-show')){
        reply.classList.toggle('reply-show');
    // }
}); 