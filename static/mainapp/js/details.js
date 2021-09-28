
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

    item.onclick = () =>{
        mainImage.src = item.src;
    }
    // item.onmouseout= () =>{
    //     console.log("I am out!!!")
    //     mainImage.src = biggerImage
    // }
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


var LoadMoreComment = document.getElementById("loadMoreComment")

LoadMoreComment.addEventListener("click",function(){
    var offset = document.querySelectorAll("#comment-box").length
    var limit = LoadMoreComment.dataset.limit_comments
    var total = LoadMoreComment.dataset.total_comments
    console.log(offset,limit,total)

    url = window.location.href

    data = {
        'offset':offset,
        'limit':limit
    }
    
    $.ajax({
        url: url,
        data: data,
        dataType : 'json',
        beforeSend:function(){
            $("#loadMoreComment").attr('disabled',true)
            $("#load-more-comment-icon").addClass("fa-spin")
        },
        success:function(res){
            console.log(res.data)
            $("#loadMoreComment").attr('disabled',true)
            $("#load-more-comment-icon").addClass("fa-spin") 
            $("#comment-section").append(res.data)
            var _countTotal=$("#comment-box").length;
            if(_countTotal == total){
                $("#LoadMoreComment").remove();
            }else{
                $("#LoadMoreComment").removeClass('disabled').text('Load More');
            }
                        
        }
    })

})