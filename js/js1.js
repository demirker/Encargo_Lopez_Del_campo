$(document).ready(function(){
    $('.item_categoria').click(function(){
        var catProduct = $(this).attr('category');
        console.log(catProduct);

        $('.item_producto').hide();

        $('.item_producto[category="'+catProduct+'"]').show();

    });

    $('.item_categoria[category="all"]').click(function(){
        $('.item_producto').show();

    });

});