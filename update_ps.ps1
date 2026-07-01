$ErrorActionPreference = "Stop"

$filePath = "c:\Users\ADMIN\Desktop\N5 T12-2021\index.html"
$html = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

$explanations = @{
    "listen-m1-1" = "【Script】<br>先生「では、これからカレーを作りましょう。」<br>学生「先生、私は野菜を切りましょうか。」<br>先生「いいえ、野菜じゃなくて、肉を切ってください。」<br>学生「はい。」<br><br>【Giải thích】Giáo viên bảo học sinh cắt thịt (肉) chứ không phải rau (野菜). Chọn đáp án 3."
    "listen-m1-2" = "【Script】<br>女「あ、この手袋は今店を出た女の人のですね。」<br>男「ああ、四人のグループですね。あそこにいますよ。」<br>女「すぐ持って行って、渡してください。あの髪が短くて、メガネをかけている人のです。」<br>男「分かりました。」<br><br>【Giải thích】Người phụ nữ có tóc ngắn (髪が短くて) và đeo kính (メガネをかけている). Chọn đáp án 4."
    "listen-m1-3" = "【Script】<br>男の子「お母さん、荷物来たよ、どこに置く？テーブルの上でいい？」<br>母「それ食べ物よ。テーブルの上じゃなくて、冷蔵庫に入れて。」<br>男の子「お母さん、冷蔵庫、いっぱいだよ。」<br>母「じゃ、冷蔵庫の横の椅子に置いて。」<br>男の子「はーい。」<br><br>【Giải thích】Tủ lạnh đầy nên mẹ bảo để lên ghế cạnh tủ lạnh (冷蔵庫の横の椅子に置いて). Chọn đáp án 1."
    "listen-m1-4" = "【Script】<br>女「もしもし、今駅に着きました。」<br>男「そうですか、僕は喫茶店にいます。」<br>女「ああ、駅の隣の喫茶店ですね。」<br>男「いいえ、大学の前の喫茶店です。」<br>女「ああ、分かりました、すぐ行きます。」<br><br>【Giải thích】Người nam đang ở quán nước trước trường đại học (大学の前の喫茶店). Chọn đáp án 4."
    "listen-m1-5" = "【Script】<br>先生「皆さん、今日授業の後、この新しい教科書を買って、次の授業の時に持って来てください。教科書の名前は日本語２です。教科書は明日まで、一階の１０１で売っています。この教室は２階の２０１ですから、丁度この下の教室ですね。」<br><br>【Giải thích】Sách bán ở phòng 101 tầng 1 (一階の１０１で売っています). Chọn đáp án 1."
    "listen-m1-6" = "【Script】<br>女「黄色の帽子と、青と、それから、黒があるよ。どれがいい？」<br>男「それじゃあ、黒と青の帽子は持っているから、黄色がいい。」<br>女「分かった。」<br><br>【Giải thích】Người nam đã có mũ đen và xanh, nên chọn mũ màu vàng (黄色がいい). Chọn đáp án 2."
    "listen-m1-7" = "【Script】<br>先生「バスの切符は５００円ですが、山に登って、またバスで帰りますから、千円持ってきてください。山の上は少し寒いですから、上着も忘れないでくださいね。皆一緒に歩きますから、山の地図は私が持って行きます。」<br><br>【Giải thích】Cần mang theo 1000 yên (千円 - tiền) và áo khoác (上着 - áo). Chọn đáp án 1."

    "listen-m2-1" = "【Script】<br>男「いいえ、月曜日から木曜日まで大学に行って、金曜日は近くの図書館で勉強します。」<br>女「土曜日や日曜日はどうしていますか。」<br>男「掃除をしたり、友達と会ったりしています。」<br><br>【Giải thích】Hỏi ngày thứ 6. Nam nói: 金曜日は近くの図書館で勉強します (Thứ 6 học ở thư viện gần đó). Chọn đáp án 2."
    "listen-m2-2" = "【Script】<br>男「じゃあ、一緒に晩ご飯を食べに行きませんか。」<br>女「あ、ごめんなさい。ちょっと頭が痛いですから、今日はもう家に帰ります。」<br>男「そう、じゃ、また。」<br><br>【Giải thích】Người nữ bị đau đầu (頭が痛い) nên sẽ đi về nhà (家に帰ります). Chọn đáp án 4."
    "listen-m2-3" = "【Script】<br>女「林さん、いつ国へ帰りますか。」<br>男「今日は三月四日ですから、ちょうど二週間後です。」<br>女「そうですか。再来週の金曜ですね。」<br>男「はい。」<br><br>【Giải thích】Hôm nay mùng 4. Về nước sau 2 tuần (二週間後). Tức là ngày 18. Chọn đáp án 4."
    "listen-m2-4" = "【Script】<br>女「林さんの家は山と海は近いから、毎日見ていますよ。この橋の絵のはがきはどうですか。綺麗ですよ。」<br>男「いいですね。それを出しましょう。」<br><br>【Giải thích】Cả hai chọn thiệp có hình cây cầu (橋の絵) để gửi vì nhà bạn kia đã gần núi và biển. Chọn đáp án 1."
    "listen-m2-5" = "【Script】<br>男「山本さん、今日は五月二十九日、山本さんの誕生日ですね。これ、プレゼントです。どうぞ。」<br>女「綺麗な花ですね。ありがとうございます。でも、誕生日はまだです。一日早いですよ。」<br><br>【Giải thích】Hôm nay 29/5. Sinh nhật còn sớm 1 ngày (一日早いですよ), vậy sinh nhật là ngày 30/5. Chọn đáp án 3."
    "listen-m2-6" = "【Script】<br>男「僕はスポーツが大好きです。授業の前に毎朝友達とバスケットボールの練習をしています。時々大学のプールで泳いだり、テニスをしたりしています。サッカーはあまりしませんが、毎日見ています。」<br><br>【Giải thích】Mỗi sáng trước giờ học tập bóng rổ (バスケットボールの練習をしています). Chọn đáp án 4."
}

foreach ($key in $explanations.Keys) {
    $exp = $explanations[$key]
    $exp = $exp.Replace('"', '&quot;')
    
    # Regex to match the explanation div for the specific question
    $pattern = '(?s)(<div class="question-card" data-qid="' + $key + '">.*?<div class="explanation".*?data-explain=")(.*?)("></div>)'
    $replacement = "`${1}$exp`${3}"
    
    $html = [System.Text.RegularExpressions.Regex]::Replace($html, $pattern, $replacement)
}

[System.IO.File]::WriteAllText($filePath, $html, [System.Text.Encoding]::UTF8)
Write-Host "Update completed successfully."
