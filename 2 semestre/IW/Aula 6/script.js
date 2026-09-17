document.addEventListener("DOMContentLoaded", () => {
    const visor = document.getElementById("texto");
    const botoes = document.querySelectorAll("#botoes button");

    let numeroDigitado = "";

    // Mapeamento dos candidatos cadastrados no seu HTML
    const candidatos = {
        "99": "Du Contra",
        "66": "Cebolinha",
        "42": "Julio",
        "13": "Pokemon Lixo",
        "76": "JUAN!!!"
    };

    botoes.forEach((botao) => {
        botao.addEventListener("click", () => {
            const valor = botao.value;

            if (valor === "Branco") {
                numeroDigitado = "BRANCO";
                visor.innerText = numeroDigitado;
            } 
            else if (valor === "Apagar") {
                numeroDigitado = "";
                visor.innerText = "";
            } 
            else if (valor === "Enviar") {
                if (numeroDigitado === "") {
                    alert("Por favor, digite um número ou escolha BRANCO antes de enviar.");
                    return;
                }

                // Verificação do voto
                if (numeroDigitado === "BRANCO") {
                    alert("Você votou em: BRANCO");
                } 
                else if (candidatos[numeroDigitado]) {
                    // Candidato encontrado na lista
                    const nomeCandidato = candidatos[numeroDigitado];
                    alert(`Voto confirmado para: ${nomeCandidato} (Número ${numeroDigitado})`);
                } 
                else {
                    // Número não encontrado
                    alert(`Número ${numeroDigitado} não encontrado! VOTO NULO / INVÁLIDO.`);
                }

                // Finalização do voto
                numeroDigitado = "";
                visor.innerText = "FIM";
                
                setTimeout(() => {
                    visor.innerText = "";
                }, 2000);
            } 
            else {
                // Se já estiver "BRANCO" e clicar em um número, limpa e inicia o número
                if (numeroDigitado === "BRANCO") {
                    numeroDigitado = "";
                }

                // Permite até 2 dígitos
                if (numeroDigitado.length < 2) {
                    numeroDigitado += valor;
                    visor.innerText = numeroDigitado;
                }
            }
        });
    });
});