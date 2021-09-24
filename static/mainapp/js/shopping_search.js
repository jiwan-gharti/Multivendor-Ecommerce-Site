
var min_max_button = document.getElementById("min_max_button")
var input_minimum = document.getElementById('input_minimum')
var input_maximum = document.getElementById('input_maximum')
var sorted_filter = document.getElementById("asc_desc")
var filterobj = {}
// var url =  '/test/'
var url = window.location.url

console.log(url)

// min_max_button.onclick = function (event) {
//     input_max_value = input_maximum.value
//     input_min_value = input_minimum.value

//     var query_string = ""
//     var added = false
//     if (input_max_value) {
//         query_string += 'price_max=' + input_max_value;
//         added = true;
//     }
//     if (input_min_value) {
//         if (added) query_string += "&";
//         query_string += 'price_min=' + input_min_value
//         added = true;
//     }
//     var url = new URL(window.location)
//     var params_length = (Array.from(url.searchParams).length)
//     var has_query = params_length > 0 ? true : false
//     if (has_query) {
//         query_string = "&" + query_string
//     } else {
//         query_string = "?" + query_string
//     }
//     if (added) {
//         window.location.href += query_string
//     }
// }

var radio_filter = document.querySelectorAll(".radio_search")
// console.log('radio',radio_filter)
radio_filter.forEach((element)=>{
    element.addEventListener("click",function(){
        // console.log("Radio Element",element)
        var radio_filter_key = element.getAttribute("data-radio-key")
        var radio_filter_value = element.value
        console.log(radio_filter_key,radio_filter_value)
        filterobj[radio_filter_key] = radio_filter_value
        console.log(filterobj)
        
        API();
    })
    

});




function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



var checkboxBtn = document.querySelectorAll(".filter-checkbox, #min_max_button")
// console.log("checkbox",checkboxBtn)

checkboxBtn.forEach((element)=>
{
    
    element.addEventListener("click", function(){
        var key = element.getAttribute("data-key")
        // var value = element.value
        var price_key = input_minimum.getAttribute("data-price-key")
        var min_price = input_minimum.value
        var max_price = input_maximum.value

        filterobj['min_price'] = min_price
        filterobj['max_value'] = max_price

        // console.log(price_key, min_price, max_price)
        // console.log(key,value)

        filterobj[key] = Array.from(document.querySelectorAll('input[data-key="'+key+'"]:checked')).map(function(el){
            return el.value
        })
        // console.log(filterobj)
        API()
        
    });
    // url = "/test/"

});



sorted_filter.addEventListener("click",function(){
sorted_filter.addEventListener("change",function(){
    var value = sorted_filter.options[sorted_filter.selectedIndex].value;
    if(value !== null)
        filterobj["sorted_filter"] = value
        console.log(filterobj)
        API()
});

});








var filteredData = document.querySelector("#filteredData")
function API(){
    console.log(filterobj)

    $.ajax({
        url: url,
        // method: "GET",
        data: filterobj,
        dataType:'json',
        beforeSend:function(){
            console.log("Loading...........")
        },
        success:function(res){
            $("#filteredProducts").html(res.data)
            // filteredData.textContent = `h1>I am Here !!!!!!!!!!!!</h1>`
            // console.log(res);
            
        }
    });
}

