<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $_SESSION['customer_info'] = $_POST;
    header('Location: product_info.php');
    exit;
}
?>

<html>
<head>
    <title>Customer Information</title>
</head>
<body>
    <h2>Customer Information</h2>
    <form action="customer_info.php" method="post">
        Name: <input type="text" name="name" required><br>
        Address: <input type="text" name="address" required><br>
        Mobile Number: <input type="text" name="mobno" required><br>
        <input type="submit" value="Next">
    </form>
</body>
</html>
