const body = document.querySelector('body');
const popups = document.querySelectorAll('.popup-sign');
const header = document.querySelector('header');
const logo = header.querySelector('.logo svg');
const sidebar = document.querySelector('.sidebar');
const age = document.getElementById('age');
const range = document.getElementById('range');
const userMenu = document.querySelectorAll('.user ul');
const messageBox = document.querySelector('.message-box');
const password1 = document.getElementById('signup_password1');
const password2 = document.getElementById('signup_password2');
const wantedList = document.querySelectorAll('.wanted-item');
const wantedAddForm = document.querySelector('.wanted-add-content');
const loadScreen = document.querySelector('.loading');
const commentsBtn = document.querySelectorAll('.comments button');

commentsBtn.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        btn.parentNode.classList.toggle('showed');
    });
});



window.addEventListener('scroll',()=>{
    console.log(window.pageYOffset)
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
    body.classList.add('fixed');
}

const closePopup = () =>{
    popups.forEach(pop => {
        pop.classList.remove('shown');
    });
    body.classList.remove('fixed');
}

validationReset = () =>{
    password1.classList.remove('wrong')
    password2.classList.remove('wrong')
    document.querySelector('.signUp-popup form p').textContent = '';
}

const signup = (btn) =>{
    if(password1.value != password2.value){
        document.querySelector('.signUp-popup form p').textContent = 'Пароли не совпадают';
        password1.classList.remove('wrong');
        password2.classList.remove('wrong');
        password1.classList.add('wrong');
        password2.classList.add('wrong');
    }
    else{
        btn.parentNode.submit();
    }
}

wantedList.forEach(wanted => {
    wanted.addEventListener('click', (evt)=>{
        if(!evt.target.classList.contains('close-button')){
            wanted.classList.add('popup')
            body.classList.add('fixed');
        }
    })
});

const wantedAdd = (evt) =>{
        evt.target.classList.toggle('shown');
        wantedAddForm.classList.toggle('shown');
}

const closeWantedPopup = (evt) =>{
    evt.target.parentNode.parentNode.classList.remove('popup');
    body.classList.remove('fixed');
}

const openSidebar = () =>{
    sidebar.classList.add('shown');
    body.classList.add('fixed');
}

const closeSidebar = (evt) =>{
    if(!evt.target){
        return
    }
    if(evt.target == sidebar){
        if(evt.target.classList.contains('sidebar'))
        sidebar.classList.remove('shown') ;
        body.classList.remove('fixed');
    }
}



window.addEventListener('DOMContentLoaded', ()=>{

    setTimeout(()=>{
        if(loadScreen){
            loadScreen.classList.add('hidden');
        }

    }, 100);
});


