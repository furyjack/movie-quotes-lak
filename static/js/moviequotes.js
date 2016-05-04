var rh = rh||{};
rh.mq=rh.mq || {};

rh.mq.editing=false;

rh.mq.enableButtons=function()
{

$("#toggle-edit").click(function()
{
     if (rh.mq.editing)
     {
     	rh.mq.editing=false;
     	$(".edit-actions").addClass("hidden");
     	$(this).html("Edit");

     }
     else
     {
        rh.mq.editing=true;
        $(".edit-actions").removeClass("hidden");
     	$(this).html("Done");
           
     }


});

$("#add-movie-quote").click(function()
{
	   

   $("#Insert-Quote-Modal .modal-title").html("Add Quote");
   $("#Insert-Quote-Modal button[type=submit]").html("Done");

   $("#Insert-Quote-Modal input[name=quote]").val('');
   $("#Insert-Quote-Modal input[name=movie]").val('');
   $("#Insert-Quote-Modal input[name=entity-key]").val('').prop("disabled",true);

});

$(".edit-movie-quote").click(function()
{
	  
   
   $("#Insert-Quote-Modal .modal-title").html("Edit Quote");
   $("#Insert-Quote-Modal button[type=submit]").html("Done");

   quote=$(this).find(".quote").html();
   movie=$(this).find(".movie").html();
   entitykey=$(this).find(".entity-key").html();

   $("#Insert-Quote-Modal input[name=quote]").val(quote);
   $("#Insert-Quote-Modal input[name=movie]").val(movie);
   $("#Insert-Quote-Modal input[name=entity-key]").val(entitykey).prop("disabled",false);

});

$(".del-movie-quote").click(function()
{
	  
   
  

   entitykey=$(this).find(".entity-key-del").html();

   $("#Delete-Quote-Modal input[name=entity-key-del]").val(entitykey).prop("disabled",false);

});


};

rh.mq.ModelOpenListnen=function()
{


  $("#Insert-Quote-Modal").on("shown.bs.modal",function()
{

$("input[name=quote]").focus();

});

rh.mq.initialize_user=function()
{

if( $(".user").html() !="")
{
  $("#Sign-up").addClass("hidden")
  $("#Log-In").addClass("hidden")
  $(".g-signin2").addClass("hidden")
  $("#pser").removeClass("hidden")
  $("#add-movie-quote").removeClass("hidden")
  $("#pser").html("Welcome , " + $(".user").html());
  $("#logout").removeClass("hidden")
  $("#toggle-edit").removeClass("hidden")
}
if( $(".user").html() =="")
{
  $("#Sign-up").removeClass("hidden")
  $("#Log-In").removeClass("hidden")
  $("#pser").addClass("hidden")
  $("#add-movie-quote").addClass("hidden")
  $("#logout").addClass("hidden")
  $("#toggle-edit").addClass("hidden")
  $(".g-signin2").removeClass("hidden")
}
console.log($(".error").html());

if($(".error").html()=="true")
{
   $(".err_msg").removeClass("hidden")
}
if($(".error").html()=="wrong")
{
   $(".err_wrng_msg").removeClass("hidden")
}


};


}
function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  document.cookie = "user="+profile.getName()+";path=/";
  document.cookie = "exist=true;path='/";
   $(".user").html(profile.getName());

  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail());
  console.log($(".user").html());
  $(".error").html("false")
  rh.mq.initialize_user();

}
function logout() {
  
   $(".user").html("");
   document.cookie="user=";
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
    rh.mq.initialize_user();
   

}

$(document).ready(function()

{
 rh.mq.enableButtons();
 rh.mq.ModelOpenListnen();
 rh.mq.initialize_user();
 console.log($(".user").html());

}


	)