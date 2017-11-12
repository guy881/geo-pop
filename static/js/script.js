function validate_form() {
    check_full_name();
    check_gender();
    //check_schedule();
    check_pesel();
    check_phone_number();
    check_permissions_level();
}

var empty_message = "Proszę wypełnij to pole";
var too_short_message = "Zła długość podanej danej";
var white_space_message = "Podaj pełne imię i nazwisko przedzielone spacją";
var default_message = "Nie możesz wybrać wartości domyślnej";


function isEmpty(field) {
    if (field == null || field == "") {
        return true;
    } else {
        return false;
    }
}

function nameSurname(string) {
    var typedWords = string.match(/\b/g).length / 2;
    if (typedWords <= 1) {
        return true;
    }
}

function showWrong(field, message, glyph) {
    field.innerHTML = message;
    glyph.style.visibility = "visible";
    return false;
}

function showOK(field, glyph, glyph_positive) {
    field.innerHTML = "";
    glyph.style.visibility = "hidden";
    glyph_positive.style.visibility = "visible"
    return true;
}

function check_full_name(form_name) {
    var full_name = document.forms[form_name]["full_name"].value;
    var field = document.getElementById("full_name_error");
    var glyph = document.getElementById("full_name_glyph");
    if (isEmpty(full_name)) {
        showWrong(field, empty_message, glyph)
    } else if (full_name.length < 6) {
        showWrong(field, too_short_message, glyph)
    } else if (nameSurname(full_name)) {
        showWrong(field, white_space_message, glyph)
    } else {
        showOK(field, glyph)
    }
}

function check_gender(form_name) {
    var gender = document.forms[form_name]["gender"].value;
    var field = document.getElementById("gender_error");
    var glyph = document.getElementById("gender_glyph");
    if (isEmpty(gender)) {
        showWrong(field, empty_message, glyph)
    } else if (gender == "default") {
        showWrong(field, default_message, glyph)
    } else {
        showOK(field, glyph)
    }
}

/*function check_schedule() {
    var schedule = document.forms["create_driver_form"]["schedule"].value;
    var field = document.getElementById("schedule_error");
    var glyph = document.getElementById("schedule_glyph");
    if (isEmpty(schedule)) {
        showWrong(field, empty_message, glyph)
    } else if (schedule.length < 10) {
        showWrong(field, too_short_message, glyph)
    } else {
        showOK(field, glyph)
    }
}*/

function check_pesel(form_name) {
    var pesel = document.forms[form_name]["pesel"].value;
    var field = document.getElementById("pesel_error");
    var glyph = document.getElementById("pesel_glyph");
    if (isEmpty(pesel)) {
        showWrong(field, empty_message, glyph)
    } else if (pesel.length !== 11) {
        showWrong(field, too_short_message, glyph)
    } else {
        showOK(field, glyph)
    }
}

function check_phone_number(form_name) {
    var phone_number = document.forms[form_name]["phone_number"].value;
    var field = document.getElementById("phone_number_error");
    var glyph = document.getElementById("phone_number_glyph");
    if (isEmpty(phone_number)) {
        showWrong(field, empty_message, glyph)
    } else if (phone_number.length !== 9) {
        showWrong(field, too_short_message, glyph)
    } else {
        showOK(field, glyph)
    }
}

function check_permissions_level(form_name) {
    var permissions_level = document.forms[form_name]["permissions_level"].value;
    var field = document.getElementById("permissions_level_error");
    var glyph = document.getElementById("permissions_level_glyph");
    if (isEmpty(permissions_level)) {
        showWrong(field, empty_message, glyph)
    } else if (permissions_level == "default") {
        showWrong(field, default_message, glyph)
    } else {
        showOK(field, glyph)
    }
}

function check(form_name, param) {
    var param_value = document.forms[form_name][param].value;
    var field = document.getElementById(param + "_error");
    var glyph = document.getElementById(param + "_glyph");
    if (isEmpty(param_value)) {
        showWrong(field, empty_message, glyph);
    }
}