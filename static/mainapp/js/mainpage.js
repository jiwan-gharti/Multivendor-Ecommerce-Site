console.log("main page")

// for cart notification
var notify = document.querySelector(".notify");
var addTocartBtn = document.querySelector(".add-to-cart")

addTocartBtn.addEventListener("click", function(){
    var add = Number(notify.getAttribute('data-count') || 0)
    notify.setAttribute("data-count", add + 1)
    if (add == 0){
        notify.classList.add("add-numbs");
    }
});

// end notification cart 


// progress bar indicator

window.onscroll = function(){
    // console.log('scrolling')
    var scrollTopPosition = document.documentElement.scrollTop;
    // console.log(scrollTopPosition)
    var totalHeight = document.documentElement.scrollHeight;
    var visibleDocumentSize = window.innerHeight;
    
    var calculatedWidth = scrollTopPosition / (totalHeight - visibleDocumentSize) * 100;

    if(scrollTopPosition <= 10){
        document.querySelector('.scroll-progress').style.height = "0";
    }else{
        document.querySelector('.scroll-progress').style.height = "2px";
        document.querySelector('.scroll-progress').style.width = calculatedWidth + "%";
    }

}

//search toggle
const searchIcon = document.querySelector('.search-icon');
const search = document.querySelector('.search-wrapper');

searchIcon.onclick = function(){
    search.classList.toggle('hide-show');
}

