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
    
    if (file_exists($counter_file)) {
        $counter = (int)file_get_contents($counter_file);
        $counter++;
    } else {
        $counter = 1;
    }
    
    file_put_contents($counter_file, $counter);
    return $counter;
}

// Функция для получения списка файлов
function get_answer_files() {
    $files = glob('otvet*.txt');
    $fileList = [];
    
    foreach ($files as $file) {
        if (is_file($file)) {
            $filename = basename($file);
            $filesize = filesize($file);
            $filemtime = filemtime($file);
            
            // Извлекаем номер из имени файла
            preg_match('/otvet(\d+)\.txt/', $filename, $matches);
            $number = isset($matches[1]) ? (int)$matches[1] : 0;
            
            $fileList[] = [
                'name' => $filename,
                'number' => $number,
                'size' => $filesize,
                'date' => date('d.m.Y H:i', $filemtime)
            ];
        }
    }
    
    // Сортируем по номеру (по убыванию - последние файлы первыми)
    usort($fileList, function($a, $b) {
        return $b['number'] - $a['number'];
    });
    
    return $fileList;
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
    
    // Записываем данные в файл
    $file_saved = false;
    
    if (file_put_contents($filename, $data_to_save, LOCK_EX)) {
        $file_saved = true;
    }
    
    // Получаем список всех файлов для отображения
    $all_files = get_answer_files();
    
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
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            
            body {
                max-width: 900px;
                margin: 20px auto;
                padding: 20px;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
            }
            
            .result-container {
                background-color: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            }
            
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
                padding-bottom: 20px;
                border-bottom: 2px solid #3498db;
            }
            
            .success-message {
                background: linear-gradient(to right, #d4edda, #c3e6cb);
                border: 1px solid #c3e6cb;
                color: #155724;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 25px;
                text-align: center;
                font-size: 1.1em;
            }
            
            .file-info {
                background: linear-gradient(to right, #d1ecf1, #bee5eb);
                border: 1px solid #bee5eb;
                color: #0c5460;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 30px;
                text-align: center;
            }
            
            .file-info p {
                margin: 8px 0;
                font-size: 1.05em;
            }
            
            .data-table {
                width: 100%;
                border-collapse: separate;
                border-spacing: 0;
                margin-top: 20px;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            }
            
            .data-table th,
            .data-table td {
                padding: 16px 20px;
                text-align: left;
                border-bottom: 1px solid #eaeaea;
            }
            
            .data-table th {
                background-color: #f8fafc;
                color: #2c3e50;
                font-weight: 600;
                width: 35%;
                font-size: 1.05em;
            }
            
            .data-table tr:last-child td {
                border-bottom: none;
            }
            
            .data-table tr:hover {
                background-color: #f8f9fa;
            }
            
            .back-button {
                display: inline-block;
                background: linear-gradient(to right, #3498db, #2980b9);
                color: white;
                padding: 14px 28px;
                text-decoration: none;
                border-radius: 8px;
                margin: 8px;
                transition: all 0.3s ease;
                border: none;
                cursor: pointer;
                font-size: 16px;
                font-weight: 600;
                box-shadow: 0 4px 6px rgba(52, 152, 219, 0.2);
            }
            
            .back-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(52, 152, 219, 0.3);
                background: linear-gradient(to right, #2980b9, #3498db);
            }
            
            .back-button.secondary {
                background: linear-gradient(to right, #95a5a6, #7f8c8d);
                box-shadow: 0 4px 6px rgba(149, 165, 166, 0.2);
            }
            
            .back-button.secondary:hover {
                background: linear-gradient(to right, #7f8c8d, #95a5a6);
                box-shadow: 0 6px 12px rgba(149, 165, 166, 0.3);
            }
            
            .back-button.success {
                background: linear-gradient(to right, #2ecc71, #27ae60);
                box-shadow: 0 4px 6px rgba(46, 204, 113, 0.2);
            }
            
            .back-button.success:hover {
                background: linear-gradient(to right, #27ae60, #2ecc71);
                box-shadow: 0 6px 12px rgba(46, 204, 113, 0.3);
            }
            
            .actions {
                text-align: center;
                margin-top: 40px;
                padding-top: 30px;
                border-top: 2px solid #ecf0f1;
            }
            
            .empty-field {
                color: #95a5a6;
                font-style: italic;
            }
            
            .section {
                margin: 30px 0;
                padding: 25px;
                background-color: #f8fafc;
                border-radius: 12px;
                border-left: 5px solid #3498db;
            }
            
            .section h3 {
                color: #2c3e50;
                margin-top: 0;
                margin-bottom: 20px;
                font-size: 1.4em;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            
            .section h3 i {
                color: #3498db;
            }
            
            .error-message {
                background: linear-gradient(to right, #f8d7da, #f5c6cb);
                border: 1px solid #f5c6cb;
                color: #721c24;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
            }
            
            .file-list {
                background-color: #fff;
                border: 1px solid #e0e0e0;
                border-radius: 10px;
                padding: 20px;
                margin-top: 30px;
            }
            
            .file-list h4 {
                margin-top: 0;
                color: #2c3e50;
                margin-bottom: 15px;
                font-size: 1.2em;
            }
            
            .file-item {
                padding: 12px 15px;
                border-bottom: 1px solid #eee;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .file-item:last-child {
                border-bottom: none;
            }
            
            .file-link {
                color: #3498db;
                text-decoration: none;
                font-weight: 500;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            
            .file-link:hover {
                color: #2980b9;
                text-decoration: underline;
            }
            
            .status-badge {
                display: inline-block;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 0.85em;
                font-weight: 600;
                margin-left: 10px;
            }
            
            .status-agreed {
                background-color: #d4edda;
                color: #155724;
            }
            
            .status-disagreed {
                background-color: #f8d7da;
                color: #721c24;
            }
            
            ul {
                margin: 0;
                padding-left: 25px;
            }
            
            li {
                margin-bottom: 8px;
                line-height: 1.5;
            }
            
            .refresh-btn {
                background: linear-gradient(to right, #f39c12, #e67e22);
                margin: 10px;
                padding: 10px 20px;
                font-size: 0.9em;
            }
            
            .refresh-btn:hover {
                background: linear-gradient(to right, #e67e22, #f39c12);
            }
            
            .no-files {
                text-align: center;
                color: #95a5a6;
                padding: 20px;
                font-style: italic;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body>
        <div class="result-container">
            <h1><i class="fas fa-check-circle" style="color: #2ecc71;"></i> Анкета успешно сохранена!</h1>
            
            <?php if ($file_saved): ?>
            <div class="success-message">
                <i class="fas fa-save fa-lg"></i> <strong>Данные успешно сохранены в системе</strong>
            </div>
            
            <div class="file-info">
                <p><i class="fas fa-file-alt"></i> <strong>Файл создан:</strong> <?php echo $filename; ?></p>
                <p><i class="fas fa-hashtag"></i> <strong>Номер анкеты:</strong> #<?php echo $file_number; ?></p>
                <p><i class="fas fa-calendar-check"></i> <strong>Дата сохранения:</strong> <?php echo date('d.m.Y H:i:s'); ?></p>
            </div>
            <?php else: ?>
            <div class="error-message">
                <i class="fas fa-exclamation-triangle fa-lg"></i> <strong>Ошибка при сохранении данных</strong>
                <p style="margin-top: 10px;">Пожалуйста, проверьте права доступа к папке или обратитесь к администратору.</p>
            </div>
            <?php endif; ?>
            
            <div class="section">
                <h3><i class="fas fa-user-circle"></i> Основная информация</h3>
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
                <h3><i class="fas fa-info-circle"></i> Дополнительная информация</h3>
                <table class="data-table">
                    <tr>
                        <th>Информация о пользователе:</th>
                        <td><?php echo $info ?: '<span class="empty-field">Не указано</span>'; ?></td>
                    </tr>
                </table>
            </div>
            
            <div class="section">
                <h3><i class="fas fa-paw"></i> Домашние животные</h3>
                <table class="data-table">
                    <tr>
                        <th>Список:</th>
                        <td>
                            <?php if (is_array($pets)): ?>
                                <ul>
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
                <h3><i class="fas fa-heart"></i> Увлечения</h3>
                <table class="data-table">
                    <tr>
                        <th>Список:</th>
                        <td>
                            <?php if (is_array($hobbies)): ?>
                                <ul>
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
                <h3><i class="fas fa-shield-alt"></i> Согласие на обработку данных</h3>
                <table class="data-table">
                    <tr>
                        <th>Статус:</th>
                        <td>
                            <strong style="color: <?php echo $consent === 'согласен' ? '#27ae60' : '#e74c3c'; ?>;">
                                <?php if ($consent === 'согласен'): ?>
                                    <i class="fas fa-check-circle"></i> 
                                <?php else: ?>
                                    <i class="fas fa-times-circle"></i> 
                                <?php endif; ?>
                                <?php echo $consent; ?>
                            </strong>
                            <span class="status-badge <?php echo $consent === 'согласен' ? 'status-agreed' : 'status-disagreed'; ?>">
                                <?php echo $consent === 'согласен' ? 'Согласие получено' : 'Согласие отсутствует'; ?>
                            </span>
                        </td>
                    </tr>
                </table>
            </div>
            
            <div class="actions">
                <a href="index.html" class="back-button">
                    <i class="fas fa-home"></i> На главную
                </a>
                <a href="forms.html" class="back-button success">
                    <i class="fas fa-plus-circle"></i> Новая анкета
                </a>
                <?php if ($file_saved): ?>
                <a href="<?php echo $filename; ?>" class="back-button secondary" target="_blank">
                    <i class="fas fa-eye"></i> Просмотреть файл
                </a>
                <a href="<?php echo $filename; ?>" class="back-button" download>
                    <i class="fas fa-download"></i> Скачать файл
                </a>
                <?php endif; ?>
                
                <button onclick="refreshFileList()" class="back-button refresh-btn">
                    <i class="fas fa-sync-alt"></i> Обновить список
                </button>
            </div>
            
            <!-- Список всех файлов -->
            <div class="file-list" id="file-list">
                <h4><i class="fas fa-folder-open"></i> Все сохраненные анкеты:</h4>
                <div id="files-container">
                    <?php if (!empty($all_files)): ?>
                        <?php foreach ($all_files as $fileInfo): ?>
                            <?php 
                            $file_size_kb = round($fileInfo['size'] / 1024, 2);
                            $file_number = $fileInfo['number'];
                            ?>
                            <div class="file-item" data-file="<?php echo $fileInfo['name']; ?>">
                                <div>
                                    <a href="<?php echo $fileInfo['name']; ?>" class="file-link" target="_blank">
                                        <i class="fas fa-file-text"></i> <?php echo $fileInfo['name']; ?>
                                    </a>
                                    <span style="color: #7f8c8d; font-size: 0.9em;">(<?php echo $file_size_kb; ?> KB, <?php echo $fileInfo['date']; ?>)</span>
                                </div>
                                <div>
                                    <a href="<?php echo $fileInfo['name']; ?>" class="back-button secondary" style="padding: 8px 15px; font-size: 0.9em;" download>
                                        <i class="fas fa-download"></i>
                                    </a>
                                </div>
                            </div>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <div class="no-files">
                            <i class="fas fa-inbox fa-2x" style="margin-bottom: 15px;"></i><br>
                            Анкеты еще не созданы
                        </div>
                    <?php endif; ?>
                </div>
            </div>
        </div>
        
        <script>
            // Функция обновления списка файлов
            function refreshFileList() {
                const refreshBtn = document.querySelector('.refresh-btn');
                const originalHtml = refreshBtn.innerHTML;
                
                // Показываем индикатор загрузки
                refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Обновление...';
                refreshBtn.disabled = true;
                
                // Используем AJAX для получения актуального списка файлов
                fetch('get_files.php')
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            updateFileListDisplay(data.files);
                        }
                    })
                    .catch(error => {
                        console.error('Ошибка при обновлении списка файлов:', error);
                        alert('Не удалось обновить список файлов');
                    })
                    .finally(() => {
                        // Восстанавливаем кнопку
                        setTimeout(() => {
                            refreshBtn.innerHTML = originalHtml;
                            refreshBtn.disabled = false;
                        }, 500);
                    });
            }
            
            // Функция обновления отображения списка файлов
            function updateFileListDisplay(files) {
                const filesContainer = document.getElementById('files-container');
                
                if (files.length > 0) {
                    let html = '';
                    files.forEach(file => {
                        const fileSizeKB = (file.size / 1024).toFixed(2);
                        html += `
                            <div class="file-item" data-file="${file.name}">
                                <div>
                                    <a href="${file.name}" class="file-link" target="_blank">
                                        <i class="fas fa-file-text"></i> ${file.name}
                                    </a>
                                    <span style="color: #7f8c8d; font-size: 0.9em;">(${fileSizeKB} KB, ${file.date})</span>
                                </div>
                                <div>
                                    <a href="${file.name}" class="back-button secondary" style="padding: 8px 15px; font-size: 0.9em;" download>
                                        <i class="fas fa-download"></i>
                                    </a>
                                </div>
                            </div>
                        `;
                    });
                    filesContainer.innerHTML = html;
                } else {
                    filesContainer.innerHTML = `
                        <div class="no-files">
                            <i class="fas fa-inbox fa-2x" style="margin-bottom: 15px;"></i><br>
                            Анкеты еще не созданы
                        </div>
                    `;
                }
            }
            
            // Автоматическое обновление списка файлов при возврате на страницу
            if (window.history.replaceState) {
                window.history.replaceState(null, null, window.location.href);
            }
            
            // Плавная прокрутка к началу страницы
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
            // Проверяем, есть ли новый файл и выделяем его
            document.addEventListener('DOMContentLoaded', function() {
                const currentFilename = "otvet<?php echo $file_number; ?>.txt";
                const currentFileElement = document.querySelector(`[data-file="${currentFilename}"]`);
                
                if (currentFileElement) {
                    // Прокручиваем к новому файлу
                    currentFileElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    
                    // Добавляем анимацию выделения
                    currentFileElement.style.backgroundColor = '#e8f4fc';
                    currentFileElement.style.transition = 'background-color 0.5s ease';
                    
                    setTimeout(() => {
                        currentFileElement.style.backgroundColor = '';
                    }, 3000);
                }
            });
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
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            
            .error-container {
                background-color: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 15px 35px rgba(0,0,0,0.1);
                text-align: center;
                width: 100%;
            }
            
            h2 {
                color: #e74c3c;
                margin-bottom: 20px;
                font-size: 1.8em;
            }
            
            p {
                color: #555;
                line-height: 1.6;
                margin-bottom: 25px;
                font-size: 1.1em;
            }
            
            .back-button {
                display: inline-block;
                background: linear-gradient(to right, #3498db, #2980b9);
                color: white;
                padding: 14px 28px;
                text-decoration: none;
                border-radius: 8px;
                margin: 10px;
                transition: all 0.3s ease;
                font-weight: 600;
                font-size: 16px;
                box-shadow: 0 4px 6px rgba(52, 152, 219, 0.2);
            }
            
            .back-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(52, 152, 219, 0.3);
                background: linear-gradient(to right, #2980b9, #3498db);
            }
            
            .icon {
                font-size: 4em;
                color: #e74c3c;
                margin-bottom: 20px;
            }
            
            .button-group {
                margin-top: 30px;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body>
        <div class="error-container">
            <div class="icon">
                <i class="fas fa-exclamation-triangle"></i>
            </div>
            <h2>Ошибка доступа</h2>
            <p>Данная страница предназначена для обработки данных формы.</p>
            <p>Пожалуйста, заполните форму анкеты для отправки данных.</p>
            
            <div class="button-group">
                <a href="index.html" class="back-button">
                    <i class="fas fa-home"></i> На главную страницу
                </a>
                <a href="forms.html" class="back-button">
                    <i class="fas fa-clipboard-list"></i> К форме анкеты
                </a>
            </div>
        </div>
    </body>
    </html>
    <?php
}
?>