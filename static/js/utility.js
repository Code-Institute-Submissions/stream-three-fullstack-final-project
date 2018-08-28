
// ----- FUNCTIONS AND CLASSES ACCESSIBLE BY ALL TEMPLATES ---- //

// DETECT IF MOBILE BROWSER // 

// USED TO COMBAT ISSUES WITH MOBILE BROWSER AUTO/SHOW HIDE OF URL BAR //
// SHOW/HIDE RESULTS IN JERKY DISPLAY OF FIXED DIVS ON LOGIN AND REGISTER TEMPLATE //

// CREDIT : https://stackoverflow.com/questions/11381673/detecting-a-mobile-browser // 

const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

// ADD BG COLOR TO BODY IN BASE.HTML //

const addBgColorToBody = (_class) => {

    const body = document.getElementsByTagName('body');

    for (let i = 0; i < body.length; i++) {

        body[i].classList.add(_class);

    }
    
}

// ADD/REMOVE CLASS ON CLICK //

const addRemoveClassOnClick = (clickElement, _element, _class) => {

    clickElement.addEventListener('click', () => {

        if (_element.classList.contains(_class)) {

            _element.classList.remove(_class);
    
        } else {
    
            _element.classList.add(_class);
    
        }

    });

}

// USED TO CHANGE THE INNER HTML OF MANAGE TEMPLATES BUTTON ELEMENTS TO 'NOT SURE' ON CLICK //
const insertNotSureOnClick = (clickElement, condition) => {
    
    clickElement.addEventListener('click', function() {
        
        if (this.innerHTML == condition){
            
            this.innerHTML = 'Not Sure';

        } else {

            this.innerHTML = condition;
        }

    });

}


// WILL CHECK TO SEE IF 'NOT SURE' IS ALREADY PART OF THE INNER HTML OF A BUTTON.
// IF IT ISN'T IT WILL SET INNER HTML TO 'NOT SURE'
// IF IT IS, IT WILL SET THE INNER HTML TO THE CONDITION ARGUMENT
const insertNotSureOnOtherButtonClick = (condition, target) => {
    
        if (target.innerHTML == condition){

            target.innerHTML = 'Not Sure';

        } else {
            
            target.innerHTML = condition;
        }

    

}


// ADD CLASS TO HTML COLLECTION // 
const addClassToCollection = (collection, _class) => {

    if (collection instanceof HTMLCollection) {

        for(let i = 0; i < collection.length; i++) {

            collection[i].classList.add(_class);
        }
    }
}

// ADD CLASS ATTRIBUTE TO INDIVIDUAL ELEMENT //
const addClassToElement = (_element, _class) => {

    _element.setAttribute('class', _class);

}


// ADD CLASSNAME TO A CLASSLIST //
const addClassToClassList = (_element, _class) => {

    _element.classList.add(_class);
}

 // ADD CLASSES TO PARENT ELEMENT OF SELECT BOX //
const addStylesToSelectParent = (select, _class) => {

     select.parentElement.setAttribute('class', _class);
    
}


  // INSERT ICON INTO SELECT BOX //
const addIconToSelect = (select, _class) => {

     select.parentElement.insertAdjacentHTML('beforeend',
                         `<i class="fas fa-sort-down ${_class}" aria-hidden="true"></i>`);

}


// ADD REQUIRED ATTRIBUTE TO RENDERED INPUT //
const addRequiredAttribute = (input) => {

    for (let i = 0; i < input.length; i++) {

        input[i].setAttribute('required','true');
    }

}  


    // WRAPS MULTIPLE SELECTS IN A DIV FOR STYLING //
    const wrapSelectsWithDiv = (selects, parentClass, iconClass) => {

        for (let i = 0; i < selects.length; i++) {

            let parent = selects[i].parentElement;
            parent.insertAdjacentHTML('beforeend', '<div></div>');
            parent.lastChild.appendChild(selects[i]);
            addStylesToSelectParent(selects[i], parentClass);
            addIconToSelect(selects[i], iconClass);                                      

        }
}
