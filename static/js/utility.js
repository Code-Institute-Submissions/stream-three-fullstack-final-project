
// ----- FUNCTIONS AND CLASSES ACCESIBLE BY ALL TEMPLATES ---- //

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


