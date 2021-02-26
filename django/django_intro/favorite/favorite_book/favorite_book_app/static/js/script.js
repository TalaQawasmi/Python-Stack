function validateRegister() {
    var fname = document.forms["register"]["fname"].value, lname = document.forms["register"]["lname"].value, email = document.forms["register"]["email"].value, birthday = document.forms["register"]["date"].value, password = document.forms["register"]["password"].value, confirm = document.forms["register"]["confirm"].value;
    var pattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    var errors = [];
    if (fname.length == 0) {
        errors.push("First Name is required");
    }
    if(lname.length == 0){
        errors.push("Last Name is required");
    }
    if(email.length == 0){
        errors.push("Email is required");
    }
    if(birthday.length == 0){
        errors.push("Birthday is required");
    }
    if(password.length == 0){
        errors.push("Password is required");
    }
    if(confirm.length == 0){
        errors.push("Confirm your password");
    }
    console.log(errors)
    for(var i=0; i<errors.length;i++){
        var para = document.createElement("p");
        var node = document.createTextNode(errors[i]);
        para.appendChild(node);
        var element = document.getElementById("errors");
        element.appendChild(para);
    }
    if (errors.length > 0){
        return false;
    }
}
function validateForm() {
    var title =  document.forms["book"]["title"].value, desc = document.forms["book"]["desc"].value;
    var errors = [];
    if (title.length == 0){
        errors.push("Title is required");
    }
    if (desc.length < 5){
        errors.push("Description must be more than 5 characters");
    }
    for(var i=0; i<errors.length;i++){
        var para = document.createElement("p");
        var node = document.createTextNode(errors[i]);
        para.appendChild(node);
        var element = document.getElementById("errors");
        element.appendChild(para);
    }
    if (errors.length > 0){
        return false;
    }
}
function validateLogin(){
    email = document.forms["login"]["email"].value, password = document.forms["login"]["password"].value;
    errors = [];
    if(email.length == 0){
        errors.push("Email is required");
    }
    if(password.length == 0){
        errors.push("Password is required");
    }
    for(var i=0; i<errors.length;i++){
        var para = document.createElement("p");
        var node = document.createTextNode(errors[i]);
        para.appendChild(node);
        var element = document.getElementById("errors");
        element.appendChild(para);
    }
    if (errors.length > 0){
        return false;
    }

}
function validateBook(){
    var title = document.forms["book"]["title"].value, errors=[];
    if(title.length == 0){
        errors.push("Title is required")
    }
    for(var i=0; i<errors.length;i++){
        var para = document.createElement("p");
        var node = document.createTextNode(errors[i]);
        para.appendChild(node);
        var element = document.getElementById("errors");
        element.appendChild(para);
    }
    if (errors.length > 0){
        return false;
    }
}