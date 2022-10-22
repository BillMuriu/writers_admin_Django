// let totalp = document.querySelector('#totalp');

// totalp.addEventListener('click', () => {
//     let level = document.querySelector('#level').value;
//     let pages = document.querySelector('#pages').value;

//     validate
//     if(totalBill === '' || tipPercent == 0 || split == 0){
//         alert('Please enter values');
//         return;
//     }
//     calculate


//     let total = (level) * pages;
//     total = total.toFixed(2);
    
//     document.getElementById('tip').innerHTML = total;


// })




function myFunction(){
    let level = document.querySelector('#level').value;
    let pages = document.querySelector('#pages').value;

    let total = (level) * pages;
    total = total.toFixed(2);

    document.getElementById('tip').innerHTML = total;
     
}


