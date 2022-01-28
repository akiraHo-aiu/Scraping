<head>
<meta charset=”UTF-8″>
<title>仙台市の気温</title>
</head>
<body>
<h1>仙台市の9月1日の気温</h1>
<form action="second.php" method="post" id="form_sample">

    <select name="都道府県">    
        <option name="">選択してください</option>    
        <option value="">北海道</option> <!-- 1 -->
        <option value="">青森</option> 
        <option value="">岩手</option>
        <option value="">宮城</option>
        <option value="">秋田</option> <!-- 5 -->
        <option value="">山形</option>
        <option value="">福島</option>
        <option value="">茨城</option>
        <option value="">栃木</option>
        <option value="">群馬</option> <!-- 10 -->
        <option value="">埼玉</option>
        <option value="">千葉</option>
        <option value="">東京</option>
        <option value="">神奈川</option>
        <option value="">新潟</option> <!-- 15 -->
        <option value="">富山</option>
        <option value="">石川</option>
        <option value="">福井</option>
        <option value="">山梨</option>
        <option value="">長野</option> <!-- 20 -->
        <option value="">岐阜</option>
        <option value="">静岡</option>
        <option value="">愛知</option>
        <option value="">三重</option>
        <option value="">滋賀</option> <!-- 25 -->
        <option value="">京都</option>
        <option value="">大阪</option>
        <option value="">兵庫</option>
        <option value="">奈良</option>
        <option value="">和歌山</option> <!-- 30 -->
        <option value="">鳥取</option>
        <option value="">島根</option>
        <option value="">岡山</option>
        <option value="">広島</option>
        <option value="">山口</option> <!-- 35 -->
        <option value="">徳島</option>
        <option value="">香川</option>
        <option value="">愛媛</option>
        <option value="">高知</option>
        <option value="">福岡</option>　<!-- 40 -->
        <option value="">佐賀</option>
        <option value="">長崎</option>
        <option value="">熊本</option>
        <option value="">大分</option>
        <option value="">宮崎</option> <!-- 45 -->
        <option value="">鹿児島</option>
        <option value="">沖縄</option>
    </select> 
    <input type="submit">
</form>    



</body>

<?php
    $command = "python3.6.8 D:\XAMPP\htdocs\scraping\scrapepython_sample.py";
    exec($command,$output);
    //echo $output[0], "\n";
    $result = '宮城県の天気予報（明後日までの詳細）\n2021年10月01日11時\u3000仙台管区気象台\u3000発表\n\n\n日付 今日 01日(金) 明日 02日(土) 明後日 03日(日)\n東部 天気\n雨 晴れ\u3000明け方\u3000まで\u3000くもり\u3000所により\u3000未明\u3000雨 晴れ\u3000時々\u3000くもり\n風 北の風\u3000後\u3000やや強く\u3000海上\u3000では\u3000後\u3000北の風\u3000強く 北西の風\u3000やや強く\u3000後\u3000西の風\u3000やや強く\u3000海上\u3000では\u3000はじめ\u3000北の風\u3000強く 南東の風\u3000後\u3000南の風\n波 ３メートル\u3000後\u3000６メートル\u3000うねり\u3000を伴う ６メートル\u3000後\u3000４メートル\u3000うねり\u3000を伴う ３メートル\u3000後\u3000２メートル\u3000うねり\u3000を伴う\n降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24\n- - 80 70 30 0 0 0\n気温\n(℃) 朝の最低 日中の最高 朝の最低 日中の最高\n仙台 - 20 17 27\n石巻 - 19 15 26\n古川 - 19 15 25\n日付 今日 01日(金) 明日 02日(土) 明後日 03日(日)\n西部 天気\n雨 くもり\u3000昼前\u3000から\u3000晴れ 晴れ\u3000時々\u3000くもり\n風 北東の風\u3000後\u3000北の風 西の風 西の風\n降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24\n- - 80 60 10 10 0 0\n気温\n(℃) 朝の最低 日中の最高 朝の最低 日中の最高\n白石 - 18 15 26';
    //strstrを用いてR2以降のデータを切り出す
    //strstrを用いてR2以降のデータを切り出す
    /**  
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
    */
?>
