<?php
session_start();

if (!isset($_SESSION['emp-details']) || !isset($_SESSION['earning_details'])) 
{
    header('Location: employee_details.php');
    exit;
}

$employeeInfo = array_merge($_SESSION['emp-details'], $_SESSION['earning_details']);
$totalEarnings = $employeeInfo['Basic'] + $employeeInfo['DA'] + $employeeInfo['HRA'];
$employeeInfo['Total'] = $totalEarnings;
?>

<html>
<head>
    <title>Employee Information</title>
</head>
<body>
    <h2>Employee Information</h2>
    <?php echo "<p> Employee No: ".$employeeInfo['Eno'];
          echo "<br>Employee Name: ".$employeeInfo['Ename'];
          echo "<br>Address: ".$employeeInfo['Address'];
          echo "<br>Basic: ".$employeeInfo['Basic'];
          echo "<br>DA: ".$employeeInfo['DA'];
          echo "<br>HRA: ".$employeeInfo['HRA'];
          echo "<br>Total Earnings: ".$employeeInfo['Total'];
          echo "</p>";
    ?>
</body>
</html>
