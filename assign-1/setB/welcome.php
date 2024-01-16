<?php
session_start();

if (!isset($_SESSION['logged_in']) || !$_SESSION['logged_in']) 
{
    header('Location: login.php');
    exit;
}
?>

<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h2>Welcome</h2>
    <p>You have successfully logged in!</p>
</body>
</html>
