// This is for Django's CSRF protection; see https://docs.djangoproject.com/en/1.5/ref/contrib/csrf/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// Helpful snippet from http://stackoverflow.com/questions/680241/resetting-a-multi-stage-form-with-jquery
function resetForm($form) {
    $form.find('input:text, input:password, input:file, select, textarea').val('');
    $form.find('input:radio, input:checkbox')
         .removeAttr('checked').removeAttr('selected');
}

// Main App
$(document).ready(function() {
  // Account - Use ajax to get the account edit from and 
  // display it on the page w/out a refresh
  
  $('#gi-container').delegate('.edit-account', 'click', function(e) {
        e.preventDefault();
        $('#gi-container').load($(this).attr('href'));
    });


  // Contact - Use AJAX to get the Contact Add form
    $('#cd-container').delegate('#new-contact', 'click', function(e) {
        e.preventDefault();
        $.get($(this).attr('href'), function(data) {
            $('#cd-body').append(data);
            $('#new-contact').hide();
        });
    });

    // Contact - Use AJAX to get the Contact Edit form
    $('#cd-container').delegate('.edit-contact', 'click', function(e) {
        e.preventDefault();
        var that = $(this);
        $.get($(this).attr('href'), function(data) {
            $('#new-contact').hide();
            that.parent().parent().remove();
            $('#cd-body').append(data);
        })
    });

    // Contact - Use AJAX to save the Contact Add Form
    $('#cd-container').delegate('#contact-form', 'submit', function(e) {
        e.preventDefault();
        var form = $('#contact-form');
        var url = form.attr('action');
        $.post(url, form.serialize(), function(data) {
            if ($(data).find('.errorlist').html()) {
                // If the contact form is returned we know there are errors
                $('#new-contact').hide();
                $('#cd-body').append(data);
            } else {
                // Otherwise insert the row into the table
                $('#cd-table tr:last').after(data);
                $('#new-contact').show();
            }
        });
        $(this).remove(); // Remove the form
    });
});
