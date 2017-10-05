

<?php
// para realizar la activacion del led
if ($_POST[LED]){ // condicional si se pulsa la acion
 $a- exec ("sudo python /var/www/html/led/led.py");
 echo $a;
}


?>

<form action="led.php" method="POST">
LED&nbsp<input type="submit" value="ON" name="LED">
</form>
