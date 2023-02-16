// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});



let tag=document.getElementsByClassName('project-tag')

for(let i=0;i<tag.length;i++){
    tag[i].addEventListener('click',(e)=> {
    let tagid=e.target.dataset.tag
    let projectid=e.target.dataset.project
    // console.log('tag',tagid)
    // console.log('project',projectid)
    fetch('http://127.0.0.1:8000/api/remove_tag/',{
        method:'DELETE',
        headers:{
          'Content-Type':'application/json',
        },
        body:JSON.stringify({'project':projectid,'tag':tagid})
    }).then(response => response.json())
    .then(data=>
    e.target.remove())
})
}


let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}
