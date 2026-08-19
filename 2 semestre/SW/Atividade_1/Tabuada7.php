<?php
$num = $_POST["numero"];
for ($i = 1; $i<11; $i++){
    
    echo $num . " x " . $i . "=" . ($num*$i) . "<br/>" ;
}