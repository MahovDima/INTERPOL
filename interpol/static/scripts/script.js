const body = document.querySelector('body');
const popups = document.querySelectorAll('.popup-sign');
const header = document.querySelector('header');
const logo = header.querySelector('.logo svg');
const sidebar = document.querySelector('.sidebar');
const age = document.getElementById('age');
const range = document.getElementById('range');
const userMenu = document.querySelectorAll('.user ul');
const messageBox = document.querySelector('.message-box');

const ageChanger = (value) =>{
    age.value = value;
}

const rangeChanger = (value) =>{
    range.value = value;
}

const userMenuOpener = () =>{
    userMenu.forEach(menu => {
        menu.classList.toggle('shown');
    });
}

const openPopup = (evt) =>{
    if(evt.target.classList.contains('signIn')){
        popups.forEach(pop =>{
            pop.classList.contains('signIn-popup') ? pop.classList.add('shown') : {} ;
        })
    }
    else{
        popups.forEach(pop =>{
            pop.classList.contains('signUp-popup') ? pop.classList.add('shown') : {} ;
        })
    }
    sidebar.classList.remove('shown');
}

const closePopup = () =>{
    popups.forEach(pop => {
        pop.classList.remove('shown');
    });
    body.style.position = 'relative';
}

const closeMessage = () =>{
    messageBox.classList.toggle('hidden');
}

const openSidebar = () =>{
    sidebar.classList.add('shown');
    body.style.position = 'fixed'
}

const closeSidebar = (evt) =>{
    if(!evt.target){
        return
    }
    if(evt.target == sidebar){
        if(evt.target.classList.contains('sidebar'))
        sidebar.classList.remove('shown') ;
        body.style.position = 'relative';
    }
}

window.addEventListener('scroll',()=>{
    let posTop = (window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;
    if(posTop > 200){
        header.style.cssText = 'position: fixed; height:80px;'
        logo.style.cssText = 'opacity: 0; width: 0;';
        body.style.cssText = 'padding-top: 130px ;'
    }
    else{
        header.style.cssText = 'position: relative; height:130px;'
        logo.style.cssText = 'opacity: 1; width: auto;';
        body.style.cssText = 'padding-top: 0 ;'
    }
})

window.addEventListener('DOMContentLoaded',()=>{
    
})