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
            uploadFields[i].parentElement.style.display='none';
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
        
        for (let i = 0; i < browseButtons.length; i++) {

            
            browseButtons[i].addEventListener('click', () => {
                
                console.log(`upload-${i}`);
                
                document.getElementById(`upload-${i}`).click();

            });
        }

    }

    const setNameOfButtonToFile = (uploadFields, browseButtons) => {

        for (let i = 0; i < uploadFields.length; i++) {

            uploadFields[i].onchange = function () {
                
                let stripValue = this.value.toString().replace(/.*(\/|\\)/, " ").substring(0, 15);

                if(stripValue) {

                    let buttonHTML = `<i class="far fa-file"></i> ${stripValue}. . .`;
                    browseButtons[i].innerHTML = buttonHTML;

                } else {

                    let buttonHTML = `<i class="far fa-file"></i> File attached.`;
                    browseButtons[i].innerHTML = buttonHTML;
                }
                
                
                
            }
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
    let uploadFields = [];

            
    if (quoteUpload) {

        uploadFields.push(quoteUpload);

    }  
    
    if (poUpload) {

        uploadFields.push(poUpload);

    } 
    
    if (invoiceUpload) {

        uploadFields.push(invoiceUpload);

    }
       
    console.log(quoteUpload);
    console.log(poUpload);
    console.log(invoiceUpload);
    console.log(uploadFields);


    // TRIGGER HIDDEN DJANGO GENERATED FORM BROWSE BUTTON //
    onBrowseButtonClickTriggerHiddenButton(browseButtons);

    
    // SET CUSTOM UPLOAD BUTTON TO FILE NAME //
    setNameOfButtonToFile(uploadFields, browseButtons);

    // HIDE THOSE ELEMENTS // 
    hideUploadFields(uploadFields);
    //getNameOfFile(quoteUpload);
   

 

    // STYLE UPLOAD FORM //
    // VARIABLE VALUE INPUT ONLY EXISTS IN MEMBER TEMPLATE //
    // CHECK IF IT EXISTS BEFORE EXECUTING // 
    if(valueInput) {

        addPlaceHolderToValueInput(valueInput);

    }
    
    hideSelects(selects);

    // BODY AND NAV STYLES //
    addClassToClassList(nav, 'porthole-nav');
    addBgColorToBody('porthole-bg-color');


})();