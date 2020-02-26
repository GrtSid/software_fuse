$('#post-form').on('submit',function(event){
  console.log("main loaded")
  event.preventDefault();
  console.log("form submitted!")
  create_post();
});
console.log(15);
function create_post(){
  console.log("Create post is working")
  console.log($('#post-form').val())
};
$('#sign').click(function(){
  console.log(115)
  $.ajax({
    url:'/templates/accounts/signup.html',
    type: 'POST',
    datatype: 'json',
    data:$('form#post-form').serialize(),
    success: function(data){
      console.log(json);
      console.log('success');

    }
  })
});