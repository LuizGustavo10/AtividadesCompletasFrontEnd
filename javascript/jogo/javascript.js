var jogador = "x";

function jogar(celula){
  
    //compara se a célula está vazia para assim escrever
    if(celula.innerHTML == ""){

        //escreve no HTML a letra
        celula.innerHTML = jogador;

        //alterna variavel jogador para a próxima jogada
        if(jogador == "x"){
            jogador = "o";
            celula.style.backgroundColor = "red";

        }else{
            jogador = "x";
            celula.style.backgroundColor = "blue";
        }

    }
}

//função recarrega pagina
function reiniciar(){
    window.location.reload();
}

// fulano = 0, ciclano =1, deltrano =2, beltrano=3
const nomes = ['ALISSON', 'DIOGO ', 'ERICK' ,'FELIPE ', 'GERSON ', 'HILLARY' , 'JOSÉ' ,'MARIA' , 'REINALDO '];

function gerarBatalha(){
 //sorteia um nome da lista, "Math.random vai sortear os itens", "math.floor arredonda o numero da lista"
    const nome1 = nomes[ Math.floor( Math.random() * nomes.length ) ];
    const nome2 = nomes[ Math.floor( Math.random() * nomes.length ) ];

    //enquanto nome1 = nome2, sorteia novamente
    if(nome1 === nome2){
        gerarBatalha();
    }

    //escreve na tela
    document.getElementById('jogador1').textContent = nome1 + " x "+ nome2;
    document.getElementById('jogador2').textContent = nome2;

}

function adicionar() {
    var nome = document.getElementById("nome").value;
    nomes.push(nome);
    listar();

}

function listar(){
    var listagem = document.getElementById("lista");
    listagem.innerHTML= "";                        //limpa a lista em tela

    for(var i = 0; i < nomes.length; i++){         //percorre os itens da lista

        var item = document.createElement("li");    //cria elemento <li> para o HTML
        var nomeItem = nomes[i];                    //guarda na variável NomeItem o nome especifico da lista 
        item.innerHTML = nomeItem;                  //colocar valor dentro do <li>
        listagem.appendChild(item);                 //adiciona o <li> na lista do html, dentro do <ul>
    }
}
