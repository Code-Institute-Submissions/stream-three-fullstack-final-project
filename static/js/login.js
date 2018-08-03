
(() => {

    
    // FUNCTION ROTATES ARROWS WHEN SCROLLING //
    const rotateUpArrowOnScrollDown = () => {

        window.addEventListener('scroll', () => {

            const upArrow = document.getElementById("up-arrow");
            const downArrow = document.getElementById("down-arrow");

            if (window.scrollY > (upArrow.offsetTop + upArrow.offsetHeight)) {
        
                upArrow.classList.add('scroll-up--show');
                downArrow.classList.add('scroll-down--hide');
               
                
            } else if (window.scrollY < (upArrow.offsetTop + upArrow.offsetHeight)) {
        
                upArrow.classList.remove('scroll-up--show');
                downArrow.classList.remove('scroll-down--hide');
                
               
                
            } 
        });

    }

   
    rotateUpArrowOnScrollDown();

})();
