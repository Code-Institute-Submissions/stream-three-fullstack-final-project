
// ----- FUNCTIONS AND CLASSES ACCESIBLE BY ALL TEMPLATES ---- //

const addBgColorToBody = (_class) => {

    const body = document.getElementsByTagName('body');

    for (let i = 0; i < body.length; i++) {

        body[i].classList.add('body-color');

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
const insertCancelOnClick = (clickElement, condition) => {

    clickElement.addEventListener('click', function() {
        
        if (this.innerHTML == condition){
            
            this.innerHTML = 'Cancel';

        } else {

            this.innerHTML = condition;
        }

    });

}


// ADD CLASS TO HTML COLLECTION // 

const addClassToCollection = (collection, _class) => {

    
    if (collection instanceof HTMLCollection) {

        for(let i = 0; i < collection.length; i++) {

            collection[i].classList.add(_class);
        }
    }
}

// ADD CLASS TO ATTRIBUTE TO INDIVIDUAL ELEMENT //
const addClassToElement = (_element, _class) => {

    _element.setAttribute('class', _class);

}

// ADD STYLES AND ICON TO SELECT BOX //

const addStylesToSelectParent = (select, _class) => {

    console.log('here');
     // ADD CLASSES TO PARENT ELEMENT OF SELECT BOX //
     select.parentElement.setAttribute('class', _class);
    
     // INSERT ICON INOT SELECT BOX //
     select.parentElement.insertAdjacentHTML('beforeend',
                         '<i class="fas fa-sort-down profile-filter-arrow" aria-hidden="true"></i>');
}
