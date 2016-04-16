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

};

$(document).ready(function()

{
 rh.mq.enableButtons();

}


	)