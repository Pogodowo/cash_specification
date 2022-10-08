const csrf = document.getElementsByName('csrfmiddlewaretoken')
var inputs = document.getElementsByClassName("calc-input");
var clearButton=document.getElementById("clear-button")
var submitButton=document.getElementById("submit-button")

window.onload = function() {
var basicActiveElement=document.getElementById('input-500').focus();
switchingInput();
calculations("calculations")
}



document.addEventListener ("click" ,function(){ switchingInput();})

function switchingInput(){
 var currentInput=document.activeElement;
    document.onkeydown = (function(e){
    if(event.keyCode=='40'){
    currentInput.blur();
    if (currentInput.parentElement.parentElement.nextElementSibling!=null){
    currentInput=currentInput.parentElement.parentElement.nextElementSibling.getElementsByTagName('input')[0];
    currentInput.focus();}
    else{currentInput.focus();}
         }
    if(event.keyCode=='38'){
    currentInput.blur();
    if (currentInput.parentElement.parentElement.previousElementSibling.getElementsByTagName('input')[0]!=null){
    currentInput=currentInput.parentElement.parentElement.previousElementSibling.getElementsByTagName('input')[0];
    currentInput.focus();                              }
    else{//currentInput.focus();
    document.getElementById('input-500').focus();}
         }
                                      })
}


function calculations(url){
var givenAmountsData={'csrfmiddlewaretoken': csrf[0].value ,}
for (var i = 0, len = inputs.length; i < len; i++) {
givenAmountsData[inputs[i].id]=inputs[i].value
}

 $.ajax({
                type: 'POST' ,
                url: url,
                data : givenAmountsData,
                success: function(response){
                         calc=response.ajax_response.calculations_json
                         for (const [key, value] of Object.entries(calc) ){
                         document.getElementById(key).innerText=value
                         if (key.slice(0, 4)=='sum-'){ document.getElementById(key).innerText=value+' zł.';}
                         }
                         document.getElementById('suma').innerText=response.ajax_response.sum_all+' zł.'
                         document.getElementById('sumtext').innerText=response.ajax_response.text_sum_all
                                        },

                error : function(error){

                                                    }
                 });
}


function postToUrl(path) {
    method = "post";

    var givenAmountsData={'csrfmiddlewaretoken': csrf[0].value ,}
    for (var i = 0, len = inputs.length; i < len; i++) {
    givenAmountsData[inputs[i].id]=inputs[i].value
    }
    var form = document.createElement("form");

    //Move the submit function to another variable
    //so that it doesn't get overwritten.
    form._submit_function_ = form.submit;

    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in givenAmountsData) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", givenAmountsData[key]);

        form.appendChild(hiddenField);
    }

    document.body.appendChild(form);
    form._submit_function_(); //Call the renamed function.
}


function clearingForm () {
for (var i = 0, len = inputs.length; i < len; i++) {

        inputs[i].value='';
}
}




document.addEventListener ("input" ,function(){ calculations("calculations")})
submitButton.addEventListener("click" , function(){event.preventDefault();postToUrl("to_pdf");})
clearButton.addEventListener ("click" , function(){clearingForm ();calculations("calculations")})
