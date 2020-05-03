console.log

$(document).ready(function(){

    //hide images:
    $('img').click(function(){
        $(this).hide();
    });

    //restore button:
    $('#btn').click(function(){
        $('img').show();
    });
});
