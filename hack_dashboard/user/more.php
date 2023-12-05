<?php
    include("../includes/db.inc.php");

    $id = $_GET["ID"];

    $sql = "SELECT * FROM wine WHERE id =" . $id;
    $result = mysqli_query($conn, $sql);

    $row=mysqli_fetch_assoc($result);
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
            <div class="flex w-auto h-5/6">
                <div class="m-auto ms-8 w-1/4">
				<img class="rounded mx-auto"
                        src="<?= $row["img"] ?>" alt="Mateus Rosé Original"
                        width="285em" />
                    <!-- <img class="rounded mx-auto"
                        src="./img/Mateus Rosé Original.jpg" alt="Mateus Rosé Original"
                        width="285em" /> -->
						<!-- <img class="rounded mx-auto"
                        src="./img/Mateus Sparkling Rosé.jpg" alt="Mateus Rosé Sparkling"
                       width="285em" /> -->
						<!-- <img class="rounded mx-auto"
						src="Herdade do Peso Trinca Bolotas Tinto.jpg" alt="H.P. Trinca Bolotas Tinto"
						width="285em" /> -->
						<!-- <img class="rounded mx-auto"
                        src="Casa Ferreirinha Papa Figos Branco.jpg" alt="C.F. Papa Figos Branco"
                        width="285em" /> -->
                </div>
                <div class="flex w-4/5">
                    <div class="w-3/4 h-auto my-auto">
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Name:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4 ">
                                <?= $row["name"] ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Store:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["store"]?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Location:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["loc"] == "es" ? "Espanha" : "Portugal" ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Year:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["year"] ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Price:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["price"] . $row["curr"] ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Discounted:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["disc"] ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Scraping Date:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["date"] ?>
                            </p>
                        </div>
                        <div class="m-auto flex w-full">
                            <p class="text-secondary font-bold my-auto me-6 text-lg py-3">Capacity:</p>
                            <p class="my-auto border-b-2 border-stone-800 my-8 text-lg w-3/4">
                                <?= $row["capacity"] ?>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>

</html>