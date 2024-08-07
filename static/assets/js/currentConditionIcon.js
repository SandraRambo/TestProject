/*
This script will check the value in Current Conditions and depending on the value, update the icon
 */
function change (iconID, status){
  console.log("Status is: " + status)
  if(status == "Partly Cloudy") {
    document.getElementById(iconID).className = "bi bi-cloud-sun";
  }else if (status == "Clear"){
    document.getElementById(iconID).className = "bi bi-brightness-high";
  }else{
    document.getElementById(iconID).className = "bi bi-question-lg";
  }
}

