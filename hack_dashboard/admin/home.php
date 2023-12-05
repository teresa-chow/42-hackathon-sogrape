<?php
    include("../includes/db.inc.php");

    if (!$_SESSION["logged"])
        header("Location: ../index.php");
    else if (!$_SESSION["Admin"])
        header("Location: ../user/home.php");

    $sql = "SELECT * FROM wine";
    $result = mysqli_query( $conn, $sql);
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="../style.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <title>Sogrape Scraper</title>
</head>

<body>
    <main>
        <div class="w-screen h-screen p-0 m-0">
            <div class="flex">
                <div class="w-1/4 h-screen border-secondary border-0 border-e-2">
                    <div class="w-3/4 m-auto flex justify-center	">
                        <a href="index.php"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Logo_Sogrape_Original_Legacy_Wines.png/640px-Logo_Sogrape_Original_Legacy_Wines.png"
                            alt="" width="230em" /></a>
                    </div>
                    <div class="pt-12 border-secondary border-0 border-t-2 text-center">
                        <label for="cars">Wine</label>
                        <br>
                        <select class="w-3/4 border-secondary border-2 rounded mx-auto mb-8 py-2" name="cars" id="nameList" onchange="filterByName()">
                            <option value="Vinho" selected="selected"> All </option>
                            <option value="Vinho Rosé">Rosé</option>
                            <option value="Espumante">Rosé Sparkling</option>
                            <option value="Figos">Papa Figos</option>
                            <option value="Bolota">Trinca Bolotas</option>
                        </select>
                        <br>
                        <label for="cars">Store</label>
                        <br>
                        <select class="w-3/4 border-secondary border-2 rounded mx-auto mb-8 py-2" name="cars" id="storeList" onchange="filterByStore()">
                            <option value="Vinho" selected="selected"> All </option>
                            <option value="Corte">El Corte Ingles</option>
                            <option value="Inglés_Es">El Corte Ingles Es</option>
                            <option value="Continente">Continente</option>
                            <option value="Soares">Garrafeira Soares</option>
                        </select>
                        <br>
                        <label for="cars">Location</label>
                        <br>
                        <select class="w-3/4 border-secondary border-2 rounded mx-auto mb-3 py-2" name="cars" id="locationList" onchange="filterByLocation()">
                            <option value="Vinho" selected="selected"> Any </option>
                            <option value="por">Portugal</option>
                            <option value="sp">Spain</option>
                        </select>
						<br>
                        	<button  value="Refresh" onClick="location.reload();" class="mt-8 secondary w-2/4 rounded py-1 text-white">Refresh</button>
                        	<button  value="Refresh" onClick="location.href='./novo.php';" class="mt-12 secondary w-2/4 rounded py-2 text-white">Novo Vinho</button>
                    </div>
                </div>
                <div class="w-3/4 ms-4 py-8 h-screen overflow-auto">
                    <table class="w-4/5 mx-auto table-auto padding-x-4" id="myTable">
                        <thead>
                            <tr class="border-neutral-50 secondary text-center">
                                <th height="50">Name</th>
                                <th class="hover:cursor-pointer" onclick="sortTable(1)">Price</th>
                                <th>Store</th>
                                <th class="hover:cursor-pointer" onclick="sortTable(3)">Date</th>
                                <th>Location</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php while ($row = mysqli_fetch_assoc($result)) { ?>
                                <tr class="border-b-2 text-center">
                                    <td height="50" id="name">
                                        <?= $row["name"] ?>
                                    </td>
                                    <td id="price">
                                        <?= $row["price"] ?><?= $row["curr"] ?>
                                    </td>
                                    <td id="store">
                                        <?= $row["store"] ?>
                                    </td>
                                    <td id="date">
                                        <?= $row["date"] ?>
                                    </td>
                                    <td id="local">
                                        <?= $row["loc"] == "es" ? "Spain" : "Portugal" ?>
                                    </td>
                                    <td><button className="bg-gray-100"><a
                                                href="<?= "./more.php?ID=" . $row["id"] ?>"><i style="font-size:15px;color:#af5b2d" class="fa">&#xf067;</i> </a></button>
                                    </td>
                                </tr>
                            <?php } ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>
    <script>
        const filterByName = () =>{
            var input, filter, table, tr, td, i;
            input = document.getElementById("nameList");
            filter = input.value.toUpperCase();
            if(filter == "VINHO")
                filter = "";
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[0];
                if (td) {
                    if (td.innerHTML.toUpperCase().indexOf(filter) > -1) 
                        tr[i].style.display = "";
                    else 
                        tr[i].style.display = "none";
                }
            }
        }

        const filterByStore = () =>{
            var input, filter, table, tr, td, i;
            input = document.getElementById("storeList");
            filter = input.value.toUpperCase();
            if(filter == "VINHO")
                filter = "";
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[2];
                if (td) {
                    if (td.innerHTML.toUpperCase().indexOf(filter) > -1) 
                        tr[i].style.display = "";
                    else 
                        tr[i].style.display = "none";
                    
                }
            }
        }

        const filterByLocation = () =>{
            var input, filter, table, tr, td, i;
            input = document.getElementById("locationList");
            filter = input.value.toUpperCase();
            if(filter == "VINHO")
                filter = "";
            table = document.getElementById("myTable");
            tr = table.getElementsByTagName("tr");
            for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[4];
                if (td) {
                    if (td.innerHTML.toUpperCase().indexOf(filter) > -1) 
                        tr[i].style.display = "";
                    else 
                        tr[i].style.display = "none";
                }
            }
        }

		function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("td")[n];
      y = rows[i + 1].getElementsByTagName("td")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

</script>
</body>

</html>