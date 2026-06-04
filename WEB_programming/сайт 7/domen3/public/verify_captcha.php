<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    
    if (isset($data['captcha'])) {
        $user_captcha = strtoupper(trim($data['captcha']));
        
        // Проверяем капчу
        if (isset($_SESSION['captcha_code']) && $user_captcha === $_SESSION['captcha_code']) {
            $_SESSION['captcha_verified'] = true;
            $_SESSION['captcha_token'] = $user_captcha;
            
            // Генерируем новую капчу для следующего раза
            $chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
            $new_captcha = '';
            for ($i = 0; $i < 5; $i++) {
                $new_captcha .= $chars[rand(0, strlen($chars) - 1)];
            }
            $_SESSION['captcha_code'] = $new_captcha;
            
            echo json_encode([
                'success' => true, 
                'message' => 'Капча верна',
                'token' => $user_captcha
            ]);
        } else {
            // Генерируем новую капчу при ошибке
            $chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
            $new_captcha = '';
            for ($i = 0; $i < 5; $i++) {
                $new_captcha .= $chars[rand(0, strlen($chars) - 1)];
            }
            $_SESSION['captcha_code'] = $new_captcha;
            
            echo json_encode([
                'success' => false, 
                'message' => 'Неверная капча',
                'new_captcha' => $new_captcha
            ]);
        }
    } else {
        echo json_encode(['success' => false, 'message' => 'Капча не предоставлена']);
    }
}
?>