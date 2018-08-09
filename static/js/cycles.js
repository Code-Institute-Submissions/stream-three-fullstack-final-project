// CYCLES PAGE SCRIPTS //
  
(() => {

    const cycleStatus = document.getElementsByClassName('cycles-results__container'); 
    const selectBoxes = document.getElementsByTagName('select');
    

    // CHANGE THE COLOR OF THE RESULT CONTAINER DIV DEPENDING ON STATUS //
    const bgColorForStatus = (cycleStatus) => {

        if (cycleStatus) {
        
            for(let i = 0; i < cycleStatus.length; i ++){ 
                
                let statusText = cycleStatus[i].childNodes[1].childNodes[1];
                let statusIcon = statusText.firstElementChild;
                let status = statusIcon.getAttribute('data-id');
               
                if (status == "cancelled") {
    
                    cycleStatus[i].classList.add('cycle-results__container-cancelled--color');
                    statusIcon.classList.add('cycle-results__overall-icon-cancelled--color');
                    statusText.classList.add('cycle-results__overall-icon-cancelled--color');
    
                } else if (status == "pending") {
    
                    cycleStatus[i].classList.add('cycle-results__container-pending--color');
                    statusIcon.classList.add('cycle-results__overall-icon-pending--color');
                    statusText.classList.add('cycle-results__overall-icon-pending--color');

                } else if (status == "complete") {
    
                    cycleStatus[i].classList.add('cycle-results__container-complete--color');
                    statusIcon.classList.add('cycle-results__overall-icon-complete--color');
                    statusText.classList.add('cycle-results__overall-icon-complete--color');

                } else if (status == "active") {

                    statusIcon.classList.add('cycle-results__overall-icon-active--color');
                    statusText.classList.add('cycle-results__overall-icon-active--color');

                }
                
            }
            
        }

    }


    bgColorForStatus(cycleStatus);
    addBgColorToBody('body-color');
   // addClassToSelect(selectBoxes, 'cycles-search__select');
 
   

})();