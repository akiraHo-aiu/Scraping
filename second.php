
<?php
$command = "python D:\XAMPP\htdocs\scraping\scrapepython_sample.py";
$output = shell_exec($command);
echo $output, "\n";
//$result = '宮城県の天気予報（明後日までの詳細）\n2021年10月01日11時\u3000仙台管区気象台\u3000発表\n\n\n日付 今日 01日(金) 明日 02日(土) 明後日 03日(日)\n東部 天気\n雨 晴れ\u3000明け方\u3000まで\u3000くもり\u3000所により\u3000未明\u3000雨 晴れ\u3000時々\u3000くもり\n風 北の風\u3000後\u3000やや強く\u3000海上\u3000では\u3000後\u3000北の風\u3000強く 北西の風\u3000やや強く\u3000後\u3000西の風\u3000やや強く\u3000海上\u3000では\u3000はじめ\u3000北の風\u3000強く 南東の風\u3000後\u3000南の風\n波 ３メートル\u3000後\u3000６メートル\u3000うねり\u3000を伴う ６メートル\u3000後\u3000４メートル\u3000うねり\u3000を伴う ３メートル\u3000後\u3000２メートル\u3000うねり\u3000を伴う\n降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24\n- - 80 70 30 0 0 0\n気温\n(℃) 朝の最低 日中の最高 朝の最低 日中の最高\n仙台 - 20 17 27\n石巻 - 19 15 26\n古川 - 19 15 25\n日付 今日 01日(金) 明日 02日(土) 明後日 03日(日)\n西部 天気\n雨 くもり\u3000昼前\u3000から\u3000晴れ 晴れ\u3000時々\u3000くもり\n風 北東の風\u3000後\u3000北の風 西の風 西の風\n降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24\n- - 80 60 10 10 0 0\n気温\n(℃) 朝の最低 日中の最高 朝の最低 日中の最高\n白石 - 18 15 26';

// 実際はこの result にスクレイピングで取り出した文字列を格納し処理を進めたいがどうしてもうまくいかなかったので得られると予想されるデータをコピー、ペーストしてここでは処理を進めている。
$result = '宮城県の天気予報（明後日までの詳細）
2021年11月16日17時 仙台管区気象台 発表 
日付 今夜 16日(火)
東部 天気
晴れ
風 北西の風　後　北の風
波 １メートル
降水確率(％) 00-06
-
気温
(℃) 朝の最低
仙台 -
石巻 -
古川 -
日付 今夜 16日(火)
西部 天気
晴れ
風 西の風
降水確率(％) 00-06
-
気温
(℃) 朝の最低
白石 -
日付 今夜 16日(火) 明日 17日(水) 明後日 18日(木)
天気
晴れ 晴れ くもり　時々　晴れ
風 北西の風　後　北の風 北西の風　後　西の風 南西の風　後　南の風
波 １メートル １メートル １メートル
降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24
- - - 0 0 0 0 0

朝の最低 日中の最高 朝の最低 日中の最高
仙台 - - 5 15
石巻 - - 3 14
古川 - - 1 14
日付 今夜 16日(火) 明日 17日(水) 明後日 18日(木)
天気
晴れ 晴れ くもり　時々　晴れ
風 西の風 西の風 南西の風
降水確率(％) 00-06 06-12 12-18 18-24 00-06 06-12 12-18 18-24
- - - 0 10 10 0 0

朝の最低 日中の最高 朝の最低 日中の最高
白石 - - 2 15
';

echo "宮城県の東部", "<br/>\n";

//パースの処理
//strstrを用いてR2以降のデータを切り出す
$data = strstr($result, '仙台 - -');
$str = strstr($data, '石巻 - -', $before_needle=True);
$temp_list = explode(" ", $str);
$place = $temp_list[0];
$today_high = $temp_list[1];
$today_low = $temp_list[2];
$tomo_low = $temp_list[3];
$tomo_high = $temp_list[4];

echo "明日の", $place, "；　最高気温：", $tomo_high, "℃　最低気温：", $tomo_low, "℃", "<br/>\n";

$data = strstr($result, '石巻 - -');
$str = strstr($data, '古川 - -', $before_needle=True);
$temp_list = explode(" ", $str);
$place = $temp_list[0];
$today_high = $temp_list[1];
$today_low = $temp_list[2];
$tomo_low = $temp_list[3];
$tomo_high = $temp_list[4];

echo "明日の", $place, "；　最高気温：", $tomo_high, "℃　最低気温：", $tomo_low, "℃", "<br/>\n";

$data = strstr($result, '古川 - -');
$str = strstr($data, '日付 今夜', $before_needle=True);
$temp_list = explode(" ", $str);
$place = $temp_list[0];
$today_high = $temp_list[1];
$today_low = $temp_list[2];
$tomo_low = $temp_list[3];
$tomo_high = $temp_list[4];

echo "明日の", $place, "；　最高気温：", $tomo_high, "℃　最低気温：", $tomo_low, "℃", "<br/>\n";

?>