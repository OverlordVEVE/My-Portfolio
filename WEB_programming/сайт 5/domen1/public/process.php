<?php
// Устанавливаем кодировку
header('Content-Type: text/html; charset=utf-8');

// Функция для безопасного вывода данных
function safe_output($data) {
    if (is_array($data)) {
        return array_map('safe_output', $data);
    }
    if (is_string($data)) {
        return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
    }
    return $data;
}

// Функция для получения следующего номера файла
function get_next_file_number() {
    $counter_file = 'counter.txt';
    $counter = 1;
    
    if (file_exists($counter_file)) {
        $counter = (int)file_get_contents($counter_file);
        $counter++;
    }
    
    file_put_contents($counter_file, $counter);
    return $counter;
}

// Обработка данных формы
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Очищаем и валидируем данные
    $lastname = safe_output($_POST['lastname'] ?? '');
    $firstname = safe_output($_POST['firstname'] ?? '');
    $info = safe_output($_POST['info'] ?? '');
    $gender = safe_output($_POST['gender'] ?? '');
    $city = safe_output($_POST['city'] ?? '');
    $consent = safe_output($_POST['consent'] ?? 'не согласен');
    
    // Обработка массива домашних животных
    $pets = [];
    if (!empty($_POST['pets']) && is_array($_POST['pets'])) {
        $pets = safe_output($_POST['pets']);
    } else {
        $pets = ['Не указано'];
    }
    
    // Обработка массива увлечений
    $hobbies = [];
    if (!empty($_POST['hobbies']) && is_array($_POST['hobbies'])) {
        $hobbies = safe_output($_POST['hobbies']);
    } else {
        $hobbies = ['Не указано'];
    }
    
    // Получаем номер для нового файла
    $file_number = get_next_file_number();
    $filename = "otvet{$file_number}.txt";
    
    // Формируем строку для записи в файл
    $data_to_save = "=== Анкета №{$file_number} от " . date('d.m.Y H:i:s') . " ===\n";
    $data_to_save .= "Фамилия: $lastname\n";
    $data_to_save .= "Имя: $firstname\n";
    $data_to_save .= "Информация о пользователе: $info\n";
    $data_to_save .= "Пол: $gender\n";
    $data_to_save .= "Город рождения: $city\n";
    $data_to_save .= "Домашние животные: " . implode(', ', $pets) . "\n";
    $data_to_save .= "Увлечения: " . implode(', ', $hobbies) . "\n";
    $data_to_save .= "Согласие на обработку данных: $consent\n";
    $data_to_save .= "=================================\n\n";
    
    // Записываем данные в файл с номером
    $file_saved = false;
    
    if (file_put_contents($filename, $data_to_save, LOCK_EX)) {
        $file_saved = true;
    }
    
    // Выводим HTML-страницу с результатами
    ?>
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Результаты анкеты</title>
        <style>
            * {
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }
            
            body {
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            
            .result-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            
            h1 {
                color: #4CAF50;
                text-align: center;
                margin-bottom: 30px;
            }
            
            .success-message {
                background-color: #dff0d8;
                border: 1px solid #d6e9c6;
                color: #3c763d;
                padding: 15px;
                border-radius: 4px;
                margin-bottom: 20px;
                text-align: center;
            }
            
            .file-info {
                background-color: #e7f3fe;
                border: 1px solid #b3d9ff;
                color: #31708f;
                padding: 15px;
                border-radius: 4px;
                margin-bottom: 20px;
                text-align: center;
            }
            
            .data-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            
            .data-table th,
            .data-table td {
                padding: 12px 15px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }
            
            .data-table th {
                background-color: #f8f9fa;
                color: #333;
                font-weight: bold;
                width: 30%;
            }
            
            .data-table tr:hover {
                background-color: #f5f5f5;
            }
            
            .back-button {
                display: inline-block;
                background-color: #337ab7;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 4px;
                margin-top: 10px;
                transition: background-color 0.3s;
                border: none;
                cursor: pointer;
                font-size: 14px;
            }
            
            .back-button:hover {
                background-color: #286090;
            }
            
            .actions {
                text-align: center;
                margin-top: 30px;
                display: flex;
                flex-direction: column;
                gap: 10px;
                align-items: center;
            }
            
            .empty-field {
                color: #999;
                font-style: italic;
            }
            
            .section {
                margin: 20px 0;
                padding: 15px;
                background-color: #f8f9fa;
                border-radius: 4px;
            }
            
            .section h3 {
                color: #333;
                margin-top: 0;
                padding-bottom: 10px;
                border-bottom: 2px solid #4CAF50;
            }
            
            .error-message {
                background-color: #f2dede;
                border: 1px solid #ebccd1;
                color: #a94442;
                padding: 15px;
                border-radius: 4px;
                margin: 20px 0;
                text-align: center;
            }
            
            .file-list {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 15px;
                margin-top: 20px;
            }
            
            .file-list h4 {
                margin-top: 0;
                color: #555;
            }
            
            .file-item {
                padding: 5px 0;
                border-bottom: 1px solid #eee;
            }
            
            .file-item:last-child {
                border-bottom: none;
            }
            
            .file-link {
                color: #337ab7;
                text-decoration: none;
            }
            
            .file-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="result-container">
            <h1>✅ Данные анкеты успешно получены!</h1>
            
            <?php if ($file_saved): ?>
            <div class="success-message">
                <strong>✓ Данные успешно сохранены!</strong>
            </div>
            
            <div class="file-info">
                <p><strong>Файл создан:</strong> <?php echo $filename; ?></p>
                <p><strong>Номер анкеты:</strong> <?php echo $file_number; ?></p>
                <p><strong>Дата сохранения:</strong> <?php echo date('d.m.Y H:i:s'); ?></p>
            </div>
            <?php else: ?>
            <div class="error-message">
                <strong>⚠ Ошибка при сохранении данных в файл</strong>
                <p>Пожалуйста, проверьте права доступа к папке.</p>
            </div>
            <?php endif; ?>
            
            <div class="section">
                <h3>Основная информация</h3>
                <table class="data-table">
                    <tr>
                        <th>Фамилия:</th>
                        <td><?php echo $lastname ?: '<span class="empty-field">Не указано</span>'; ?></td>
                    </tr>
                    <tr>
                        <th>Имя:</th>
                        <td><?php echo $firstname ?: '<span class="empty-field">Не указано</span>'; ?></td>
                    </tr>
                    <tr>
                        <th>Пол:</th>
                        <td><?php echo $gender ?: '<span class="empty-field">Не указано</span>'; ?></td>
                    </tr>
                    <tr>
                        <th>Город рождения:</th>
                        <td><?php echo $city ?: '<span class="empty-field">Не указано</span>'; ?></td>
                    </tr>
                </table>
            </div>
            
            <div class="section">
                <h3>Дополнительная информация</h3>
                <table class="data-table">
                    <tr>
                        <th>Информация о пользователе:</th>
                        <td><?php echo $info ?: '<span class="empty-field">Не указано</span>'; ?></td>
                    </tr>
                </table>
            </div>
            
            <div class="section">
                <h3>Домашние животные</h3>
                <table class="data-table">
                    <tr>
                        <th>Список:</th>
                        <td>
                            <?php if (is_array($pets)): ?>
                                <ul style="margin: 0; padding-left: 20px;">
                                    <?php foreach ($pets as $pet): ?>
                                        <li><?php echo $pet; ?></li>
                                    <?php endforeach; ?>
                                </ul>
                            <?php else: ?>
                                <span class="empty-field">Не указано</span>
                            <?php endif; ?>
                        </td>
                    </tr>
                </table>
            </div>
            
            <div class="section">
                <h3>Увлечения</h3>
                <table class="data-table">
                    <tr>
                        <th>Список:</th>
                        <td>
                            <?php if (is_array($hobbies)): ?>
                                <ul style="margin: 0; padding-left: 20px;">
                                    <?php foreach ($hobbies as $hobby): ?>
                                        <li><?php echo $hobby; ?></li>
                                    <?php endforeach; ?>
                                </ul>
                            <?php else: ?>
                                <span class="empty-field">Не указано</span>
                            <?php endif; ?>
                        </td>
                    </tr>
                </table>
            </div>
            
            <div class="section">
                <h3>Согласие на обработку данных</h3>
                <table class="data-table">
                    <tr>
                        <th>Статус:</th>
                        <td>
                            <strong style="color: <?php echo $consent === 'согласен' ? '#4CAF50' : '#f44336'; ?>">
                                <?php echo $consent === 'согласен' ? '✓ ' . $consent : '✗ ' . $consent; ?>
                            </strong>
                        </td>
                    </tr>
                </table>
            </div>
            
            <div class="actions">
                <?php if ($file_saved): ?>
                <div style="margin-bottom: 20px; text-align: center;">
                    <a href="<?php echo $filename; ?>" class="back-button" download>
                        📥 Скачать файл <?php echo $filename; ?>
                    </a>
                    <a href="<?php echo $filename; ?>" class="back-button" target="_blank">
                        👁 Просмотреть файл
                    </a>
                </div>
                <?php endif; ?>
                
                <div>
                    <button onclick="window.location.href='form.html'" class="back-button">
                        ← Заполнить новую анкету
                    </button>
                    <button onclick="window.history.back()" class="back-button">
                        ↩ Вернуться назад
                    </button>
                </div>
            </div>
            
            <?php
            // Показываем список всех файлов с ответами
            $files = glob('otvet*.txt');
            if (!empty($files)) {
                rsort($files); // Сортируем по убыванию (последние файлы первыми)
                echo '<div class="file-list">';
                echo '<h4>📁 Все сохраненные анкеты:</h4>';
                foreach ($files as $file) {
                    $file_name = basename($file);
                    $file_size = filesize($file);
                    $file_date = date('d.m.Y H:i', filemtime($file));
                    echo '<div class="file-item">';
                    echo '<a href="' . $file . '" class="file-link" target="_blank">' . $file_name . '</a>';
                    echo ' <span style="color: #666; font-size: 0.9em;">(' . $file_size . ' байт, ' . $file_date . ')</span>';
                    echo '</div>';
                }
                echo '</div>';
            }
            ?>
        </div>
        
        <script>
            // Автоматическое обновление списка файлов при возврате на страницу
            if (window.history.replaceState) {
                window.history.replaceState(null, null, window.location.href);
            }
        </script>
    </body>
    </html>
    <?php
} else {
    // Если кто-то попал на эту страницу не через POST-запрос
    ?>
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Ошибка доступа</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                text-align: center;
            }
            .error {
                background-color: #f2dede;
                border: 1px solid #ebccd1;
                color: #a94442;
                padding: 20px;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            .back-button {
                display: inline-block;
                background-color: #337ab7;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 4px;
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <div class="error">
            <h2>Ошибка доступа</h2>
            <p>Данная страница предназначена для обработки данных формы.</p>
            <p>Пожалуйста, заполните форму для отправки данных.</p>
        </div>
        <a href="form.html" class="back-button">Вернуться к форме</a>
        <a href="javascript:history.back()" class="back-button">Назад</a>
    </body>
    </html>
    <?php
}
?>