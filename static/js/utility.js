
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

// USED TO CHANGE THE INNER HTML OF AN ELEMENT ON CLICK //
const insertHTMLonClick = (clickElement, condition, html) => {

    clickElement.addEventListener('click', function() {

        if (this.innerHTML == condition){
            
            this.innerHTML = 'Cancel';

        } else {

            this.innerHTML = condition;
        }

    });

}


// ADD CLASS TO HTML COLLECTION OR INDIVIDUAL ELEMENT // 

const addClassToCollection = (collection, _class) => {

    if (collection instanceof HTMLCollection) {

        for(let i = 0; i < collection.length; i++) {

            collection[i].setAttribute('class', _class);
        }

    } else {

        collection.setAttribute('class', _class);
    }
 
}


