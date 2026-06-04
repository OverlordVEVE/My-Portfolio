<?php
session_start();

// Настройки
$upload_dir = 'uploads/';
$max_file_size = 5 * 1024 * 1024; // 5MB
$allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'image/jpg'];
$allowed_extensions = ['jpg', 'jpeg', 'png', 'gif'];

// ПРОСТАЯ ПРОВЕРКА КАПЧИ (через hidden поле)
$captcha_verified = isset($_POST['captcha_verified']) && $_POST['captcha_verified'] === '1';

if (!$captcha_verified) {
    // Сохраняем в сессии, что капча не пройдена
    $_SESSION['captcha_error'] = true;
    header('Location: index.html');
    exit();
}

// Создаем папку uploads, если её нет
if (!file_exists($upload_dir)) {
    mkdir($upload_dir, 0755, true);
}

// Проверяем, был ли загружен файл
if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !isset($_FILES['image'])) {
    die('Ошибка: файл не был загружен.');
}

$file = $_FILES['image'];
$description = htmlspecialchars($_POST['description'] ?? '');

// Проверка ошибок загрузки
if ($file['error'] !== UPLOAD_ERR_OK) {
    die('Ошибка при загрузке файла. Код ошибки: ' . $file['error']);
}

// Проверка размера файла
if ($file['size'] > $max_file_size) {
    die('Ошибка: размер файла превышает 5MB.');
}

// Получаем MIME-тип файла
$finfo = finfo_open(FILEINFO_MIME_TYPE);
$mime_type = finfo_file($finfo, $file['tmp_name']);
finfo_close($finfo);

// Проверяем MIME-тип
if (!in_array($mime_type, $allowed_types)) {
    die('Ошибка: недопустимый тип файла. Разрешены только JPG, PNG и GIF.');
}

// Получаем расширение файла
$file_extension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));

// Проверяем расширение файла
if (!in_array($file_extension, $allowed_extensions)) {
    die('Ошибка: недопустимое расширение файла.');
}

// Генерируем уникальное имя файла
$unique_name = uniqid('img_', true) . '_' . time() . '.' . $file_extension;
$target_file = $upload_dir . $unique_name;

// Проверяем, является ли файл изображением
$image_info = getimagesize($file['tmp_name']);
if (!$image_info) {
    die('Ошибка: файл не является изображением.');
}

// Перемещаем файл
if (!move_uploaded_file($file['tmp_name'], $target_file)) {
    die('Ошибка: не удалось сохранить файл.');
}

// Сохраняем информацию о файле
$_SESSION['last_upload'] = [
    'filename' => $unique_name,
    'original_name' => htmlspecialchars($file['name']),
    'description' => $description,
    'upload_time' => date('Y-m-d H:i:s')
];

// Перенаправляем на страницу просмотра
header('Location: view.php');
exit();
?>