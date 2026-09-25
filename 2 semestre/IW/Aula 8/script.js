function mudou(){
    if(itens.value==1){
        alert("mudou para o 1");
        document.body.style.backgroundColor="green";
    } else if (itens.value==2){
        alert("mudou para o 2");
        document.body.style.backgroundColor="yellow";
    } else if (itens.value==3){
        alert("mudou para o 3");
        document.body.style.backgroundColor="purple";
    } else if (itens.value==4){
        alert("mudou para o 4");
        document.body.style.backgroundColor="blue";
    } else if (itens.value==5){
        alert("mudou para o 5");
        document.body.style.backgroundColor="red";
    } else {
        alert("Não disponível");
    }
}