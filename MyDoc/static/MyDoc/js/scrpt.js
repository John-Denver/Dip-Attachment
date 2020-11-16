 /*
      signUp.addEventListener("click", () => {
        signUp.classList.add("right-panel-active")
   })
  
   signIn.addEventListener("click", () => {
        signUp.classList.remove("right-panel-active")
   })
 */
   
document.addEventListener("mousemove", function(e){

    const bg = document.querySelector('.bg');
    const bird = document.querySelector('.bid');
    const content = document.querySelector('.content');

    bg.style.width = 100 + e.pageX/100 + '%';
    bg.style.height = 100 + e.pageX/100 + '%';

    bird.style.right = 100 + e.pageX/2 + 'px';

    content.style.left = 100 + e.pageX/2.5 + 'px'
})

 var prevScrollpos = window.pageXOffset;
        window.onscroll = function(){

        if(prevScrollpos > 30){
            document.getElementById("navbar").style.top = "0";
        }else{
            document.getElementById("navbar").style.top = "0";
        }

    }

var modal=document.getElementById('id01');

//when user clicks outside modal close it
window.onclick=function(event){
    if(event.target==modal){
        modal.style.display="none";
    }
}

//m0dal t0 make an app0ntment cl0se and 0pen;
  function openForm(){
    document.getElementById("myOverlay").style.display="block"; 
       
  }

window.onclick=function lgn() {
    document.getElementById('signIn');
    setTimeout(
        Window.open("sign-in.html"), 3000
    );
}

function closeForm(){
document.getElementById("myOverlay").style.display="none";

}

  window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    document.body.style.overflow = "auto"; // ADD THIS LINE
    document.body.style.height = "auto";  // ADD THIS LINE
  }
}

 