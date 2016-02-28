<html>
<head>
<title>クッキー情報</title>
</head>
<body>
<?php print_r($_COOKIE['email']); ?>
<form method="post" action="cookie2.php">
    メールアドレス：
    <input type="text" size="40" name="email" value="<?php echo $_COOKIE['email']; ?>">
    <input type="submit" value="送信">
</form>
</body>
</html>
    