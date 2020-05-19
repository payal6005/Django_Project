window.onload=function(){

var user= document.querySelector(".userauth")

var modlpopup1=document.querySelector(".modal")

if(user.innerText=="False"){

    // console.log("payal")
    modlpopup1.style.display="block"


}
else{
    modlpopup1.style.display="none"
}


var elements= document.querySelectorAll("#lb")


var dislikes_button= document.querySelectorAll("#ld")




for (let i=0;i<elements.length;i++)
{
    elements[i].addEventListener("click",e=>{
        
       let id=elements[i].childNodes[1].innerText
        
        let l=elements[i].innerText
       
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/getlikes/${id}/${l}`, true)
        xhr.send()
       
    })
}

for (let i=0;i<dislikes_button.length;i++)
{
    dislikes_button[i].addEventListener("click",e=>{
        
        let id=dislikes_button[i].childNodes[1].innerText
        
        let l=dislikes_button[i].innerText
        
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/getdislikes/${id}/${l}`, true)
        xhr.send()
       
    })
}




}



