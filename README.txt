マニュアル

１．　動かすのに必要なライブラリ
    ・prefecture に格納されているPythonファイルについて
        47都道府県のそれぞれのファイルに同じライブラリが使用されています。
            from selenium import webdriver 
            import chromedriver_binary
            import os 
            import csv 
            from selenium import webdriver 
            from selenium.webdriver.common.keys import Keys as keys
        とありますが
            improt os 
            import csv 
        は不必要なものとなります。
        従って、selenium　と　chromedriver_binary　をインストールしてあれば動くはずです。


ファイルについて
    まずindex.phpにて47都道府県の選択をさせそれに基づき選択された都道府県のデータを表示させる(second.php)というようにしようと考えていました。