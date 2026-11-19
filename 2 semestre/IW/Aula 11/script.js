var abas = document.querySelectorAll(".aba");
var guias = document.querySelectorAll(".guia");

abas.forEach(function (aba) {
    aba.addEventListener("click", function () {
        abas.forEach(function (item) {
            item.classList.remove("ativa");
        });
        guias.forEach(function (guia) {
            guia.classList.remove("ativa");
        });
        aba.classList.add("ativa");
        document.getElementById(aba.dataset.guia).classList.add("ativa");
    });
});

var clique = 0;
document.getElementById("btnClique").onclick = function () {
    clique++;
    document.getElementById("saidaClique").textContent = "Cliques: " + clique;
};

var duplo = 0;
document.getElementById("btnDuplo").ondblclick = function () {
    duplo++;
    document.getElementById("saidaDuplo").textContent = "Duplo cliques: " + duplo;
};

document.getElementById("btnBaixo").onmousedown = function () {
    document.getElementById("saidaBaixo").textContent = "Botão pressionado!";
};

document.getElementById("btnCima").onmouseup = function () {
    document.getElementById("saidaCima").textContent = "Botão solto!";
};

document.getElementById("areaSobre").onmouseover = function () {
    document.getElementById("saidaSobre").textContent = "Mouse dentro do elemento";
};

document.getElementById("areaFora").onmouseout = function () {
    document.getElementById("saidaFora").textContent = "Mouse saiu do elemento";
};

document.getElementById("areaMove").onmousemove = function (evento) {
    var posicao = this.getBoundingClientRect();
    var x = Math.round(evento.clientX - posicao.left);
    var y = Math.round(evento.clientY - posicao.top);
    document.getElementById("saidaMove").textContent = "X: " + x + " | Y: " + y;
};

document.getElementById("campoFoco").onfocus = function () {
    document.getElementById("saidaFoco").textContent = "Campo com foco!";
};

document.getElementById("selectCor").onchange = function () {
    var valor = this.value;
    document.getElementById("saidaCor").textContent = valor ? "Cor escolhida: " + valor : "Nenhuma cor escolhida";
};

document.getElementById("campoSai").onblur = function () {
    document.getElementById("saidaSai").textContent = "Campo perdeu o foco!";
};

document.getElementById("campoTecla").onkeydown = function (evento) {
    document.getElementById("saidaTecla").textContent = "Tecla pressionada: " + evento.key;
};

document.getElementById("campoCaractere").onkeypress = function (evento) {
    document.getElementById("saidaCaractere").textContent = "Caractere digitado: " + evento.key;
};

document.getElementById("campoSolta").onkeyup = function (evento) {
    document.getElementById("saidaSolta").textContent = "Tecla solta: " + evento.key;
};

window.onload = function () {
    document.getElementById("saidaLoad").textContent = "Página carregada com sucesso!";
};

function mostrarTamanho() {
    document.getElementById("saidaResize").textContent = "Largura: " + window.innerWidth + "px | Altura: " + window.innerHeight + "px";
}

window.onresize = mostrarTamanho;
mostrarTamanho();

document.getElementById("btnResize").onclick = function () {
    window.resizeTo(800, 600);
};
