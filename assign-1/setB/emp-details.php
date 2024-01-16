<html>
<head>
    <title>Employee Details</title>
</head>
<body>
    <h2>Employee Details</h2>
    <form action="emp-details.php" method="post">
        Employee Number: <input type="text" name="eno" required><br>
        Employee Name: <input type="text" name="ename" required><br>
        Address: <input type="text" name="address" required><br>
        <input type="submit" value="Next">
    </form>
</body>
</html>

<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $_SESSION['emp-details'] = [
        'Eno' => $_POST['eno'],
        'Ename' => $_POST['ename'],
        'Address' => $_POST['address']
    ];

    header('Location: earning_details.php');
    exit;
}
?>


