$(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/create',
      data:{
        link:$('#link').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        rng:$('input[name=rng]').val(),
      },
      success: function(data){
        $('h2').html("http://s-sh.fun/"+data)
      }
    });
  });
