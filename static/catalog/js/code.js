var nav = document.getElementById('.nav');

window.addEventListener('scrooll', ()=> {

    var scroll = window.scrollY

    if (scroll>10){
        nav.style.backgroundColor = '#fff'
    } else{
        nav.style.backgroundColor = 'transparent'
    }
})