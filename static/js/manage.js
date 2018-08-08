(() => {



    const manageClientInput = document.getElementsByClassName('register-form__input');


    // ADD REQUIRED ATTR TO RENDERED INPUT //
    for (i = 0; i < manageClientInput.length; i++) {

        manageClientInput[i].setAttribute('required','true');
    }

    
})();