// LOGIN TEMPLATE RELATED JS //

(() => {

    // FUNCTION ROTATES ARROW ICON WHEN SCROLLING //
    const body =  document.getElementsByTagName('body');
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

   //console.log(body);
    let bodyHeight = (0.9 * $(window).height());
   
    bodyHeight = `${bodyHeight}` + 'px';
    for ( let i = 0; i < body.lenght; i++ ) {

        body[i].setAttribute('style', `height:${bodyHeight}`)

    }
    
    rotateUpArrowOnScrollDown();

})();
