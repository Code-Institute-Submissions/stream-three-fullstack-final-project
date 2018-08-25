// LOGIN TEMPLATE RELATED JS //

(() => {

    const landingContainer = document.getElementById('landing-container');
    // FUNCTION ROTATES ARROW ICON WHEN SCROLLING //
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

    let lastHeight = '';
    $(window).on('resize', function () {

        if (lastHeight) {

            $('#landing-container').height(lastHeight = '');
        }
    }).on('touchmove', function () {

        if (lastHeight != window.innerHeight) {

            $('#landing-container').height(lastHeight = window.innerHeight);
        }
    })

    rotateUpArrowOnScrollDown();

})();
