
function myFunctionName() {
  // Declare variables
  let input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  let categorySelected=document.querySelector("select");
  let catValue=categorySelected.value;

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if(catValue==="All" && txtValue.toUpperCase().indexOf(filter) > -1 ){
        tr[i].style.display = "";
      }
      else if (txtValue.toUpperCase().indexOf(filter) > -1 && tr[i].innerText.includes(catValue)) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }

}


function myNewFunction(){

  let categorySelected=document.querySelector("select");
  let catValue=categorySelected.value;
  
  let table = document.getElementById("myTable");
  let tr = table.getElementsByTagName("tr");
 
  for (i = 1; i < tr.length; i++) {
    let td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      let txtValue = td.textContent || td.innerText;
      // console.log(catValue.trim(),txtValue.trim());
      // console.log(!(txtValue.trim()===catValue.trim()));
      if(catValue==="All"){
        tr[i].style.display = "";
      }

      else if (!(txtValue.trim()===catValue.trim())) {
        tr[i].style.display = "none";
      } 
      else {
        tr[i].style.display = "";
      }
    }
  }

}