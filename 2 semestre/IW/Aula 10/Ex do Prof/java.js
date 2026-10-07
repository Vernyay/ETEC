/* Eventos
eventos são ações disparadas pela interação dos usuários na página.
o corrote manejo desses eventos que tornam as páginas interativas e dinâmicas.

existem muitos eventos. Veja os mais utilizados:

onclick -> Disparado quando recebe um click.
ondblclick -> Disparado quando recebe um clique duplo.
onmouseover -> Dispara quando o mouse está sobre.
onmouseout -> Dispara quando o mouse é movido para fora do elemento.
onmousemove -> Dispara quando o mouse é movido no elemento.
onmousedown -> Dispara quando o clique do botão foi pressionado.
onmouseup -> Disparado quando o clique do botão é liberado
onfocus -> Disparado quando o elemento recebo o foco. Válido para input,
onchange -> Disparado quando existe uma mudanã no conteúdo. "Ao mudar".
onblur -> Disparado quando o elemento perde o foco.
onkeydown -> Disparado quando uma tecla é pressionada.
onkeypress -> Disparado quando uma tecla é pressionada e solta.
onkeyup -> Disparado quando uma tecla é solta sobre um elemento.
onload -> Disparado quando a página terminou de ser carregada. Body.
onredize -> Disparado quando há um redimencionamento da janela.

*/

function eventoClick(){
	alert('Acionou um evento de click');
	document.body.style.backgroundColor = "#00BFFF";
}

function eventoMouse(){
	
	alert("passou o mouse");
	document.body.style.backgroundColor = "green";
	
}

function viracor(){
	let div = document.getElementById("teste");
	div.style.backgroundColor = "red";
	
}

function viracor2(){
	let div = document.getElementById("teste");
	div.style.backgroundColor = "blue";
	
}

function adicionaTexto(){
	let p = document.getElementById("nome");
	p.append('Você clicou <br>');
	
}

function escrita(){
	document.getElementById("texto").value = "";
		
}

function mudou(){
	if(itens.value=="1"){
		alert("mudou para o 1");
	}else{
		alert("mudou mas não é o 1");
}}
	