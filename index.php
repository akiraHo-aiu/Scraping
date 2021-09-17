<head>
<meta charset=”UTF-8″>
<title>仙台市の気温</title>
</head>
<body>
<h1>仙台市の9月1日の気温</h1>

</body>

<?php
    //command 必要なパッケージのあるPythonのパス
    $command = 'C:\Users\b1800\Anaconda3\envs\Scraping\python.exe D:\scraping\scrape.py'; 
    exec($command, $output);
    echo "平均気温", $output[0][6]."\n";
    echo "最高気温", $output[0][7]. "\n";
    echo "最低気温", $output[0][8]. "\n";
?>