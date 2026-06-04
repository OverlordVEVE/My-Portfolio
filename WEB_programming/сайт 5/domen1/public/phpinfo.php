<!DOCTYPE html>
<html>
<head>
    <title>Информация о PHP</title>
    <meta charset="utf-8">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        
        .header {
            max-width: 1200px;
            margin: 0 auto 20px auto;
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        h1 {
            color: #2c3e50;
            margin: 0;
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
        
        .warning {
            max-width: 1200px;
            margin: 20px auto;
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 15px;
            border-radius: 5px;
            color: #856404;
        }
        
        .phpinfo {
            max-width: 1200px;
            margin: 20px auto;
            background-color: white;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
        }
        
        .footer {
            max-width: 1200px;
            margin: 20px auto;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>⚙️ Информация о конфигурации PHP</h1>
        <a href="index.html" class="back-button">
            ← Назад на главную
        </a>
    </div>
    
    
    <div class="phpinfo">
        <?php
        // Выводим информацию о PHP
        phpinfo();
        ?>
    </div>
    
    <div class="footer">
        <p>Демонстрационный проект PHP. Информация сгенерирована <?php echo date('d.m.Y H:i:s'); ?></p>
    </div>
</body>
</html>