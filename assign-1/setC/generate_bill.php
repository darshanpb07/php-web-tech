<?php
session_start();

if (!isset($_SESSION['customer_info']) || !isset($_SESSION['product_info']) || empty($_SESSION['product_info'])) 
{
    header('Location: customer_info.php');
    exit;
}
?>

<html>
<head>
    <title>Generate Bill</title>
</head>
<body>
    <h2>Bill for Customer</h2>
    <p><strong>Name:</strong> <?php echo $_SESSION['customer_info']['name']; ?></p>
    <p><strong>Address:</strong> <?php echo $_SESSION['customer_info']['address']; ?></p>
    <p><strong>Mobile Number:</strong> <?php echo $_SESSION['customer_info']['mobno']; ?></p>

    <h3>Product Information</h3>
    <table border="1">
        <tr>
            <th>Product Name</th>
            <th>Quantity</th>
            <th>Rate</th>
            <th>Total</th>
        </tr>
        <?php foreach ($_SESSION['product_info'] as $product) : ?>
            <tr>
                <td><?php echo $product['prodname']; ?></td>
                <td><?php echo $product['qty']; ?></td>
                <td><?php echo $product['rate']; ?></td>
                <td><?php echo $product['qty'] * $product['rate']; ?></td>
            </tr>
        <?php endforeach; ?>
    </table>

    <p><strong>Total Amount:</strong> <?php echo isset($_SESSION['total_amount']) ? $_SESSION['total_amount'] : 0; ?></p>

    <?php
    unset($_SESSION['customer_info']);
    unset($_SESSION['product_info']);
    unset($_SESSION['total_amount']);
    ?>
</body>
</html>
