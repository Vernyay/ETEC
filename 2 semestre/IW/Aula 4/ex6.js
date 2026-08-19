function idade() {
    const num1 = Number(document.getElementById("num1").value);

    var age_dog = num1*7;

    if (age_dog>50) {
        document.getElementById("resultado").textContent = "Seu cachorro tem " + age_dog + " anos caninos, seu cachorro é um Cão Idoso!";
    } else {
        document.getElementById("resultado").textContent = "Seu cachorro tem " + age_dog + " anos caninos, seu cachorro é um Cão Jovem!";
    }
}