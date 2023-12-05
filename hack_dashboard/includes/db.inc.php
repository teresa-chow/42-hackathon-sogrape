<?php

    $serverName = "localhost";
    $dbUsername = "root";
    $dbPassword = "4202";
    $dbName = "hackathon";

    $conn = mysqli_connect($serverName, $dbUsername, $dbPassword, $dbName);

    if (!$conn){
        die("Connection failed: " . mysqli_connect_error());
    }

    session_start();
?>