<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $_SESSION['product_info'][] = $_POST;
    $totalAmount = isset($_SESSION['total_amount']) ? $_SESSION['total_amount'] : 0;
    $totalAmount += ($_POST['qty'] * $_POST['rate']);
    $_SESSION['total_amount'] = $totalAmount;

    header('Location: product_info.php');
    exit;
}
?>

<html>
<head>
    <title>Product Information</title>
</head>
<body>
    <h2>Product Information</h2>
    <form action="product_info.php" method="post">
        Product Name: <input type="text" name="prodname" required><br>
        Quantity: <input type="number" name="qty" required><br>
        Rate: <input type="number" name="rate" required><br>
        <input type="submit" value="Add Product">
    </form>

    <h2>Bill Summary</h2>
    <p>Total Amount: <?php echo isset($_SESSION['total_amount']) ? $_SESSION['total_amount'] : 0; ?></p>
    <p><a href="generate_bill.php">Generate Bill</a></p>
</body>
</html>
