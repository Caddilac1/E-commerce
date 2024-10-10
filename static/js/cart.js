

var updatebuttons = document.getElementsByClassName('update-cart');
console.log(updatebuttons); // This will log an HTMLCollection

for ( var i = 0; i < updatebuttons.length; i++) {
    updatebuttons[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log("ProductId:", productId , "Action:", action)
    });
}

