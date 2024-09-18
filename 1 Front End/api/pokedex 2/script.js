var contador = 0;

function buscar() {
    var entrada = document.getElementById("entrada").value.toLowerCase();

    if (entrada.length < 1) {         //se o campo de input está vázio, chama o contador
        entrada = contador;         //entrada = numero que está o contador (1,2,3...)
        //com o campo de input vazio, vai buscar por numero na URL
    }

    var url = "https://pokeapi.co/api/v2/pokemon/" + entrada + "";

    fetch(url)
        .then(response => response.json())
        .then(data => {

            var stats = data.stats;
            var hp = stats.find(parametro => parametro.stat.name === "hp").base_stat;
            var attack = stats.find(parametro => parametro.stat.name === "attack").base_stat;
            var defense = stats.find(
                function (parametro) {
                    return parametro.stat.name === "defense";
                }).base_stat;

            var tela = document.getElementById("tela");
            tela.innerHTML =
                `
                <img class="pokemon" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/${data.id}.gif" > 
                <img class="pokemon" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/back/${data.id}.gif" > 
                <div class="numero"> ${data.id} </div>
                <div class="inf"> 
                    <p>  <b> Nome </b> ${data.name} </p>
                    <p>  <b> Peso </b> ${data.weight / 10} Kg </p>
                    <p>  <b> Altura </b> ${data.height / 10} M </p>
                    <p>  <b> Tipo </b>  ${data.types.map(parametro => parametro.type.name)} </p>
                    <p>  <b> Hab </b>  ${data.abilities.map(parametro => parametro.ability.name)} </p>
                    <br>
                    
                    Vida ${hp}
                    <div id="hp-bar" style="width: 100%; height: 20px; margin: 5px 0;"></div>
                    Ataque ${attack}
                    <div id="attack-bar" style="width: 100%; height: 20px; margin: 5px 0;"></div>
                    Defesa ${defense}
                    <div id="defense-bar" style="width: 100%; height: 20px; margin: 5px 0;"></div>

                    <br> <br>
                </div>
                `;
            contador = data.id;                              //atualiza o contador para o id do pokemon
            document.getElementById("entrada").value = "";     //limpa o input de entrada

            var maxStat = 200; // Max value for stats

            // Cria uma nova barra de progresso linear (horizontal)
            var hpBar = new ProgressBar.Line('#hp-bar', {
                // Define a espessura da linha da barra de progresso
                strokeWidth: 1,

                // Define a cor da barra de progresso (neste caso, um tom de laranja)
                color: '#b84304',

                // Define a cor da trilha (a parte de fundo da barra, que não está preenchida)
                trailColor: '#e0e0e0',

                // Define a espessura da trilha (deve ser igual ou maior que 'strokeWidth')
                trailWidth: 1,

                // Define a duração da animação de preenchimento da barra (em milissegundos)
                duration: 1400
            });
            
            var attackBar = new ProgressBar.Line('#attack-bar', {
                strokeWidth: 1,
                color: '#b84304',
                trailColor: '#e0e0e0',
                trailWidth: 1,
                duration: 1400
            });
            var defenseBar = new ProgressBar.Line('#defense-bar', {
                strokeWidth: 1,
                color: '#b84304',
                trailColor: '#e0e0e0',
                trailWidth: 1,
                duration: 1400

            });

            hpBar.animate(hp / maxStat);
            attackBar.animate(attack / maxStat);
            defenseBar.animate(defense / maxStat);

        }).catch(error => {
            var tela = document.getElementById("tela");
            tela.innerHTML = '<p> Pokemon não encontrado! </p>' + error;
        })
}




function proximo() {
    contador = contador + 1;
    buscar();

}

function anterior() {
    contador = contador - 1;
    buscar();

}


