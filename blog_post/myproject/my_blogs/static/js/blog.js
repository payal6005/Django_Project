window.onload=function(){

var user= document.querySelector(".userauth")

var modlpopup1=document.querySelector(".modal")
var superu = document.querySelector(".superuser")
console.log(superu)
showpopup = function(){
    if(user.innerText=="True" || superu.innerText=="payalchavda6005@gmail.com"){
        
        modlpopup1.style.display="none"
    }
    else{
        modlpopup1.style.display="block"
    }
}
setTimeout(showpopup,3000)
var delete_button= document.querySelectorAll(".confirmdelete")
var superuser=document.querySelector(".user_is_superuser")
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


console.log(delete_button)

for (let i=0;i<delete_button.length;i++)
{
    delete_button[i].addEventListener("click",e=>{
       e.preventDefault()
       
       bootbox.confirm("Do you want to delete comment?", function(result) {
           if(result){
            let id=delete_button[i].childNodes[1].innerText
            let bid=delete_button[i].childNodes[2].innerText
            var xhr = new XMLHttpRequest();
            xhr.open('POST', `/delete_comments/${id}/${bid}`, true)
            xhr.send()
            
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
        
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/getdislikes/${id}/${dislike_count}`, true)
        xhr.send()
       
    })
}





}



