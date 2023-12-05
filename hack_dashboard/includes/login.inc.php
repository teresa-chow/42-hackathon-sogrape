<?php 
    include("db.inc.php");

    $name = $_POST["name"];
    $password = $_POST["password"];


    $sql = "SELECT * FROM users WHERE Username = '$name' AND Password = '$password'";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);

    if (!$row) 
        header("Location: ../index.php?error=1" );
    else
    {
        $_SESSION["name"] = $name;
        $_SESSION["password"] = $password;
        $_SESSION["logged"] = true;
        $_SESSION["Admin"] = $row["IsAdmin"];   
        if ($_SESSION["Admin"])
            header("Location: ../admin/home.php");
        else 
            header("Location: ../user/home.php");
    }
?>