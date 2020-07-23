window.onload=function(){

var user= document.querySelector(".userauth")

var modlpopup1=document.querySelector("#loginpopup")
var superu = document.querySelector(".super_user")
let userid=document.querySelector(".userid")
var userid1=parseInt(userid.innerText)


if(document.querySelector(".blogidw"))
{
var blogidw=document.querySelector(".blogidw").innerText
}

// var whatsupurl=`https://web.whatsapp.com/send?text=https://blogpost2020.herokuapp.com/detailofblog/${blogidw}`
// console.log(whatsupurl)
$('[data-toggle="popover"]').popover({  
    html: true,
    trigger: 'click',
    content : `<div class="media" style="margin-top:2px;"><a href="https://web.whatsapp.com/send?text=${window.location.href}" target="_blank"  class="pull-left whatsapbutton"><img src="../static/images/WhatsApp.png" style="width:50px;height:30px;padding-right:15px;" alt="Sample Image"></a>
    <a href=http://www.facebook.com/sharer/sharer.php?u=${window.location.href} target="_blank" class="pull-left whatsapbutton"><img src="../static/images/facebook.png" style="width:50px;height:30px;padding-right:15px;" alt="Sample Image"></a>
    <a href=http://www.linkedin.com/shareArticle?url=${window.location.href} target="_blank" class="pull-left whatsapbutton"><img src="../static/images/linkedin1.png" style="width:50px;height:30px;padding-right:15px;" alt="Sample Image"></a>
    <a href=https://twitter.com/share?url=${window.location.href} target="_blank"  class="pull-left whatsapbutton"><img src="../static/images/twitter.jpg" style="width:30px;height:30px;" alt="Sample Image"></a></div></div>`
    });  
    if(superu.innerText=="True"){
    $('#btnPopover').popover({
        
        placement: 'bottom',
        container: 'body',
        html: true,
        trigger: 'click',
        content:'<div><ul style="list-style: none;padding:0px 0;margin:0;"><li style="padding:0px 22px;"><a type="submit" href="/approveblogs/"  style="line-height:22px;padding:0 24px;font-family: PT Sans, sans-serif;color:gray;"><img src="https://blogpost1837.herokuapp.com/static/images/dashboard.png" style="width:13px;height:13px;"/> Blog Requests</a></li><li style="border-bottom: 1px solid #e9ebee;padding:5px 7px 10px;padding-top:1px;"></li><li style="padding:0px 22px;"><a type="submit" href="#" class="logoutbtn" style="padding:5px 50px 10px;font-family: PT Sans, sans-serif;color:gray; " onclick="logoutfunction()"><img src="https://blogpost1837.herokuapp.com/static/images/logout1.png" style="width:13px;height:13px;"/> Logout</a></li></ul></div>'
    
    });
}
else{
    $('#btnPopover').popover({
        
        placement: 'bottom',
        container: 'body',
        html: true,
        trigger: 'click',
        content:`<ul style="list-style: none;padding:0px 0;margin:0;"><li style="padding:0px 22px;"><a type="submit" href="#"  style="line-height:22px;padding:0 34px;font-family: PT Sans, sans-serif;color:gray;" onclick="popup1()"><img src="https://blogpost1837.herokuapp.com/static/images/plus.png" style="width:13px;height:13px;"/> Submit Post</a></li><li style="border-bottom: 1px solid #e9ebee;padding:5px 7px 10px;padding-top:1px;"></li><li style="padding:0px 22px;"><a type="submit"  href=/myposts/${userid1}   style="line-height:22px;padding:0 38px;font-family: PT Sans, sans-serif;color:gray;"><img src="https://blogpost1837.herokuapp.com/static/images/post.png" style="width:13px;height:13px;"/> My Post</a></li><li style="border-bottom: 1px solid #e9ebee;padding:5px 7px 10px;padding-top:1px;"></li><li style="padding:0px 22px;"><a type="submit" href="#" class="logoutbtn" style="padding:5px 39px 10px;font-family: PT Sans, sans-serif;color:gray;" onclick="logoutfunction()"><img src="https://blogpost1837.herokuapp.com/static/images/logout1.png" style="width:13px;height:13px;"/> Logout</a></li></ul></div>`
    
    });
}



logoutfunction =function (){
   
    console.log("logout")
    var xhr = new XMLHttpRequest();
        xhr.open('GET', `/logoutt`, true)
        xhr.send()
        showpopupforlogout()
        location.reload()
       
      
       
}
requestforblog=function(e){
    
    var xhr = new XMLHttpRequest();
    xhr.open('GET', `/approveblogs`, true)
   
    xhr.send()
  
   
}

popup1=function(){
    $('#blogcontentModal').modal({backdrop: 'static', keyboard: false})
    $("#blogcontentModal").modal('show')
    $('#btnPopover').popover('hide')
   
}
var btns = document.getElementsByClassName("firstnav");
    for (var i = 0; i < btns.length; i++) {
    
      btns[i].addEventListener("click", function(e) {
     
      var current = document.getElementsByClassName("active");
      current[0].className = current[0].className.replace(" active", "");
      this.className += " active";
      });
    }
    showpopupforlogout = function(){
        if(user.innerText=="True"){
            $("#loginpopup").modal('hide')
        }
        else{
            $('#loginpopup').modal({backdrop: 'static', keyboard: false})
            $("#loginpopup").modal('show')
           
           
        }
    }
showpopup = function(){
    if(user.innerText=="True"){
        $("#loginpopup").modal('hide')
    }
    else{
        $('#loginpopup').modal({backdrop: 'static', keyboard: false})
        $("#loginpopup").modal('show')
       
       
    }
}
setTimeout(showpopup,3000)
var delete_button= document.querySelectorAll(".confirmdelete")
var superuser=document.querySelector(".user_is_superuser")
if(superuser!=null)
{
if(superuser.innerText=="True")
{
    for (let i=0;i<delete_button.length;i++)
 {
    delete_button[i].style.display="block"
 }


}
else
{
    for (let i=0;i<delete_button.length;i++)
    {
       delete_button[i].style.display="none"
    }
}
}




for (let i=0;i<delete_button.length;i++)
{
    delete_button[i].addEventListener("click",e=>{
       e.preventDefault()
       
       bootbox.confirm("Do you want to delete comment?", function(result) {
           if(result){
            let id=delete_button[i].childNodes[1].innerText
            let bid=delete_button[i].childNodes[2].innerText
            var xhr = new XMLHttpRequest();
            // xhr.open('POST', `/delete_comments/${id}/${bid}`, true)
            // xhr.send()
           
            fetch(`/delete_comments/${id}/${bid}`,{
                method:'post'
            })
            .then((response) => {
                location.reload()
            
                
           }).catch((error)=>{

           }
           )
           
        }
})
})
}


var elements= document.querySelectorAll("#lb")


var dislikes_button= document.querySelectorAll("#ld")

var comments=document.querySelectorAll(".comments")
var post=document.querySelectorAll(".post")
var blogtitle=document.querySelectorAll(".tag")

var commentblog= document.querySelector("#commentsonblog")




for (let i=0;i<elements.length;i++)
{
    elements[i].addEventListener("click",e=>{
       e.preventDefault()
       console.log(elements[i].childNodes[1].innerText)
       let id=elements[i].childNodes[1].innerText
        
        let like_count=parseInt(elements[i].innerText)+1
        
        elements[i].innerText=like_count
        
       
       
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/getlikes/${id}/${like_count}`, true)
        xhr.send()
       
    })
}

for (let i=0;i<dislikes_button.length;i++)
{
    dislikes_button[i].addEventListener("click",e=>{
       e.preventDefault()
        let id=dislikes_button[i].childNodes[1].innerText
        
       
        let dislike_count=parseInt(dislikes_button[i].innerText)+1

        dislikes_button[i].innerText=dislike_count
        param={"id":id,"dislike_count":dislike_count}
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/getdislikes/${id}/${dislike_count}`, true)
        xhr.send()
       
    })
}

