$(function () {
// Get the modal

var addRatingModal = $('#add-cowork-modal');

// Get the button that opens the modal
var addRatingBtn = $('#add-rating-popup');

// Get the <span> element that closes the modal
var span = $(".add-cowork-rating-close");

var secretKey = "thestartupnetwork";
var d = new Date();
var timeStamp = d.getTime();

var ratingKey = secretKey +"_"+timeStamp;

var key = "6Le0DgMTAAAAANokdEEial"; 
var iv  = "mHGFxENnZLbienLyANoi.e"; 

key = CryptoJS.enc.Base64.parse(key);

iv = CryptoJS.enc.Base64.parse(iv);

var encrypted = CryptoJS.AES.encrypt(ratingKey, key, { iv: iv });

var decrypted = CryptoJS.AES.decrypt(encrypted, key, { iv: iv });

var plaintext = decrypted.toString(CryptoJS.enc.Utf8);
	
var cookieValue=getCookie("ratingKey");
console.log("cookieValue.." + cookieValue);
	
if (cookieValue != "" && localStorage.getItem("ratingKey") != null) {
	console.log("key exists");
} 
else{
	  setCookie("ratingKey", encrypted, 30);
	  localStorage.setItem("ratingKey", encrypted);
}

var localStorageValue = localStorage.getItem("ratingKey");
console.log("localStorageValue..." + localStorageValue); 

// When the user clicks the button, open the modal 
addRatingBtn.click(function() {
    addRatingModal.show();
});

// When the user clicks on <span> (x), close the modal
span.click(function() {
    addRatingModal.hide();
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == addRatingModal) {
        addRatingModal.hide();
    }
}
});

$(document).on('click',".rating-selector",function(){
	
var rates = document.getElementsByName('rating');
for(var i = 0; i < rates.length; i++){
    if(rates[i].checked){
        var rate_value = rates[i].value;
         document.getElementById("selected-rating-value").innerHTML = rate_value;
    }
} 

$("#display-1").innerHTML = rate_value;
$("#submit-rating").disabled = false;
$("#submit-rating").show();
$("#submit-rating").css({"backgroundColor":"teal","color":"white"});
});

function selectRating() {
	$("#submit-rating").show();
}

function change() {
	$("#display").show();
	$("#rating-popup").hide();
}

function setCookie(cname,cvalue,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

