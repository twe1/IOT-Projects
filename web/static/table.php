<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="2">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="table.css">
    
  </head>

  <body>
	 <?php
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "light";

		$db = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
		$results = $db->query('select * from tb order by time desc limit 1');

	?>

	


    <div class="container">
                             
      <table class="table">
        <thead>
          <tr>
            <th>Time</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
	<?php while ($row = $results->fetch_assoc()) { ?>
	  <tr>
              <td><?php echo $row["time"] ?></td> 
              <td><?php echo $row["status"] ?></td> 
            </tr>
	      
	   <?php } 

     ?>

        
	   
	

          

        </tbody>
      </table>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
  </body>

</html>