var btnrequestedit=document.querySelectorAll(".blogrequestbutton")

var id2=document.querySelectorAll(".idd")
var fn=document.querySelectorAll(".fname")

var ln=document.querySelectorAll(".lname")
var em=document.querySelectorAll(".emaill")
var mo=document.querySelectorAll(".mobile")
var ti=document.querySelectorAll(".title")
var de=document.querySelectorAll(".detail")
var ca=document.querySelectorAll(".category")
var im=document.querySelectorAll(".image1")

let id3=0
var image
console.log(btnrequestedit)
for (let i1=0;i1<btnrequestedit.length;i1++){
    if(btnrequestedit[i1].innerText=="Request For Edit Blog")
    {
    btnrequestedit[i1].addEventListener("click",e=>{
    e.preventDefault()
    document.querySelector(".firstname").value=fn[i1].outerText
    document.querySelector(".lastname").value=ln[i1].innerText
    document.querySelector(".email").value=em[i1].innerText
    document.querySelector(".mobileno").value=mo[i1].innerText
    document.querySelector(".title1").value=ti[i1].innerText
    document.querySelector(".blogdetail").value=de[i1].innerText
    document.querySelector(".categoryname").value=ca[i1].innerText
    image=im[i1].innerText
    id3=parseInt(id2[i1].innerText)
    
    $('#blogrequestmodal').modal({backdrop: 'static', keyboard: false})
    $("#blogrequestmodal").modal('show')
   
   
})
    }
}

var youtubelink= document.querySelector(".youtubelink")
var imagefile= document.querySelector(".imagefile11")
imagefile.style.display="block"
youtubelink.style.display="none"
uploadyoutube= function(){

    $(".youtubelink").show()
    $(".imagefile11").hide()
   
   
   
}
uploadimage= function(){

    $(".imagefile11").show()
    $(".youtubelink").hide()
 
}





var edit=document.querySelectorAll(".edit")
for (let i1=0;i1<edit.length;i1++){
    edit[i1].addEventListener("click",e=>{
       
     
       document.getElementById('form_id').action = `/editblogcontent/${id3}/${userid1}`;
  
    })
}


   


var youtubelink1= document.querySelectorAll(".youtubelink1")
var imagefilerequest= document.querySelectorAll(".imagefilerequest")
var uploadyoutubeedit=document.querySelectorAll(".uploadyoutubeedit")
var uploadimageedit=document.querySelectorAll(".uploadimageedit")
youtubelink1[0].style.display="none"
imagefilerequest[0].style.display="block"


for(let u=0;u<uploadyoutubeedit.length;u++)
{

   uploadyoutubeedit[u].addEventListener("click",function(e){
    e.preventDefault()
    youtubelink1[u].style.display="block"
    imagefilerequest[u].style.display="none"
   })
    
 

}
for(let u=0;u<uploadimageedit.length;u++)
{

    uploadimageedit[u].addEventListener("click",function(e){
    e.preventDefault()
    youtubelink1[u].style.display="none"
    imagefilerequest[u].style.display="block"
   })
    
 

}


 
    





}




