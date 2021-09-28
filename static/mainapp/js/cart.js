console.log("cart here")

var user = '{{request.user}}'

var updateBtns = document.querySelectorAll(".update-cart")


        

updateBtns.forEach((updateBtn) =>{
    updateBtn.addEventListener('click', function(e){

        e.preventDefault()
        
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product ID',productId,' Product Action:', action)


        if(user == "AnonymousUser"){
            addCookieItem(productId, action)
        }
        else{
            // console.log("first--------------------")
            // console.log(productId, action)
            updateUserOrder(productId, action)
        }

    })
})

function addCookieItem(productId, action){
    

}

function updateUserOrder(productId, action){

    console.log("User Logged in and Sending update quantity")

    var url = '/update_item/'
    
    
    // var url = "{% url 'update_item' %}"
    // console.log(url)
    // var url = window.location.href
    console.log(url)

    fetch(url, {
        method: "POST",
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken':csrftoken,

        },
        body:JSON.stringify({'productId':productId,'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        location.reload()
        // console.log(data.data)
        // $(this).prop('disabled',true)
        // $("#cart-page").html(data.data).load(url)
    })

    
}


console.log("here")
var expected_date = document.getElementById("expected_date")
window.addEventListener('load', (event) => {
    var date = new Date();
    date.setDate(date.getDate() + 7);
    expected_date.textContent = date
    console.log(date);
});


