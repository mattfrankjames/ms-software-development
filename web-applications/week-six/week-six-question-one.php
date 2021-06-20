<!-- Question 1 -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sample PHP File</title>
</head>
<body>
<header>
  <h1>Week Six | Question One</h1>
</header>
<?php
  $title = "PHP isn't as popular as it used to be";
  $subTitle = "Mostly because of React and Friends";
?>
<h2><?php echo $title ?></h2>
<h3><?php echo $subTitle ?></h3>
<script>
  function getUserInfo() {
    const userName = prompt('Please Enter Your Username');
    const passWord = prompt('Please Enter Your Password');
    if (userName.length > 1 && passWord.length > 1) {
      return userName, passWord;
    }
  }
  window.addEventListener('load', function() {
    getUserInfo();
  });
</script>
</body>
</html>