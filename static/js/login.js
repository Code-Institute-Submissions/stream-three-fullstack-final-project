// LOGIN TEMPLATE RELATED JS //

(() => {

    const landingContainer = document.getElementById('landing-container');
    const loginBlurbContainer = document.getElementById('login-blurb');
    const upArrow = document.getElementById("up-arrow");
    const downArrow = document.getElementById("down-arrow");
  
   
    // FUNCTION ROTATES ARROW ICON WHEN SCROLLING //
    
    const rotateUpArrowOnScrollDown = () => {

        window.addEventListener('scroll', () => {

            if (window.scrollY > (upArrow.offsetTop + upArrow.offsetHeight)) {
        
                upArrow.classList.add('scroll-up--show');
                downArrow.classList.add('scroll-down--hide');
               
            } else if (window.scrollY < (upArrow.offsetTop + upArrow.offsetHeight)) {
        
                upArrow.classList.remove('scroll-up--show');
                downArrow.classList.remove('scroll-down--hide');
                 
            } 
        });

    }
      
    // SET FIXED HEIGHTS ON 100% CENTRALLY ALIGNED FIXED FLEX ELEMENT TO FIX JERKING ON SCROLL //
    // LISTEN FOR ORIENTATION CHANGE TO RECALCULATE DIV HEIGHT //
    const orientationValue = () => {
        
        window.addEventListener('orientationchange', () => {

            let value = window.orientation;
           
            if (value == 0) {

                landingContainer.setAttribute('style', `height: ${(window.innerHeight).toString() + 'px'};` );
                loginBlurbContainer.setAttribute('style', `height: ${(window.innerHeight + 60).toString() + 'px'};`);

            } else if ( value != 0) {

                landingContainer.setAttribute('style', `height: ${(window.innerHeight).toString() + 'px'};`);
                loginBlurbContainer.removeAttribute('style');

            }

        })
    }
   
    // FUNCTION CALLS  //

    rotateUpArrowOnScrollDown();

    // DETECT IF MOBILE BROWSER // 

    // RUN FUNCTION BELOW IF TRUE. FUNCTION COMBATES ISSUES WITH MOBILE BROWSER AUTO/SHOW HIDE OF URL BAR //
    // AND THE JERKY DISPLAY OF FIXED DIVS //

    // CREDIT : https://stackoverflow.com/questions/11381673/detecting-a-mobile-browser // 

    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if (isMobile) {
        landingContainer.setAttribute('style', `height: ${(window.innerHeight).toString() + 'px'};` );
        loginBlurbContainer.setAttribute('style', `height: ${(window.innerHeight + 60).toString() + 'px'};`);
        orientationValue();
    }
   

})();
