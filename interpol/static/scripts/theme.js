let theme = document.querySelector('.theme');
let html = document.querySelector('html');

document.addEventListener('DOMContentLoaded', ()=>{
    const savedTheme = localStorage.getItem("theme") || "light";

    if(savedTheme == 'dark'){
        html.classList.toggle('dark');
        theme.classList.toggle('dark');
    }

    console.log(savedTheme);

    theme.addEventListener('click',()=>{
        html.classList.toggle('dark');
        theme.classList.toggle('dark');
        if(theme.classList.contains('dark')){
            localStorage.setItem("theme", 'dark');
        }
        else{
            localStorage.setItem("theme", 'light');
        }
    });
});

