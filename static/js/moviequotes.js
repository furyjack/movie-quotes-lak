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


};

rh.mq.ModelOpenListnen=function()
{


  $("#Insert-Quote-Modal").on("shown.bs.modal",function()
{

$("input[name=quote]").focus();

});


}

$(document).ready(function()

{
 rh.mq.enableButtons();
 rh.mq.ModelOpenListnen();

}


	)