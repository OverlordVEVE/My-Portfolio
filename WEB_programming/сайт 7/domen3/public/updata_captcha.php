<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    
    if (isset($data['captcha'])) {
        $_SESSION['captcha_code'] = strtoupper(trim($data['captcha']));
        echo json_encode(['success' => true]);
    } else {
        echo json_encode(['success' => false, 'message' => 'Капча не предоставлена']);
    }
}
?>