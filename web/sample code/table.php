<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="3">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="table.css">
    
  </head>

  <body>
	 <?php
		$db = new SQLite3('/home/wa/Documents/PowerMeter/database.db');

		$results = $db->query('select * from backfill order by time desc limit 1');
		
	?>

	


    <div class="container">
                             
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Time</th>
            <th>Consumption</th>
          </tr>
        </thead>
        <tbody>
	<?php while ($row = $results->fetchArray()) { ?>
	  <tr>
              <td><?php echo 2?></td>
              <td><?php echo $row['time'] ?></td> 
              <td><?php echo $row['power'] ?></td> 
            </tr>
	      
	   <?php } ?>
	   
	

          

        </tbody>
      </table>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
  </body>

</html>



