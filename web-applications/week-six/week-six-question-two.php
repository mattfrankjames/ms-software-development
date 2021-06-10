<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Week Six | Question Two</title>
</head>
<body>
<?php
$imageSources = array(0 => 'image-one.jpg', 1 => 'image-two.jpg', 2 => 'image-three.jpg', 3 => 'image-four.jpg');
$userPreference = true;

switch($userPreference) {
  case(true):
    for ($i = 0; $i < count($imageSources); $i += 1) {
      echo "<img src='".$imageSources[$i]."'/>"
    }
    break;
  case(false):
    echo "<p>You have chosen no images.</p>"
    break;
}
?>

</body>
</html>