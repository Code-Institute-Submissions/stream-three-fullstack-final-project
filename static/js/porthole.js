// CYCLE PORTHOLE JS //

(() => {

    const nav = document.getElementById('nav');
    const input = document.getElementsByTagName('input');
    const selects = document.getElementsByTagName('select');
    const valueInput = document.getElementById('id_cycle_value_0');

    // GET INPUTS BY FILE INPUT TYPE //
    const getFileInput = (input) => {

        fileInputs = []

        for (let i = 0; i < input.length; i++){ 

            if (input[i].getAttribute('type') == 'file') {

                fileInputs.push(input[i])

                
            }
        }
       
        return fileInputs

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


    const fileInput = getFileInput(input);

    console.log(fileInput);

    addPlaceHolderToValueInput(valueInput);
    hideSelects(selects);
    addClassToClassList(nav, 'porthole-nav');
    addBgColorToBody('porthole-bg-color');


})();