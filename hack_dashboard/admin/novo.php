<?php
    include("../includes/db.inc.php");
    if (!$_SESSION["logged"])
        header("Location: ../index.php");
    else if (!$_SESSION["Admin"])
        header("Location: ../user/home.php");
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="../style.css">
    <title>Index</title>
</head>

<body>
    <main>
        <div class="w-full h-screen">
		    <div class="h-1/6 border-secondary border-0 border-b-2 flex justify-center align-center">
                <a href="home.php" width="150em">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Logo_Sogrape_Original_Legacy_Wines.png/640px-Logo_Sogrape_Original_Legacy_Wines.png"
                    alt="" width="160em" />
                </a>
            </div>
            <div class="flex w-auto h-5/6 justify-center">
                <div class="m-auto w-1/4 justify-center ">
                    <form class="flex flex-col" action="../includes/search.inc.php" method="POST">
                        <p class="text-secondary font-bold text-2xl text-center mb-8">Inserir novo vinho:</p>
                        <p class="text-secondary text-lg text-center mb-1">Nome:</p>
                        <input class="w-full p-4 border-secondary border-0 border-b-2 mb-3" type="text" name="name">                    
                        <p class="text-secondary text-lg text-center mb-1">Ean:</p>
                        <input class="w-full p-4 border-secondary border-0 border-b-2 mb-3" type="text" name="EAN">                     
                        <p class="text-secondary text-lg text-center mb-1">Capacidade:</p>
                        <input class="w-full p-4 border-secondary border-0 border-b-2 mb-12 focus" type="text" name="cap">
                        <input class="rounded w-2/4 px-2 py-1.5 mx-auto text-white" type="submit" value="Pesquisar">                    
                    </form>
                </div>
            </div>
        </div>
    </main>
</body>

</html>