<?php
session_start();

// Генерируем начальную капчу при первом заходе
if (!isset($_SESSION['captcha_code'])) {
    $chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
    $captcha = '';
    for ($i = 0; $i < 5; $i++) {
        $captcha .= $chars[rand(0, strlen($chars) - 1)];
    }
    $_SESSION['captcha_code'] = $captcha;
}

// Возвращаем капчу для JavaScript
header('Content-Type: application/json');
echo json_encode(['captcha' => $_SESSION['captcha_code']]);
?>