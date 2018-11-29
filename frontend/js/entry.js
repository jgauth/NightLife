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

    var now = new Date();
    var day = ("0" + now.getDate()).slice(-2);
    var month = ("0" + (now.getMonth() + 1)).slice(-2);
    var hour = now.getHours()
    var minute = now.getMinutes()
    var second = now.getSeconds()
    var today = now.getFullYear()+"-"+(month)+"-"+(day)+"T"+(hour)+":"+(minute)+":00";
    var today2 = now.getFullYear()+"-"+(month)+"-"+(day)+"T"+(hour+2)+":"+(minute)+":00";
    
    $('input#eventStartTimeEntry').val(today)
    $('input#eventEndTimeEntry').val(today2)
});