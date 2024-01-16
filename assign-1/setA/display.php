<?php
// Display preferences from cookies
$fontStyle = isset($_COOKIE['font_style']) ? $_COOKIE['font_style'] : 'Arial';
$fontSize = isset($_COOKIE['font_size']) ? $_COOKIE['font_size'] : 'medium';
$fontColor = isset($_COOKIE['font_color']) ? $_COOKIE['font_color'] : '#000000';
$bgColor = isset($_COOKIE['bg_color']) ? $_COOKIE['bg_color'] : '#ffffff';
?>

<html>
<head>
    <title>Display Preferences</title>
    <style>
        body {
            font-family: <?php echo $fontStyle; ?>;
            font-size: <?php echo $fontSize; ?>;
            color: <?php echo $fontColor; ?>;
            background-color: <?php echo $bgColor; ?>;
        }
    </style>
</head>
<body>
    <p>Font Style: <?php echo $fontStyle; ?></p>
    <p>Font Size: <?php echo $fontSize; ?></p>
    <p>Font Color: <?php echo $fontColor; ?></p>
    <p>Background Color: <?php echo $bgColor; ?></p>
    <p>This is the actual implementation with the new settings.</p>
</body>
</html>
