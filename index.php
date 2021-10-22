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

    $result = '宮城県の天気予報（明後日までの詳細）\n2021年10月01日11時\u3000仙台管区気象台\u3000発表\n\n\n日付 今日 01日(金) 明日 02日(土) 明後日 03日(日)\n東部 天気\n雨 晴れ\u3000明け方\u3000まで\u3000くもり\u3000所により\u3000未明\u3000雨 晴れ\u3000時々\u3000くもり\n風 北の風\u3000後\u3000やや強く\u3000海上\u3000では\u3000後\u3000北の風\u3000強く 北西の風\u3000やや強く\u3000後\u3000西の風\u3000やや強く\u3000海上\u3000では\u3000はじめ\u3000北の風\u3000強く 南東の風\u3000後\u3000南の風\n波 ３メートル\u3000後\u3000６メートル\u3000うねり\u3000を伴う ６メートル\u3000後\u3000４メートル\u3000うねり\u3000を伴う ３メートル\u3000後\u3000２メートル\u3000うねり\u3000を伴う\n降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24\n- - 80 70 30 0 0 0\n気温\n(℃) 朝の最低 日中の最高 朝の最低 日中の最高\n仙台 - 20 17 27\n石巻 - 19 15 26\n古川 - 19 15 25\n日付 今日 01日(金) 明日 02日(土) 明後日 03日(日)\n西部 天気\n雨 くもり\u3000昼前\u3000から\u3000晴れ 晴れ\u3000時々\u3000くもり\n風 北東の風\u3000後\u3000北の風 西の風 西の風\n降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24\n- - 80 60 10 10 0 0\n気温\n(℃) 朝の最低 日中の最高 朝の最低 日中の最高\n白石 - 18 15 26';
    //strstrを用いてR2以降のデータを切り出す
    //strstrを用いてR2以降のデータを切り出す
    $data = strstr($result, '\n仙台');
    
    $str = strstr($data, '\n石巻', $before_needle=True);
    $str = str_replace("\n", "", $str);
    //地名を抜き出す
    $place =strstr($str, " - ", $before_needle=True);
    //気温を抜き出す
    $temp = strstr($str, " - ");
    $temp_list = explode(" ", $temp);
    
    $str = array_filter($temp_list);
    echo $temp_list[0], " | ", $temp_list[1], " | ", $temp_list[2], " | ", $temp_list[3], " | ";
    $predicts = array_map('intval', $str)
?>