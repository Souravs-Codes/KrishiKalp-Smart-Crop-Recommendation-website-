const hero = document.querySelector(".hero");

const spotlight = document.querySelector(".spotlight");

hero.addEventListener("mousemove",(e)=>{

    const rect = hero.getBoundingClientRect();

    const x = e.clientX - rect.left;

    const y = e.clientY - rect.top;

    spotlight.style.setProperty("--x", x + "px");

    spotlight.style.setProperty("--y", y + "px");

});