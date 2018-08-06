
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


// ADD CLASS TO SELECT BOXES // 

const addClassToSelect = (selectBoxes, _class) => {

    for(let i = 0; i < selectBoxes.length; i++) {

        selectBoxes[i].setAttribute('class', _class);
    }
    

}


