console.log("Sammykeys Official is in");

//getting all buttons

var updatebuttons = document.getElementsByClassName('update-cart');
console.log(updatebuttons);

for(var i = 0; i < updatebuttons; i++){
updatebuttons[i].addEventListener('click',function(){
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId",productId);
    console.log("Action",action);
})
}

