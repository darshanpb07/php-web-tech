
<html>
<head>
    <title>Change Preferences</title>
</head>
<body>
    <form action="set_pref.php" method="post">
        Font Style:
        <select name="font_style">
            <option value="Arial">Arial</option>
            <option value="Verdana">Verdana</option>
            <option value="Times New Roman">Times New Roman</option>
        </select><br>

        Font Size:
        <select name="font_size">
            <option value="small">Small</option>
            <option value="medium">Medium</option>
            <option value="large">Large</option>
        </select><br>

        Font Color:
        <input type="text" name="font_color"><br>

        Background Color:
        <input type="text" name="bg_color"><br>

        <input type="submit" value="Save Preferences">
    </form>
</body>
</html>

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Set preferences in cookies
    setcookie('font_style', $_POST['font_style'], time() + 3600, '/');
    setcookie('font_size', $_POST['font_size'], time() + 3600, '/');
    setcookie('font_color', $_POST['font_color'], time() + 3600, '/');
    setcookie('bg_color', $_POST['bg_color'], time() + 3600, '/');

    // Redirect to the next page
    header('Location: display.php');
    exit;
}
?>
