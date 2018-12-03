let hosts = ["Alpha Epsilon Pi", "Alpha Sigma Phi", "Alpha Tau Omega", "Chi Psi", "Delta Sigma Phi", 
"Delta Tau Delta", "Delta Upsilon", "Kappa Sigma", "Lambda Chi Alpha", "Phi Gamma Delta (FIJI)",
"Pi Kappa Alpha", "Pi Kappa Phi", "Sigma Alpha Epsilon", "Sigma Alpha Mu", "Sigma Chi", "Sigma Nu",
"Sigma Phi Epsilon", "Theta Chi"];

let themes = ["Toga", "Halloween", "Date Dash", "Formal"
];

$(document).ready(function(){
    $('input#eventHostInput').autocomplete({
        source: hosts
    });

    $('input#eventThemeInput').autocomplete({
        source: themes
    });
    
    ten = function(i) {
        return (i < 10 ? '0' : '') + i;
    }

    var date = new Date();

    YYYY = date.getFullYear();
    MM = ten(date.getMonth() + 1);
    DD = ten(date.getDate());
    HH = ten(date.getHours());
    II = ten(date.getMinutes());
    SS = ten(date.getSeconds());

    now = YYYY + '-' + MM + '-' + DD + 'T' + HH + ':' + II;

    $('input#eventStartTimeEntry').val(now)
    $('input#eventEndTimeEntry').val(now)
});