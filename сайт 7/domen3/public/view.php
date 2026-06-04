<?php
session_start();
$upload_dir = 'uploads/';

// Создаем папку, если её нет
if (!file_exists($upload_dir)) {
    mkdir($upload_dir, 0755, true);
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Просмотр изображений</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Галерея изображений</h1>
        
        <div class="navigation">
            <a href="index.html" class="btn">Загрузить новое изображение</a>
        </div>
        
        <!-- Последнее загруженное изображение -->
        <?php if (isset($_SESSION['last_upload'])): ?>
        <div class="last-upload">
            <h2>Только что загруженное изображение:</h2>
            <div class="image-card">
                <?php
                $image_path = $upload_dir . $_SESSION['last_upload']['filename'];
                if (file_exists($image_path)): 
                ?>
                <img src="<?= htmlspecialchars($image_path) ?>" 
                     alt="<?= htmlspecialchars($_SESSION['last_upload']['original_name']) ?>">
                <?php else: ?>
                <div style="padding: 20px; background: #f8d7da; color: #721c24;">
                    Изображение не найдено
                </div>
                <?php endif; ?>
                <div class="image-info">
                    <h3><?= htmlspecialchars($_SESSION['last_upload']['original_name']) ?></h3>
                    <p><strong>Загружено:</strong> <?= htmlspecialchars($_SESSION['last_upload']['upload_time']) ?></p>
                    <?php if (!empty($_SESSION['last_upload']['description'])): ?>
                    <p><strong>Описание:</strong> <?= htmlspecialchars($_SESSION['last_upload']['description']) ?></p>
                    <?php endif; ?>
                </div>
            </div>
        </div>
        <?php endif; ?>
        
        <!-- Все предыдущие изображения -->
        <div class="previous-uploads">
            <h2>Ранее загруженные изображения:</h2>
            <div class="gallery">
                <?php
                // Получаем все файлы из папки uploads
                $files = scandir($upload_dir);
                $images = array_diff($files, ['.', '..']);
                
                if (count($images) > 0) {
                    // Сортируем по времени изменения (новые первыми)
                    usort($images, function($a, $b) use ($upload_dir) {
                        return filemtime($upload_dir . $b) - filemtime($upload_dir . $a);
                    });
                    
                    // Пропускаем последнее загруженное изображение, если оно есть
                    if (isset($_SESSION['last_upload'])) {
                        $last_filename = $_SESSION['last_upload']['filename'];
                        $images = array_filter($images, function($img) use ($last_filename) {
                            return $img !== $last_filename;
                        });
                    }
                    
                    foreach ($images as $image) {
                        $file_path = $upload_dir . $image;
                        
                        if (!file_exists($file_path)) {
                            continue;
                        }
                        
                        $file_info = [
                            'name' => $image,
                            'size' => filesize($file_path),
                            'upload_time' => date('Y-m-d H:i:s', filemtime($file_path))
                        ];
                        
                        // Проверяем, является ли файл изображением
                        if (@getimagesize($file_path)) {
                            echo '<div class="image-card">';
                            echo '<img src="' . htmlspecialchars($file_path) . '" alt="' . htmlspecialchars($image) . '">';
                            echo '<div class="image-info">';
                            echo '<h3>' . htmlspecialchars($image) . '</h3>';
                            echo '<p><strong>Загружено:</strong> ' . htmlspecialchars($file_info['upload_time']) . '</p>';
                            echo '<p><strong>Размер:</strong> ' . round($file_info['size'] / 1024, 2) . ' KB</p>';
                            echo '</div>';
                            echo '</div>';
                        }
                    }
                } else {
                    echo '<p class="no-images">Нет загруженных изображений.</p>';
                }
                
                // Очищаем последнюю загрузку после отображения
                unset($_SESSION['last_upload']);
                ?>
            </div>
        </div>
    </div>
</body>
</html>