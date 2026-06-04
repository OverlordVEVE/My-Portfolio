<?php
session_start();

// Настройки CAPTCHA
$captcha_length = 6;
$width = 300;  // Увеличил ширину для 6 символов
$height = 100; // Увеличил высоту
$font_size = 40; // Увеличил размер шрифта

// Путь к шрифту
$font_file = 'captcha_fonts/arial.ttf'; // или arial.otf

// Функция генерации текста CAPTCHA (только строчные буквы и цифры)
function generateCaptchaText($length = 6) {
    // Только строчные английские буквы (без заглавных) и цифры 1-9
    $letters = 'abcdefghjkmnpqrstuvwxyz'; // строчные, исключаем похожие буквы
    $numbers = '23456789'; // цифры 1-9, исключаем 0 и 1
    $chars = $letters . $numbers;
    
    $text = '';
    for ($i = 0; $i < $length; $i++) {
        $text .= $chars[rand(0, strlen($chars) - 1)];
    }
    return $text;
}

// Генерируем новую CAPTCHA при каждом обновлении
// Если нужна новая капча (например, при нажатии кнопки обновления)
if (isset($_GET['refresh'])) {
    $_SESSION['captcha_text'] = generateCaptchaText($captcha_length);
}

// Если текста CAPTCHA еще нет в сессии
if (!isset($_SESSION['captcha_text'])) {
    $_SESSION['captcha_text'] = generateCaptchaText($captcha_length);
}

$captcha_text = $_SESSION['captcha_text'];

// Создаем изображение
$image = imagecreatetruecolor($width, $height);

// Цвета
$bg_color = imagecolorallocate($image, 255, 255, 255); // Белый фон
$text_color = imagecolorallocate($image, 40, 40, 40);  // Темно-серый текст

// Заполняем фон
imagefilledrectangle($image, 0, 0, $width, $height, $bg_color);

// Добавляем легкий шум (точки)
for ($i = 0; $i < 100; $i++) {
    $dot_color = imagecolorallocate($image, rand(200, 230), rand(200, 230), rand(200, 230));
    imagesetpixel($image, rand(0, $width), rand(0, $height), $dot_color);
}

// Рисуем текст
if (file_exists($font_file) && function_exists('imagettftext')) {
    try {
        // Вычисляем общую ширину текста
        $bbox = imagettfbbox($font_size, 0, $font_file, $captcha_text);
        $text_width = $bbox[2] - $bbox[0];
        $text_height = $bbox[1] - $bbox[7];
        
        // Начальная позиция для центрирования
        $start_x = ($width - $text_width) / 2;
        $base_y = ($height + $text_height) / 2;
        
        // Рисуем каждый символ отдельно с правильным позиционированием
        $current_x = $start_x;
        
        for ($i = 0; $i < strlen($captcha_text); $i++) {
            $char = $captcha_text[$i];
            
            // Получаем ширину текущего символа
            $char_bbox = imagettfbbox($font_size, 0, $font_file, $char);
            $char_width = $char_bbox[2] - $char_bbox[0];
            
            // Небольшой случайный наклон
            $angle = rand(-8, 8);
            
            // Небольшое случайное смещение по вертикали
            $char_y = $base_y + rand(-5, 5);
            
            // Рисуем символ
            imagettftext($image, $font_size, $angle, $current_x, $char_y, $text_color, $font_file, $char);
            
            // Сдвигаем позицию для следующего символа
            $current_x += $char_width + 5; // +5 пикселей между символами
        }
        
    } catch (Exception $e) {
        // Если произошла ошибка, используем встроенный шрифт
        $font_file = null;
    }
}

// Если шрифт не найден, используем встроенный
if (!$font_file) {
    $font_size = 5;
    $text_width = imagefontwidth($font_size) * strlen($captcha_text);
    $text_height = imagefontheight($font_size);
    $x = ($width - $text_width) / 2;
    $y = ($height - $text_height) / 2;
    
    imagestring($image, $font_size, $x, $y, $captcha_text, $text_color);
}

// Добавляем несколько тонких линий для защиты
for ($i = 0; $i < 4; $i++) {
    $line_color = imagecolorallocate($image, rand(180, 220), rand(180, 220), rand(180, 220));
    imageline($image, 
        rand(0, $width), rand(0, $height), 
        rand(0, $width), rand(0, $height), 
        $line_color);
}

// Устанавливаем заголовки для предотвращения кэширования
header('Content-Type: image/png');
header('Cache-Control: no-cache, no-store, must-revalidate');
header('Pragma: no-cache');
header('Expires: 0');

// Выводим изображение
imagepng($image);
imagedestroy($image);
exit();
?>