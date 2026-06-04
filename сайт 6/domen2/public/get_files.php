<?php
header('Content-Type: application/json; charset=utf-8');

// Функция для получения списка файлов с ответами
function getAnswerFiles() {
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

// Получаем список файлов
$files = getAnswerFiles();

// Выводим результат в формате JSON
echo json_encode([
    'success' => true,
    'files' => $files,
    'count' => count($files),
    'total_size' => array_sum(array_column($files, 'size'))
]);
?>