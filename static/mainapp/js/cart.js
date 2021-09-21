console.log("cart here")

var user = '{{request.user}}'

var updateBtns = document.getElementsByClassName("update-cart")

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){

        // e.preventDefault()
        
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product ID',productId,' Product Action:', action)


        if(user == "AnonymousUser"){
            addCookieItem(productId, action)
        }
        else{
            updateUserOrder(productId, action)
        }

    })
}

function addCookieItem(productId, action){

}

function updateUserOrder(productId, action){

    console.log("User Logged in and Sending update quantity")

    var url = '/update_item/'

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
        console.log('Data:',data)
    })

}
