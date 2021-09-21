console.log("merchant dashboard!!");

var updateBtn = document.getElementById('update-button');
console.log(updateBtn)
var updateSection = document.querySelector('.update-section')
var closeBtn = document.querySelector('.close-btn')
var deletebtn = document.querySelector('.delete-btn')
var deleteConfirm = document.querySelector('.delete-section')
var cancelBtn = document.querySelector('.cancel-btn')
console.log(cancelBtn)

updateBtn.addEventListener('click',function(){
    console.log("clicked update!!");
    if (updateSection.classList.contains("show")){
        updateSection.classList.remove("show")
    }else{
        updateSection.classList.add("show")
    }
});

closeBtn.addEventListener("click",function(){
    updateSection.classList.remove("show")
});
cancelBtn.addEventListener("click",function(){
    
    deleteConfirm.classList.remove("show")
});

deletebtn.addEventListener('click',function(){
    console.log("ckicked delete!!");
    if (deleteConfirm.classList.contains("show")){
        deleteConfirm.classList.remove("show")
    }else{
        deleteConfirm.classList.add("show")
    }
});
