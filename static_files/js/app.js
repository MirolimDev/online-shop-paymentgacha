$(document).ready( function (e){
    $('.add_to_cart').on('click', function(e){
        
        e.preventDefault()
        let product_id = $(this).attr('data-id')
        // alert('salom')

        $.ajax({
          
            url:"http://localhost:8000/order/add_to_cart/",
            type: "POST",
            data: {
                product_id: product_id,
                quantity: 1 
            },
            success: function (data){
                $(".cart_html").html(data)
            },
            error: function(data){
                alert('error')
            }
           
        }) 
    })

    

})