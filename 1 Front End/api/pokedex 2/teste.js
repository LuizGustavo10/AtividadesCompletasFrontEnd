// var defense = stats.find(parametro => parametro.stat.name === "defense").base_stat;

// var defense = stats.find(
    
// function(parametro) {
//     return parametro.stat.name === "defense";
//   }).base_stat;



// Função tradicional
function somaTradicional(a, b) {
  return a + b;
}

// Usando a função
const resultadoTradicional = somaTradicional(3, 5);
console.log(resultadoTradicional); // Saída: 8

// Função de seta
const somaSeta = (a, b) => a + b;

// Usando a função
const resultadoSeta = somaSeta(3, 5);
console.log(resultadoSeta); // Saída: 8