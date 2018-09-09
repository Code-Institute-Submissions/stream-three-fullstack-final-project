// CYCLES PAGE SCRIPTS //
  
(() => {

    const portholeButton = document.getElementsByClassName('cycles-results__porthole-button');

    //-----//

    const cycleStatus = document.getElementsByClassName(' cycles-status-icon');

    // -------------------------- FUNCTIONS --------------------------- //

    const colorForTable = () => {

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
    colorForTable();

    for (let i = 0; i < portholeButton.length; i++) {

        tippy(portholeButton[i], toolTipRight);
    }

})();