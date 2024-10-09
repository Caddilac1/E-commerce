
//getting all buttons
var updateBtns = document.getElementsByClassName('update-cart');
console.log("updateBtns",updateBtns);

for(let i=0; i< updateBtns.length; i++){
    console.log("Button:", updateBtns[i]);

    updateBtns[i].addEventListener('click',function(){
        alert("button clicked");
        console.log("Button clicked!");
        console.log("Button:", this);

        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log("ProductId",productId);
        console.log("Action",action);

    if(user == 'AnonymousUser'){
        console.log("Not logged in")
    }
    else{
        console.log("User is logged in sending data...");
    }
    })
}

