// Variáveis com os caminhos das imagens (substitua pelos nomes reais dos seus arquivos)
var imgManha = "manha.jpg";
var imgTarde = "tarde.webp";
var imgNoite = "noite.jpg";

function mostrarPeriodo(periodo) {
    let mensagemEl = document.getElementById("mensagem");
    let figuraEl = document.getElementById("figura");

    if (periodo === 'manha') {
        mensagemEl.innerText = "Bom dia!";
        figuraEl.src = imgManha;
    } else if (periodo === 'tarde') {
        mensagemEl.innerText = "Boa tarde!";
        figuraEl.src = imgTarde;
    } else if (periodo === 'noite') {
        mensagemEl.innerText = "Boa noite!";
        figuraEl.src = imgNoite;
    }
}