<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="./style.css">
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <title>Sogrape Scraper</title>
</head>
<body>
    <main>
        <div class="w-screen h-screen background-select">
            <div class="h-full my-auto flex justify-center w-full items-center flex-col">
                <div class="h-1/4"> 
                    <img src="./img/logo.png" alt="">
                </div>
                <div class="h-5/12 bg-white py-4 px-10 rounded w-4/12"> 
                    <form class="w-full flex flex-col items-center" action="./includes/login.inc.php" method="POST">
                        <p class="text-secondary text-xl font-bold mb-2">User</p>
                        <input class="rounded border-secondary border-2 p-2 w-3/4 mb-8 "type="text" name="name" id="">
                        <p class="text-secondary text-xl font-bold mb-2">Password</p>
                        <input class="rounded border-secondary border-2 p-2 w-3/4 mb-4"type="password" name="password" id="">
                        <br>
                        <input class="secondary p-1 w-1/4 mx-auto rounded text-white hover:cursor-pointer focus:translate-y-0.5 focus:translate-x-0.5 mb-4" type="submit" value="Ok">
                        <p class="text-red-600 font-bold"><?= isset($_GET["error"]) ? "Wrong Login" : "" ?></p>
                    </form>
                </div>
            </div>
        </div>
    </main>
</body>
</html>