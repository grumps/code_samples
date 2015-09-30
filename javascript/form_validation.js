/**
 * Created by Maxwell J. Resnick on 9/1/15.
 */

var form = {
    /*
     * @description form validation obj.
     */
    name: function (name) {
        var isValid = /^([a-zA-Z]+)$/
            .test(name);
        this.errorMessage = "Your name must be chars only.";
        if (!isValid) {
            this.errors["name"] = this.errorMessage;  // should really use '.' not a dict style like python
            this.validFields["name"] = false;
        } else {
            this.errors["name"] = false;
            this.validFields["name"] = true;
        }
        return isValid;
    },
    username: function (username) {
        var isValid = /^[a-zA-Z]+[\w\.][a-zA-Z0-9]+$/
            .test(username);
        this.errorMessage = "Your name must be number, chars, and _ only.";
        if (!isValid) {
            this.errors["username"] = this.errorMessage;
            this.validFields["username"] = false;
        } else {
            this.errors["username"] = false;
            this.validFields["username"] = true;
        }
        return isValid;
    },
    email: function (email) {
        // this doesn't pass 100% email IETF addresses, but we had to do our own regex
        var isValid = /^[a-zA-Z]+[\w\._+]+@([^\.]\w*\.)*[a-zA-Z]*[a-zA-Z]$/
            .test(email);
        this.error = "You must have a valid email address.";
        if (!isValid) {
            this.errors["email"] = this.errorMessage;
            this.validFields["email"] = false;
        } else {
            this.errors["email"] = false;
            this.validFields["email"] = true;
        }
        return isValid;
    },
    isValid: function () {
        // check for false to be in our validFields obj.
        var hasInvalid = false;
        var potentialValidData = {};
        $jQ.each(this.validFields, function (index, value) {
            potentialValidData[index] = $;
            if (!value) {
                hasInvalid = true;
            }
        });
        // flip logic, because were checking for the existence, of false.
        return !hasInvalid;
    },
    validFields: { name: false, username: false, email : false },
    errors: { name: false, username: false, email : false },
};

// Handlers 
function formHandler($e) {
    /*
     * @description
     */
    $e.each(function () {
        if (!form[this.name](this.value)) {
            // only add if div doesn't exist.
            if (!$jQ(this).next().attr('class')) {
                $jQ(this).after(function () {
                        return '<div class="error">' + form.errors[this.name] + '</div>';
                });
            }
        } else {
            $jQ(this).next('.error').remove();
        }
    });
    // validation over.

};

function register(toCheck) {
    /*
     * @description validate form && set session.
     */
    formHandler(toCheck);
    if (form.isValid()){
        sessionStorage.setItem('javapic', $jQ("[name='username']").val());
        location.href = 'gallery.html';
    }
    else {
        $jQ('.error').fadeOut("fast").fadeIn("fast");
    }
}

(function () {
    /*
     * @description make my error css class, because we weren't 
     *              allowed to touch both the HTML & CSS unless we didd it in JS
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

// Event binds
$jQ(function () {
    /*
     * @description event bindings.
     */
    $jQ('#signup').on({
        'submit': function(e){
            e.preventDefault();
            var toCheck = $jQ(e.target).children('input').not("#submit");
            register(toCheck);
        },
        'change': function(e){
            var toCheck = $jQ(e.target);
            formHandler(toCheck);
        }
    });
}());