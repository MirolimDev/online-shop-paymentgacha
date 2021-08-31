$(document).ready(function(s){

    $(document).on('click', '.delete_from_cart',function(s){
        

        let id = $(this).attr('data_id')
        alert(id + '  salom ')  
  
        $.ajax({

            url: "http://localhost:8000/order/delete_from_cart/",
            type: "POST",
            data: {
                product_id: id,
            },
            success: function(html){
                $('#table_body').html(html)
            },
            error: function(html){
                alert('error')
            }
        })
    })

    $(document).on('click', '.delete', function(s){
        

        let id1 = $(this).attr('data_id1')
        alert(id1 +   '  salom ')  
  
        $.ajax({

            url:"http://localhost:8000/order/delete_cart/",
            type: "POST",
            data: {
                product_id: id1,
            },
            success: function(html){
                $('.cart_html').html(html)
            },
            error: function(html){
                alert('error')
            }
        })
    })

})