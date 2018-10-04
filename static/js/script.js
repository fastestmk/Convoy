function display(id){
    document.getElementById("delete" + id).style.display = "none";
    document.getElementById("displayDelete" + id).style.display = "block";
}
function cancel(id){
    document.getElementById("delete" + id).style.display = "block";
    document.getElementById("displayDelete" + id).style.display = "none";
}
