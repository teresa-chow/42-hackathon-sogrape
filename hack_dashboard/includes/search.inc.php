<?php 
    include("db.inc.php");

    $name = $_POST["name"];
    $ean = $_POST["EAN"];
    $cap = $_POST["cap"];

    header("Location: ../Admin/home.php");
?>