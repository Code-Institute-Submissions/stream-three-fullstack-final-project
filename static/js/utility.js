
// ----- FUNCTIONS AND CLASSES ACCESIBLE BY ALL TEMPLATES ---- //

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

// USED TO CHANGE THE INNER HTML OF A BUTTON ELEMENTS TO CANCEL ON CLICK //
const insertNotSureOnClick = (clickElement, condition) => {
    
    clickElement.addEventListener('click', function() {
        
        if (this.innerHTML == condition){
            
            this.innerHTML = 'Not Sure';

        } else {

            this.innerHTML = condition;
        }

    });

}

const insertNotSureOnOtherButtonClick = (condition, target) => {

    
        
        if (target.innerHTML == condition){
            console.log('not sure');
            target.innerHTML = 'Not Sure';

        } else {
            console.log('else');
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

const addClassToClassList = (_element, _class) => {

    _element.classList.add(_class);
}

// ADD STYLES AND ICON TO SELECT BOX //

const addStylesToSelectParent = (select, _class) => {

     // ADD CLASSES TO PARENT ELEMENT OF SELECT BOX //
     select.parentElement.setAttribute('class', _class);
    
}

const addIconToSelect = (select, _class) => {

     // INSERT ICON INTo SELECT BOX //
     select.parentElement.insertAdjacentHTML('beforeend',
                         `<i class="fas fa-sort-down ${_class}" aria-hidden="true"></i>`);

}


// ADD REQUIRED ATTRIBUTE TO RENDERED INPUT //
const addRequiredAttribute = (input) => {

    for (let i = 0; i < input.length; i++) {

        input[i].setAttribute('required','true');
    }

}  
