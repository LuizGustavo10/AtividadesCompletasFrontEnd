// var frase = "Mãe é flor e com ela tudo floresce";
var frase = "Quando você é mãe, você nunca está realmente sozinha em seus pensamentos. Uma mãe sempre tem que pensar duas vezes, uma por ela e outra por seu filho."

function gerarFrase(){
    var texto = document.getElementById("frase");
    texto.innerHTML = frase;
}

function lerFrase(){
     var som = window.speechSynthesis;
     var discurso = new SpeechSynthesisUtterance(frase);
     som.speak(discurso);
}



