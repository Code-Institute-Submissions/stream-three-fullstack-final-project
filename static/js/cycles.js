// CYCLES PAGE SCRIPTS //
  
(() => {

   // const cycleStatus = document.getElementsByClassName('column-icon');
    const portholeButton = document.getElementsByClassName('cycles-results__porthole-button');

    //-----//

    const cycleStatus = document.getElementsByClassName(' cycles-status-icon');

    // -------------------------- FUNCTIONS --------------------------- //

    // CHANGE THE COLOR OF THE RESULTS CONTAINER DIV AND STATUS ICON DEPENDING ON ITS STATUS FOR NON TABLE TABLES //
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

    const colorForStatusTable = () => {

        if (cycleStatus) {
        
            for(let i = 0; i < cycleStatus.length; i ++){ 
                // GET CYCLE STATUS CONTAINER //
                const cycleStatusParent = cycleStatus[i].
                                        parentElement.
                                        parentElement.
                                        parentElement.
                                        parentElement.
                                        parentElement;

                // GET CYCLES STATUS FIRST ICON DATA ID //
                const status = cycleStatus[i].getAttribute('data-id');

                const statusText = cycleStatus[i].parentElement;
                
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
    
   //colorForStatus(cycleStatus);
    colorForStatusTable();

    for (let i = 0; i < portholeButton.length; i++) {

        tippy(portholeButton[i], toolTipDefault);
    }

})();