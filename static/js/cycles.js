// CYCLES PAGE SCRIPTS //
  
(() => {

    const cycleStatus = document.getElementsByClassName('column-icon'); 
   
    // -------------------------- FUNCTIONS --------------------------- //

    // CHANGE COLOR OF STATUS ICONS DEPENDING ON STATUS //
    const colorForStatusIcons = (cycleStatus, _class) => {

        for(let i = 0; i < cycleStatus.length; i ++){ 
            
            const statusText = cycleStatus[i].firstElementChild;
            statusText.classList.add(_class);
            
        }

    }
    // CHANGE THE COLOR OF THE RESULT CONTAINER DIV DEPENDING ON STATUS //
    const bgColorForStatus = (cycleStatus) => {

        if (cycleStatus) {
        
            for(let i = 0; i < cycleStatus.length; i ++){ 
                // GET CYCLE STATUS CONTAINER //
                const cycleStatusParent = cycleStatus[i].
                                        parentElement.
                                        parentElement;

                // GET CYCLES STATUS FIRST ICON //
                const status = cycleStatus[i].
                                    firstElementChild.
                                    firstElementChild.
                                    getAttribute('data-id');
               
                if (status == "cancelled") {
                   
                    cycleStatusParent.classList.add('cycle-results__container-cancelled--color');
                    colorForStatusIcons(cycleStatus, 'cycle-results__overall-icon-cancelled--color');
    
                } else if (status == "pending") {
    
                    cycleStatusParent.classList.add('cycle-results__container-pending--color');
                    colorForStatusIcons(cycleStatus, 'cycle-results__overall-icon-pending--color');
    

                } else if (status == "complete") {
    
                    cycleStatusParent.classList.add('cycle-results__container-complete--color');
                    colorForStatusIcons(cycleStatus, 'cycle-results__overall-icon-complete--color');
            
                } else if (status == "active") {

                    colorForStatusIcons(cycleStatus, 'cycle-results__overall-icon-active--color');
                }
                
            }
            
        }

    }


    // -------------------- FUNCTION CALLS ----------------------- //
    
    bgColorForStatus(cycleStatus);
    addBgColorToBody('body-color');

})();