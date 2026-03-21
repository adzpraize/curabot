function addMessage(text,type){

let box=document.getElementById("chat-box")

let msg=document.createElement("div")

msg.className="message "+type

msg.innerText=text

box.appendChild(msg)

box.scrollTop=box.scrollHeight

}

function sendMessage(){

let input=document.getElementById("msg")

let text=input.value

if(text===""){

Swal.fire({

toast:true,

position:"top-end",

icon:"warning",

title:"Type a message",

showConfirmButton:false,

timer:2000

})

return

}

addMessage(text,"user")

fetch("/get",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({message:text})

})

.then(res=>res.json())

.then(data=>{

addMessage(data.reply,"bot")

})

input.value=""

}