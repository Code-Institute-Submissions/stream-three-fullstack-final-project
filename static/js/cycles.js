// CYCLES PAGE SCRIPTS //
  
(() => {

    const cycleStatus = document.getElementsByClassName('column-icon');
   
    // -------------------------- FUNCTIONS --------------------------- //

    // CHANGE THE COLOR OF THE RESULTS CONTAINER DIV AND STATUS ICON DEPENDING ON ITS STATUS //
    const colorForStatus = (cycleStatus) => {

        if (cycleStatus) {
        
            for(let i = 0; i < cycleStatus.length; i ++){ 
                // GET CYCLE STATUS CONTAINER //
                const cycleStatusParent = cycleStatus[i].
                                        parentElement.
                                        parentElement;

                // GET CYCLES STATUS FIRST ICON DATA ID //
                const status = cycleStatus[i].
                                    firstElementChild.
                                    firstElementChild.
                                    getAttribute('data-id');

                const statusText = cycleStatus[i].firstElementChild;
                
                // DEPENDING ON DATA ID SET COLOR //
                if (status == "cancelled") {
                   
                    cycleStatusParent.classList.add('cycle-results__container-cancelled--color');
                    statusText.classList.add('cycle-results__overall-icon-cancelled--color');
    
                } else if (status == "pending") {
    
                    cycleStatusParent.classList.add('cycle-results__container-pending--color');
                    statusText.classList.add('cycle-results__overall-icon-pending--color');
                   
                } else if (status == "complete") {
    
                    cycleStatusParent.classList.add('cycle-results__container-complete--color');
                    statusText.classList.add('cycle-results__overall-icon-complete--color');

                } else if (status == "active") {

                    statusText.classList.add('cycle-results__overall-icon-active--color');
                }
                
            }
            
        }

    }

    // -------------------- FUNCTION CALLS ----------------------- //
    
    colorForStatus(cycleStatus);
    addBgColorToBody('body-color');

})();