function carregou() {
    alert('Página carregada!');
}

function redimensionou() {
    document.getElementById('tela').innerHTML = window.innerWidth + ' x ' + window.innerHeight;
}

function sobre(elemento) {
    elemento.style.transform = 'translateY(-10px) scale(1.03)';
}

function fora(elemento) {
    elemento.style.transform = '';
}

function baixo(elemento) {
    elemento.style.transform = 'scale(0.95)';
}

function cima(elemento) {
    elemento.style.transform = '';
}

function parallax(banner, evento) {
    var tamanho = banner.getBoundingClientRect();
    var x = (evento.clientX - tamanho.left - tamanho.width / 2) * 0.05;
    var y = (evento.clientY - tamanho.top - tamanho.height / 2) * 0.05;
    banner.querySelector('h2').style.transform = 'translate(' + x + 'px,' + y + 'px)';
}

function clique() {
    alert('Clicou!');
}

function duplo(cartao) {
    cartao.style.backgroundColor = cartao.style.backgroundColor == 'red' ? 'white' : 'red';
}

function teclaBaixo(cartao, evento) {
    if (evento.key == 'Enter') {
        alert('Enter no card!');
    }
}

function teclaPress(evento) {
    if (evento.key == ' ') {
        evento.preventDefault();
    }
}

function teclaCima(cartao) {
    cartao.style.transform = '';
}

function foco(campo) {
    campo.style.backgroundColor = '#eef7fc';
    campo.previousElementSibling.style.color = '#ffe08a';
}

function saiu(campo) {
    campo.style.backgroundColor = '';
    campo.previousElementSibling.style.color = '';

    if (campo.value == '') {
        campo.style.backgroundColor = '#ffeef0';
    }
}

function mudou(campo) {
    if (campo.tagName == 'SELECT') {
        alert('Estado: ' + campo.value);
        return;
    }

    campo.value = campo.value.toUpperCase();
}

function digitando(campo) {
    campo.style.backgroundColor = '#eef7fc';
}

function parou(campo) {
    campo.style.backgroundColor = '';
    document.getElementById('contador').innerHTML = campo.value.length + ' / 140';
}

function enviar() {
    if (document.getElementById('nome').value == '' || document.getElementById('email').value == '') {
        alert('Preencha nome e email!');
        return;
    }

    alert('Enviado!');
}