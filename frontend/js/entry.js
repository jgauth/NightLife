let hosts = ["Alpha Epsilon Pi", "Alpha Sigma Phi", "Alpha Tau Omega", "Chi Psi", "Delta Sigma Phi", 
"Delta Tau Delta", "Delta Upsilon", "Kappa Sigma", "Lambda Chi Alpha", "Phi Gamma Delta (FIJI)",
"Pi Kappa Alpha", "Pi Kappa Phi", "Sigma Alpha Epsilon", "Sigma Alpha Mu", "Sigma Chi", "Sigma Nu",
"Sigma Phi Epsilon", "Theta Chi"];

$(document).ready(function(){
    $('input#eventHostInput').autocomplete({
        source: hosts
    });
});