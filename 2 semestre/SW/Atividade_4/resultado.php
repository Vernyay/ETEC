<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
</head>
<body>
    <?php
    require_once 'controller.php';
    echo "Nome: ".$nome."<br>";
    echo "Total sem desconto: R$ ".$total."<br>";
    echo "Total com desconto: R$ ".$desc."<br>";
    if ($estoque==True) {
        echo "Esta em estoque baixo!";
    } else {
        echo "";
    }
    ?>
</body>
</html>