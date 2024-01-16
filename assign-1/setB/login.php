<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form action="login.php" method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $username = $_POST['username'];
    $password = $_POST['password'];

    $correctUsername = 'admin';
    $correctPassword = 'pswd';

    if ($username === $correctUsername && $password === $correctPassword) 
    {
        $_SESSION['logged_in'] = true;
        header('Location: welcome.php');
        exit;
    } 
    else 
    {
        echo"Login Failed!";
        if (!isset($_SESSION['login_attempts'])) 
            $_SESSION['login_attempts'] = 1;
        else 
            $_SESSION['login_attempts']++;

        if ($_SESSION['login_attempts'] > 3) 
        {
            echo "Login failed. You have exceeded the maximum number of attempts.";
            exit;
        }
    }
}
?>


