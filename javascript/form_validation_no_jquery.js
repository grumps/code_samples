/**
 * Created by Maxwell J. Resnick on 8/27/15.
 * same as form_validation, sans jquery
 * All changes to the DOM had to be handled via JavaScript, ie. we had no error classes etc.
 */

var validData = [];

function register() {
    // nothing to see here, move along. perhaps we were to use query strings?
    sessionStorage.setItem('javapic', validData.username);
    // redirect!
    location.href = "gallery.html";
}

function tearDownError(target) {
    this.target = target;
    var messageID = this.target.getAttribute('name') + "error";
    var messageToTear = document.getElementById(messageID);
    // check for existing error message
    if (messageToTear !== null){
        messageToTear.parentNode.removeChild(messageToTear);
    }
}

function assertMessage (target, message) {
    /*
     * @param takes HTMLCollection object, to attach sibling message to
     * @param the message.
     */
    this.target = target;
    this.message = message;
    var messageID = this.target.getAttribute('name') + "error";
    // check for existing error message
    if (document.getElementById(messageID) === null){
        var newMessageBlock = document.createElement('div');
        newMessageBlock.setAttribute('id', messageID);
        var messageText = document.createTextNode(this.message);
        newMessageBlock.appendChild(messageText);
        newMessageBlock.className = "error";
        this.target.parentNode.insertBefore(newMessageBlock, this.target.nextSibling);
    }
}

function validateForm(target, fullForm) {
    /*
     * @description validates form
     */
    this.fieldsToValidate = target;
    this.fullForm = fullForm;
    this.submitButton = document.querySelector('#submit');
    if (this.fullForm) {
        // get array of fields to validate
        this.toValidate = this.fieldsToValidate.target.getElementsByTagName('input');
        this.isValid = checkFields(this.toValidate);
    }
    else {
        this.toValidate = [this.fieldsToValidate.target];
        // we don't set this.isValid b.c. we don't care if a field is validated, that's just for UX.
        checkFields(this.toValidate);
    }
    // now if we have a fully isValid form, we pass off.
    if (this.isValid && this.fullForm) {
        tearDownError(this.submitButton);
        register(validData.username);
    }

    else if (this.fullForm) {
        this.submitError = "Please correct the errors shown above.";
        assertMessage(this.submitButton, this.submitError);
    }
}

function checkFields(targets) {
    this.fieldsToValidate = targets;
    for (var i=0; i < this.fieldsToValidate.length; i++) {
        if (this.fieldsToValidate[i].getAttribute('name') === 'name') {
            // REGEX
            var name = /^[a-zA-Z]+[a-zA-Z ]+[a-zA-Z]$/
                .test(this.fieldsToValidate[i].value);
            // Going to explicitly test for true and false. What if it's all janky?
            if (!name || this.fieldsToValidate[i].length === 0) {
                this.errorMessage = "The name field must only contain Alphabet characters";
                assertMessage(this.fieldsToValidate[i], this.errorMessage);
                return false;
            } else if (name) {
                tearDownError(this.fieldsToValidate[i]);
                validData["name"] = this.fieldsToValidate[i].value;
            }
        }
        else if (this.fieldsToValidate[i].getAttribute('name') === 'email') {
            /*
             * ^[a-zA-Z] - email usernamesstart w/ alpha only
             * [\w\._+] any alphanumeric but also "." "_" "+" are isValid specials for usernames.
             * must be a @
             * any number of domains, subdomains as long as we end with a char.
             */
            var email = /^[a-zA-Z]+[\w\._+]+@([^\.]\w*\.)*[a-zA-Z]*[a-zA-Z]$/
                .test(this.fieldsToValidate[i].value);
            if (!email || this.fieldsToValidate[i].length === 0) {
                this.errorMessage = "A email must be waka@waka.com";
                assertMessage(this.fieldsToValidate[i], this.errorMessage);
                return false;
            } else if (email) {
                tearDownError(this.fieldsToValidate[i]);
                validData["email"] = this.fieldsToValidate[i].value;
            }

        }
        else if (this.fieldsToValidate[i].getAttribute('name') === 'username') {
            // REGEX
            var username = /^[a-zA-Z]+[\w\.][a-zA-Z0-9]+$/
                .test(this.fieldsToValidate[i].value);
            if (!username || this.fieldsToValidate[i].length === 0) {
                this.errorMessage = "A username must start with a char, may only contain _ and . and digits";
                assertMessage(this.fieldsToValidate[i], this.errorMessage);
                return false;
            } else if (username){
                tearDownError(this.fieldsToValidate[i]);
                validData["username"] = this.fieldsToValidate[i].value;
            }
        }
    }
    // zomg we've made it here, we have a isValid form.
    return true;
}


(function (){
    /*
     * @description hack Tiffany's CSS since she gave us no error handling love.
     */
    this.sheet = document.styleSheets[0];
    this.errorStyle = (".error {" +
                       "background-color: tomato;" +
                       "color: #fff;" +
                       "size: .75em;" +
                       "padding: 10px;" +
                       "margin: 10px;" +
                       "border-radius: 5px; }");
    this.sheet.insertRule(this.errorStyle, 0);
}());

// Event Binding
var form = document.getElementById('signup');
form.addEventListener('change', function(e){
    validateForm(e, false);
});
form.addEventListener('submit', function(e){
    // Stop the form from actually submitting.
    e.preventDefault();
    validateForm(e, true);
});