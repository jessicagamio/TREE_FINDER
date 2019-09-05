    

function showSpinner () {
  const spinner = document.querySelector('#spin');
  spinner.style.display= 'inline-block';
}

function hideSpinner () {
  const spinner = document.querySelector('#spin');
  spinner.style.display= 'none';
}

function formInputs(evt){
  //access file 
  const files = document.getElementById('customFile').files;
  console.log(files.length);
  //show spinner
  showSpinner();
  
  //if no file selected prevent default 
  if (files.length===0){
    console.log(files.length)
    evt.preventDefault();

    // dipslay flash message
    const message=document.querySelector('#flash');
    message.style.display = 'block';

    //hide spinner
    hideSpinner();
  }
}

//On click submit button call formInputs
$('#img_submit').on('click', formInputs);


customFile=document.querySelector('#customFile');

customFile.addEventListener('change',()=>{
//Display File Name in layer when chosen
var filename = document.getElementById('customFile').files[0].name;
$('#displayfile').html(filename);
})

