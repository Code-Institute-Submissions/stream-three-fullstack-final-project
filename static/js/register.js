// REGISTER TEMPLATE JS //

(() => { 

    const explain = document.getElementById("explain");
    const explainText = document.getElementById("explain-text");
    const stepOne = document.getElementById("step-one");
    const stepTwo = document.getElementById("step-two");
    
    // CHANGES GIVEN DIV TO FIXED BASED ON TOP POSITION //
    const setDivToFixed = (div, class1, class2) => {

        window.addEventListener('scroll', () => {

            if (window.scrollY > div.offsetTop) {
                
                div.classList.add(class1);
        
            } else if (window.scrollY == div.offsetTop) {

                div.classList.add(class2);

                setTimeout(() => {

                    div.classList.remove(class2);
                    div.classList.remove(class1);

                }, 450);
            }
        });
    }

    // CHANGES FIXED DIV TEXT BASED ON TOP POSITION OF RELATIVE DIVS //
    const changeFixedDivText = () => {

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

    setDivToFixed(explain, "container--fixed", 
                            "container--fixed-100");
    
    changeFixedDivText();
    addBgColorToBody('body-color');
    

})();