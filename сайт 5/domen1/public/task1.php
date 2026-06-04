<!DOCTYPE html>
<html>
<head>
    <title>Основные конструкции PHP</title>
    <meta charset="utf-8">
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            margin: 0; 
            padding: 20px; 
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }
        
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid #4CAF50;
        }
        
        .back-button {
            background: linear-gradient(to right, #3498db, #2c3e50);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .back-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4);
        }
        
        .section { 
            margin-bottom: 30px; 
            padding: 20px; 
            border: 1px solid #e0e0e0; 
            border-radius: 10px;
            background-color: #f9f9f9;
            transition: all 0.3s ease;
        }
        
        .section:hover {
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
        }
        
        h1 { 
            color: #2c3e50; 
            margin: 0;
            font-size: 2.5em;
        }
        
        h2 { 
            color: #333; 
            border-bottom: 2px solid #4CAF50; 
            padding-bottom: 10px; 
            margin-top: 0;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        pre { 
            background: #f5f5f5; 
            padding: 15px; 
            border-radius: 5px; 
            overflow-x: auto; 
            border-left: 4px solid #3498db;
        }
        
        .result { 
            color: #2196F3; 
            font-weight: bold; 
            background-color: #e3f2fd;
            padding: 2px 6px;
            border-radius: 3px;
        }
        
        .highlight {
            background-color: #fffde7;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #ffc107;
        }
        
        .navigation {
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }
        
        .nav-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 10px 20px;
            background-color: #f0f0f0;
            border-radius: 5px;
            text-decoration: none;
            color: #333;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            background-color: #e0e0e0;
            transform: translateY(-2px);
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #7f8c8d;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Демонстрация основных конструкций PHP</h1>
            <a href="index.html" class="back-button">
                ← Назад на главную
            </a>
        </div>

        <?php
        // 1. Создание переменных
        echo '<div class="section">';
        echo '<h2><span>1️⃣</span> Переменные и их значения</h2>';
        
        $integerVar = 42;
        $floatVar = 3.14159;
        $stringVar = "Привет, мир!";
        $boolVar = true;
        $nullVar = null;
        
        echo '<p>Целое число: <span class="result">' . $integerVar . '</span></p>';
        echo '<p>Дробное число: <span class="result">' . $floatVar . '</span></p>';
        echo '<p>Строка: <span class="result">' . $stringVar . '</span></p>';
        echo '<p>Булево значение: <span class="result">' . ($boolVar ? 'true' : 'false') . '</span></p>';
        echo '<p>Null значение: <span class="result">' . (is_null($nullVar) ? 'null' : 'не null') . '</span></p>';
        echo '</div>';

        // 2. Операторы сравнения
        echo '<div class="section">';
        echo '<h2><span>2️⃣</span> Операторы сравнения</h2>';
        
        $a = 10;
        $b = "10";
        $c = 15;
        
        echo '<div class="highlight">';
        echo '<p><strong>$a = ' . $a . ', $b = "' . $b . '", $c = ' . $c . '</strong></p>';
        echo '</div>';
        
        echo '<p>$a == $b: <span class="result">' . ($a == $b ? 'true' : 'false') . '</span> (равно по значению)</p>';
        echo '<p>$a === $b: <span class="result">' . ($a === $b ? 'true' : 'false') . '</span> (равно по значению и типу)</p>';
        echo '<p>$a != $c: <span class="result">' . ($a != $c ? 'true' : 'false') . '</span> (не равно)</p>';
        echo '<p>$a < $c: <span class="result">' . ($a < $c ? 'true' : 'false') . '</span> (меньше)</p>';
        echo '<p>$a > $c: <span class="result">' . ($a > $c ? 'true' : 'false') . '</span> (больше)</p>';
        echo '<p>$a <= $c: <span class="result">' . ($a <= $c ? 'true' : 'false') . '</span> (меньше или равно)</p>';
        echo '</div>';

        // 3. Создание массива с циклом for
        echo '<div class="section">';
        echo '<h2><span>3️⃣</span> Массив с циклом for</h2>';
        
        $randomArray = array();
        for ($i = 0; $i < 10; $i++) {
            $randomArray[] = rand(1, 100); // случайные числа от 1 до 100
        }
        
        echo '<p>Сгенерированный массив из 10 случайных чисел (1-100):</p>';
        echo '<pre>';
        print_r($randomArray);
        echo '</pre>';
        echo '</div>';

        // 4. Третий элемент массива
        echo '<div class="section">';
        echo '<h2><span>4️⃣</span> Третий элемент массива</h2>';
        
        if (isset($randomArray[2])) {
            echo '<p>Третий элемент массива (индекс 2): <span class="result">' . $randomArray[2] . '</span></p>';
        } else {
            echo '<p>Третий элемент не существует</p>';
        }
        echo '</div>';

        // 5. Переменная переменной
        echo '<div class="section">';
        echo '<h2><span>5️⃣</span> Переменная переменной</h2>';
        
        $variableName = "myVariable";
        $$variableName = "Значение переменной переменной";
        
        echo '<p>Имя переменной: $variableName = "<span class="result">' . $variableName . '</span>"</p>';
        echo '<p>Значение переменной переменной ($$variableName): <span class="result">' . $myVariable . '</span></p>';
        echo '</div>';

        // 6. Текущие дата и время
        echo '<div class="section">';
        echo '<h2><span>6️⃣</span> Текущие дата и время</h2>';
        
        $currentDateTime = date('d.m.Y H:i:s');
        echo '<p>Текущая дата и время: <span class="result">' . $currentDateTime . '</span></p>';
        echo '</div>';

        // 7. UNIX timestamp дня рождения
        echo '<div class="section">';
        echo '<h2><span>7️⃣</span> UNIX timestamp дня рождения</h2>';
        
        // Пример: 15 августа 1990 года
        $birthdayTimestamp = mktime(0, 0, 0, 8, 15, 1990);
        $birthdayFormatted = date('d.m.Y', $birthdayTimestamp);
        
        echo '<p>День рождения: <span class="result">' . $birthdayFormatted . '</span></p>';
        echo '<p>UNIX timestamp: <span class="result">' . $birthdayTimestamp . '</span></p>';
        echo '<p>Это соответствует: <span class="result">' . number_format($birthdayTimestamp) . '</span> секунд с 1 января 1970 года</p>';
        echo '</div>';

        // 8. Суперглобальный массив $_SERVER
        echo '<div class="section">';
        echo '<h2><span>8️⃣</span> Некоторые элементы $_SERVER</h2>';
        
        echo '<pre>';
        echo "<strong>Основная информация:</strong>\n";
        echo "SERVER_SOFTWARE: " . ($_SERVER['SERVER_SOFTWARE'] ?? 'не определено') . "\n";
        echo "SERVER_NAME: " . ($_SERVER['SERVER_NAME'] ?? 'не определено') . "\n";
        echo "REQUEST_METHOD: " . ($_SERVER['REQUEST_METHOD'] ?? 'не определено') . "\n";
        echo "\n<strong>Информация о клиенте:</strong>\n";
        echo "REMOTE_ADDR: " . ($_SERVER['REMOTE_ADDR'] ?? 'не определено') . "\n";
        echo "HTTP_USER_AGENT: " . ($_SERVER['HTTP_USER_AGENT'] ?? 'не определено') . "\n";
        echo "\n<strong>Информация о скрипте:</strong>\n";
        echo "SCRIPT_FILENAME: " . ($_SERVER['SCRIPT_FILENAME'] ?? 'не определено') . "\n";
        echo "PHP_SELF: " . ($_SERVER['PHP_SELF'] ?? 'не определено') . "\n";
        echo '</pre>';
        echo '</div>';

        // 9. Произвольная функция
        echo '<div class="section">';
        echo '<h2><span>9️⃣</span> Произвольная функция</h2>';
        
        function calculateCircleArea($radius) {
            if ($radius <= 0) {
                return "Радиус должен быть положительным числом";
            }
            return pi() * pow($radius, 2);
        }
        
        $radius = 5;
        $area = calculateCircleArea($radius);
        
        echo '<p>Функция <strong>calculateCircleArea($radius)</strong> вычисляет площадь круга по формуле: π × r²</p>';
        echo '<p>Для радиуса = ' . $radius . ' площадь круга: <span class="result">' . round($area, 2) . '</span></p>';
        
        // Дополнительный вызов
        $radius2 = 7.5;
        $area2 = calculateCircleArea($radius2);
        echo '<p>Для радиуса = ' . $radius2 . ' площадь круга: <span class="result">' . round($area2, 2) . '</span></p>';
        echo '</div>';
        ?>
        
        <div class="navigation">
            <a href="index.html" class="nav-link">
                ← Назад на главную
            </a>
            <a href="phpinfo.php" class="nav-link">
                Перейти к информации о PHP →
            </a>
        </div>
        
        <div class="footer">
            <p>Демонстрационный проект PHP. Все примеры выполнены в реальном времени.</p>
            <p>Серверное время: <?php echo date('d.m.Y H:i:s'); ?></p>
        </div>
    </div>
</body>
</html>