/**
 * Created by Max Resnick 9/8/15
 * @description: forum javascript, GET and POST to Google Docs
 */


// Load no conflict version
var $jQ = jQuery.noConflict();


// Objects

var posts = []; // all our posts.


var httpService = {
    /*
     * @description HTTP request handler
     * @return HTTP request as promise
     */
    "get": function () {
        return $jQ.ajax({
            type: "GET",
            dataType: "jsonp",
            url: "https://spreadsheets.google.com/feeds/list/"
        });
    },
    "post": function (title, body) {
         var _data = {
            entry_434124687: title,
            entry_1823097801: body,
         };
         return $jQ.ajax({
            type: "POST",
            url: "https://docs.google.com/forms/d/SOMEID/formResponse",
            dataType: 'json',
            data: _data,
         });
        }
    };

function forumPost (postTitle, postBody) {
    /*
     * @description object representing a single forum post.
     */
    this.postTitle = postTitle;
    this.postBody = postBody;
    this.postHTML = (function () {
                    /*
                     * @description html for object.
                     */
                     return ('<div class="post"><h2>' +
                                        postTitle + '</h2><p>' +
                                        postBody + '</p></div>');
                    }());

}

//  "Controllers"
function formHandler() {
    /*
     * @description determine if new post is valid, if so post to google docs.
     */
    var $errorMessage = $jQ('.error');
    var isValid = true;
    var $inputFields = $jQ('#post-body, #post-title');
    var title, body;
    $inputFields.each(function(index, field) {
        // We are only foolishly checking if we're posting blank messages
        // We also use Jquery parseHTML as a 'cleaner' to check for diry submissions i.e. SQL
        var fieldValue = $jQ.parseHTML(field.value);
        if (fieldValue.length === 0 || fieldValue.length !== 1 ){
            // Array from parseHTML should only be length of 1
            // if it's more we got a bot or injection attack
            isValid = false;
        }
        // populate `title` and `body`, with parseHTML's returned array
        field.id === 'post-title' ? title = fieldValue[0].textContent : body = fieldValue[0].textContent;
    });
    if (isValid) {
        if($errorMessage.length) $errorMessage.remove();
        // we use parseHTML to return a list of nodes
        httpService.post(title, body)
                         .then( // we call the same function due to
                                // a CORS issue w/ posting to google docs.
                                // the promise ends up calling the errorFn despite a successful post.
                                forumPostSuccess, forumPostSuccess);
    } else {
        // if we don't have an element with an error class, add it.
        if(!$errorMessage.length) {
            $jQ('#new-post')
                .append("<div class='error'>Please complete all the fields. </div>")
                .fadeIn('fast');
        }
    }

    function forumPostSuccess(data) {
        var newPost = new forumPost(title, body);
        posts.push = newPost;
        renderPosts(newPost);
        // reset form.
        $inputFields.each(function(index, field) {
            field.value = "";
        });
        $jQ('.success').show().fadeOut(5000); // thanks jQuery, only pass an int
    }
}
function renderPosts(postsToRender) {
    /*
     * @param postsToRender [array] objects to render.
     * @description renders forum posts on html.
     */
    var $main = $jQ('main');
    $jQ(postsToRender).each(function(index, formPost) {
            $main.append(formPost.postHTML);
    });
}

// Event binding
$jQ(function () {
    /*
     * @description bind to submit button on page load.
     */
    $jQ('#new-post').on({
        'submit': function(e) {
            e.preventDefault();
            formHandler();
        },
    });
});


// On Load functions
(function () {
    /*
     * @description load all posts on a page load.
     */
    httpService.get().then(function(data) {
        data.feed.entry.forEach(function(entry){
            posts.push(new forumPost(entry.gsx$posttitle.$t, entry.gsx$postbody.$t));
        });
        renderPosts(posts);
    });

}());
