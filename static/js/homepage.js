

function showSpinner () {
  const spinner = document.querySelector('#spin');
  spinner.style.display= 'inline-block';
}

function hideSpinner () {
  const spinner = document.querySelector('#spin');
  spinner.style.display= 'none';
}
function formInputs(evt){
  const files = document.getElementById('customFile').files;
  console.log(files.length);
  showSpinner();
  
  if (files.length===0){
    console.log(files.length)
    evt.preventDefault();
    const message=document.querySelector('#flash');

    message.style.display = 'block';
    hideSpinner();
  }

}

$('#img_submit').on('click', formInputs);


customFile=document.querySelector('#customFile');

customFile.addEventListener('change',()=>{
  var filename = document.getElementById('customFile').files[0].name;
  $('#displayfile').html(filename);
  })
