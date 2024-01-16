<html>
<head>
    <title>Earning Details</title>
</head>
<body>
    <h2>Earning Details</h2>
    <form action="earning_details.php" method="post">
        Basic: <input type="text" name="basic" required><br>
        DA: <input type="text" name="da" required><br>
        HRA: <input type="text" name="hra" required><br>
        <input type="submit" value="Next">
    </form>
</body>
</html>

<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $_SESSION['earning_details'] = 
    [   'Basic' => $_POST['basic'],
        'DA' => $_POST['da'],
        'HRA' => $_POST['hra'] ];

    header('Location: emp-display.php');
    exit;
}
?>


