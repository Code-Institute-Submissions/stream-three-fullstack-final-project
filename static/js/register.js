// REGISTER TEMPLATE JS //

(() => { 

    const explain = document.getElementById("explain");
    const explainText = document.getElementById("explain-text");
    const stepOne = document.getElementById("step-one");
    const stepTwo = document.getElementById("step-two");
    const stepThree = document.getElementById("step-three");
    const explainArray = [stepOne, stepTwo, stepThree, explain]
    const initialFixHeight = (window.innerHeight + 80).toString();
    

    // FIX EXPLAIN DIV HEIGHTS ON MOBILE DEVICES TO COMBAT FIXED //
    // POSITION BUG WITH SHOW/HIDE OF URL BAR // 

    const fixExplainDivHeight = (fixHeight) => {

        for (let i = 0; i < explainArray.length; i++) {

            explainArray[i].style.height = fixHeight + 'px';
        }

    }

    // OFFSET THE POSITION OF EXPLAIN TEXT BY 80 PX //
    // TO ACCOUNT FOR FIXES HEIGHT ON MOBILE //

    const shiftPositionOfExplainText = () => {

        explainText.style.position = 'relative';
        explainText.style.top = '-40px';
    }

    // SET EXPLAIN DIV POSITION BASED ON NEW HEIGHT VALUES //

    const setExplainDivPosition = (fixHeight) => {

        for (let i = 0; i <= 2; i++) {
            
            explainArray[i].style.top = (fixHeight * (i + 1)) + 'px';
        
        }

    }

    // CALL ABOVE FUNCTIONS ON ORIENTATION CHANGE //

    const setExplainOnOrientation = () => {

        window.addEventListener('orientationchange', () => {

            let orientationFixHeight = (window.innerHeight + 80).toString();
           
            fixExplainDivHeight(orientationFixHeight);
            setExplainDivPosition(orientationFixHeight);
         
        })

    }
   
    // CHANGES GIVEN DIV TO FIXED BASED ON TOP POSITION //

    const setDivToFixed = (div, class1, class2) => {

        window.addEventListener('scroll', () => {

            if (window.scrollY > div.offsetTop) {
                
                div.classList.add(class1);
        
            } else if (window.scrollY == div.offsetTop) {

                setTimeout(() => {

                    div.classList.remove(class2);
                    div.classList.remove(class1);

                }, 450);
            }
        });
    }

    // CHANGES FIXED DIV TEXT BASED ON TOP SCROLL POSITION OF RELATIVE DIVS //

    const changeFixedDivTextOnScroll = () => {

        window.addEventListener('scroll', () => {

            if(window.scrollY > stepOne.offsetTop) {
                
                explainText.innerHTML = 'Why make things difficult?';

            } else if(window.scrollY < stepTwo.offsetTop){

                explainText.innerHTML = 'Let Us Explain.';
            }
            
            if(window.scrollY > stepTwo.offsetTop){

                explainText.innerHTML="When it's this simple.";

            } 
        });
    }

 

    // FUNCTION CALLS //

    // DETECT MOBILE BROWSER //

    if (isMobile) {

        fixExplainDivHeight(initialFixHeight);
        setExplainDivPosition(initialFixHeight);
        shiftPositionOfExplainText();
        setExplainOnOrientation();
    }

    setDivToFixed(explain, "container--fixed", 
                            "container--fixed-100");
    changeFixedDivTextOnScroll();
    addBgColorToBody('body-color');
    

})();