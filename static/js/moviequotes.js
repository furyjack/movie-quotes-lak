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

});

$(".edit-movie-quote").click(function()
{
	  
   
   $("#Insert-Quote-Modal .modal-title").html("Edit Quote");
   $("#Insert-Quote-Modal button[type=submit]").html("Done");

});


};

rh.mq.ModelOpenListnen=function()
{


  $("#Insert-Quote-Modal").on("shown.bs.modal",function()
{
	
$("input[name='quote']").focus();

});


}

$(document).ready(function()

{
 rh.mq.enableButtons();
 rh.mq.ModelOpenListnen();

}


	)