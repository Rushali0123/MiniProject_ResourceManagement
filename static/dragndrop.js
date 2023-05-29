function allowDrop(event) {
    event.preventDefault();
}
function drop(event) {
    event.preventDefault();
    var product_id = event.dataTransfer.getData("text/plain");
    console.log(product_id)
    window.location.href=`assigned/${product_id}`
}
function allowDropbill(event) {
    event.preventDefault();
}
function dropbill(event) {
    event.preventDefault();
    var product_id = event.dataTransfer.getData("text/plain");
    window.location.href=`billable/${product_id}`
}
function allowDropAvailable(event) {
    event.preventDefault();
}
function dropAvailable(event) {
    event.preventDefault();
    var product_id = event.dataTransfer.getData("text/plain");
    window.location.href=`billable-remove/${product_id}`
}
var products = document.querySelectorAll('.product');
products.forEach(function(product) {
    product.addEventListener('dragstart', function(event)
    {
        event.dataTransfer.setData("text/plain", event.target.id);
    });
});