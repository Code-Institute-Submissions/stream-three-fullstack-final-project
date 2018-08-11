// CYCLE PORTHOLE JS //

(() => {

    const nav = document.getElementById('nav');
    const input = document.getElementsByTagName('input');
    const selects = document.getElementsByTagName('select');
    const valueInput = document.getElementById('id_cycle_value_0');
    const browseButtons = document.getElementsByClassName('upload-form__browse-button');
    


    // GET INPUTS BY FILE INPUT TYPE //
    const getFileInput = (input) => {

        fileInputs = []

        for (let i = 0; i < input.length; i++){ 

            if (input[i].getAttribute('type') == 'file') {

                fileInputs.push(input[i]);

            }
        }
       
        return fileInputs;

    }


    // SWITCH OUT FILE INPUT ID'S FOR INDIVUAL STYLING //
    const replaceFileInputId = (fileInput) => {

        for (i = 0; i < fileInput.length; i++) {

            fileInput[i].setAttribute('id', `upload-${i}`);
        }
    }

    // HIDE UPLOAD FIELDS TO REPLACE WITH CUSTOM STYLED UPLOAD FIELDS //

    const hideUploadFields = (uploadFields) => {
       

        for (i = 0; i < uploadFields.length; i++) {

            uploadFields[i].style.display='none';
        }
    }


    // HIDE CURRENCY DROP DOWN LIST //
    const hideSelects = (selects) => {

        for (i = 0; i < selects.length; i++) {

            selects[i].style.display = 'none';
        }
    }

    // ADD PLACEHOLDER TO INPUT VALUE // 
    const addPlaceHolderToValueInput = () => {

        valueInput.setAttribute('placeholder', 'Enter cycle value')
    }

     // TRIGGER HIDDEN UNSTYLED BROWSE BUTTON ON CLICK OF STYLED BUTTON //
    const onBrowseButtonClickTriggerHiddenButton = (browseButtons) => {
        //console.log(browseButtons);
        for (i = 0; i < browseButtons.length; i++) {

            browseButtons[i].addEventListener('click', () => {

                document.getElementById(`upload-${i}`).click();

            });
        }

    }

    //----------------------------- FUNCTION CALLS ------------------------// 

    // REPLACE ID OF INPUT OF TYPE=FILE // 
    const fileInput = getFileInput(input);
    replaceFileInputId(fileInput);

    // GET THE ELEMENTS WITH REPLACED ID'S //
    const quoteUpload = document.getElementById('upload-0');
    const poUpload = document.getElementById('upload-1');
    const invoiceUpload = document.getElementById('upload-2');
    const uploadFields = [quoteUpload, poUpload, invoiceUpload];

    // HIDE THOSE ELEMENTS // 
    hideUploadFields(uploadFields);

    for(let  i =0; i < uploadFields.length; i++) {

        uploadFields[i].onchange = function() {

            console.log(this.value);
        }
    }

    // TRIGGER HIDDEN DJANGO GENERATED FORM BROWSE BUTTON //
    onBrowseButtonClickTriggerHiddenButton(browseButtons);

    // STYLE UPLOAD FORM //
    addPlaceHolderToValueInput(valueInput);
    hideSelects(selects);

    // BODY AND NAV STYLES //
    addClassToClassList(nav, 'porthole-nav');
    addBgColorToBody('porthole-bg-color');


})();