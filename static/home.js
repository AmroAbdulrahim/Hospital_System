let register = document.getElementsByClassName("registered")
let patient = document.getElementsByClassName("new-patient")
let info = document.getElementsByClassName("info")
let exit = document.getElementsByClassName("exit")

register[0].onclick = function(){
    window.location.href="/patient"
}
patient[0].onclick = function(){
    window.location.href="/register"
}
info[0].onclick = function(){
    window.location.href="/info"
}
exit[0].onclick = function(){
    window.location.href="/"
}