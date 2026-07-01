$ErrorActionPreference = "Stop"

$filePath = "c:\Users\ADMIN\Desktop\N5 T12-2021\index.html"
$html = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

$explanations = @{
    "listen-m1-1" = "【Script】<br>１、男の学生はこの後すぐ何をしますか<br>先生「では、これからカレーを作りましょう。」<br>学生「先生、私は野菜を切りましょうか。」<br>先生「いいえ、野菜じゃなくて、肉を切ってください。」<br>学生「はい。」<br><br>【Giải thích】Câu hỏi: Nam sinh sau đây sẽ làm gì ngay?<br>Giáo viên bảo học sinh cắt thịt (肉) chứ không phải rau (野菜). Chọn đáp án 3."
    
    "listen-m1-2" = "【Script】<br>２、店の男の人は誰に手袋を渡しますか<br>女「あ、この手袋は今店を出た女の人のですね。」<br>男「ああ、四人のグループですね。あそこにいますよ。」<br>女「すぐ持って行って、渡してください。あの髪が短くて、メガネをかけている人のです。」<br>男「分かりました。」<br><br>【Giải thích】Câu hỏi: Nam nhân viên cửa hàng đưa găng tay cho ai?<br>Người phụ nữ có tóc ngắn (髪が短くて) và đeo kính (メガネをかけている). Chọn đáp án 4."
    
    "listen-m1-3" = "【Script】<br>３、男の子は荷物をどこに置きますか<br>男の子「お母さん、荷物来たよ、どこに置く？テーブルの上でいい？」<br>母「それ食べ物よ。テーブルの上じゃなくて、冷蔵庫に入れて。」<br>男の子「お母さん、冷蔵庫、いっぱいだよ。」<br>母「じゃ、冷蔵庫の横の椅子に置いて。」<br>男の子「はーい。」<br><br>【Giải thích】Câu hỏi: Bé trai sẽ đặt hành lý ở đâu?<br>Tủ lạnh đầy nên mẹ bảo để lên ghế cạnh tủ lạnh (冷蔵庫の横の椅子に置いて). Chọn đáp án 1."
    
    "listen-m1-4" = "【Script】<br>４、女の人はこの後どこへ行きますか<br>女「もしもし、今駅に着きました。」<br>男「そうですか、僕は喫茶店にいます。」<br>女「ああ、駅の隣の喫茶店ですね。」<br>男「いいえ、大学の前の喫茶店です。」<br>女「ああ、分かりました、すぐ行きます。」<br><br>【Giải thích】Câu hỏi: Người phụ nữ sau đây đi đâu?<br>Người nam đang ở quán nước trước trường đại học (大学の前の喫茶店). Chọn đáp án 4."
    
    "listen-m1-5" = "【Script】<br>５、学生はどこで新しい教科書を買いますか<br>先生「皆さん、今日授業の後、この新しい教科書を買って、次の授業の時に持って来てください。教科書の名前は日本語２です。教科書は明日まで、一階の１０１で売っています。この教室は２階の２０１ですから、丁度この下の教室ですね。」<br><br>【Giải thích】Câu hỏi: Học sinh mua sách giáo khoa mới ở đâu?<br>Sách bán ở phòng 101 tầng 1 (一階の１０１で売っています). Chọn đáp án 1."
    
    "listen-m1-6" = "【Script】<br>６、女の学生は男の学生に何色の帽子をあげますか<br>男「あんさんのその赤い帽子、いいね。」<br>女「これは私が作った帽子だよ。」<br>男「上手だね。」<br>女「他の色で同じものを三つ作ったから、どれかあげる。」<br>男「え？本当？ありがとう。」<br>女「黄色の帽子と、青と、それから、黒があるよ。どれがいい？」<br>男「それじゃあ、黒と青の帽子は持っているから、黄色がいい。」<br>女「分かった。」<br><br>【Giải thích】Câu hỏi: Nữ sinh sẽ cho nam sinh chiếc mũ màu gì?<br>Người nam đã có mũ đen và xanh, nên chọn mũ màu vàng (黄色がいい). Chọn đáp án 2."
    
    "listen-m1-7" = "【Script】<br>７、学生は山に何を持って行きますか。<br>先生「明日は東山に行きます。學校の前のバス停から山までバスで行きます。バスの切符は５００円ですが、山に登って、またバスで帰りますから、千円持ってきてください。山の上は少し寒いですから、上着も忘れないでくださいね。皆一緒に歩きますから、山の地図は私が持って行きます。」<br><br>【Giải thích】Câu hỏi: Học sinh mang theo những gì lên núi?<br>Cần mang theo 1000 yên (千円 - tiền) và áo khoác (上着 - áo). Chọn đáp án 1."

    "listen-m2-1" = "【Script】<br>１、男の留学生は金曜日何をしていますか<br>女「日本はどうですか。」<br>男「はい、とても楽しいです。」<br>女「毎日大学に行きますか。」<br>男「いいえ、月曜日から木曜日まで大学に行って、金曜日は近くの図書館で勉強します。」<br>女「土曜日や日曜日はどうしていますか。」<br>男「掃除をしたり、友達と会ったりしています。」<br>女「そうですか。」<br><br>【Giải thích】Câu hỏi: Du học sinh nam làm gì vào ngày thứ 6?<br>Nam nói: 金曜日は近くの図書館で勉強します (Thứ 6 học ở thư viện gần đó). Chọn đáp án 2."
    
    "listen-m2-2" = "【Script】<br>２、女の人は今から何をしますか。<br>男「仕事は終わりましたか。」<br>女「はい。」<br>男「じゃあ、一緒に晩ご飯を食べに行きませんか。」<br>女「あ、ごめんなさい。ちょっと頭が痛いですから、今日はもう家に帰ります。」<br>男「そう、じゃ、また。」<br><br>【Giải thích】Câu hỏi: Người phụ nữ bây giờ sẽ làm gì?<br>Người nữ bị đau đầu (頭が痛い) nên sẽ đi về nhà (家に帰ります). Chọn đáp án 4."
    
    "listen-m2-3" = "【Script】<br>３、男の留学生はいつ国へ帰りますか。<br>女「林さん、いつ国へ帰りますか。」<br>男「今日は三月四日ですから、ちょうど二週間後です。」<br>女「そうですか。再来週の金曜ですね。」<br>男「はい。」<br><br>【Giải thích】Câu hỏi: Du học sinh nam bao giờ về nước?<br>Hôm nay mùng 4. Về nước sau đúng 2 tuần (ちょうど二週間後です). Tức là ngày 18. Chọn đáp án 4."
    
    "listen-m2-4" = "【Script】<br>４、男の留学生が毎日しているスポーツは何ですか。<br>男「僕はスポーツが大好きです。授業の前に毎朝友達とバスケットボールの練習をしています。時々大学のプールで泳いだり、テニスをしたりしています。サッカーはあまりしませんが、毎日見ています。」<br><br>【Giải thích】Câu hỏi: Môn thể thao du học sinh nam chơi mỗi ngày là gì?<br>Mỗi sáng trước giờ học tập bóng rổ (バスケットボールの練習をしています). Chọn đáp án 1."
    
    "listen-m2-5" = "【Script】<br>５、女の学生の誕生日は何月何日ですか。<br>男「山本さん、今日は五月二十九日、山本さんの誕生日ですね。これ、プレゼントです。どうぞ。」<br>女「綺麗な花ですね。ありがとうございます。でも、誕生日はまだです。一日早いですよ。」<br>男「え？すみません。」<br><br>【Giải thích】Câu hỏi: Sinh nhật của nữ sinh là ngày tháng nào?<br>Hôm nay 29/5. Sinh nhật còn sớm 1 ngày (一日早いですよ), vậy sinh nhật là ngày 30/5. Chọn đáp án 3."
    
    "listen-m2-6" = "【Script】<br>６、二人はどのはがきを選びましたか。<br>女「綺麗な葉書がたくさんありますね。一つ選んで、一緒に林さんに出しましょうか。」<br>男「いいですね。花の絵、海の絵、色々ありますね。この山のはがきはどうですか。」<br>女「林さんの家は山と海は近いから、毎日見ていますよ。この橋の絵のはがきはどうですか。綺麗ですよ。」<br>男「いいですね。それを出しましょう。」<br><br>【Giải thích】Câu hỏi: 2 người đã chọn tấm bưu thiếp nào?<br>Cả hai chọn thiệp có hình cây cầu (橋の絵) để gửi vì nhà bạn kia đã gần núi và biển. Chọn đáp án 4."
    
    "listen-m3-1" = "【Script】<br>１、時計を忘れました、今の時間が知りたいです、友達に何と言いますか<br>①今何時？<br>②今時間がある？<br>③今１０時だよ<br><br>【Giải thích】Tình huống: Quên đồng hồ, muốn biết giờ hiện tại thì nói gì với bạn bè.<br>Hỏi: 今何時？ (Bây giờ là mấy giờ?). Chọn đáp án 1."
    
    "listen-m3-2" = "【Script】<br>２、先生の部屋に入ります、何と言いますか<br>①また明日<br>②失礼します<br>③どうぞ<br><br>【Giải thích】Tình huống: Vào phòng của giáo viên, nói gì?<br>Nói: 失礼します (Thất lễ, xin phép). Chọn đáp án 2."
    
    "listen-m3-3" = "【Script】<br>３、友達が結婚します、何と言いますか<br>①いらっしゃい<br>②おめでとう<br>③ありがとう<br><br>【Giải thích】Tình huống: Bạn bè kết hôn, nói gì?<br>Chúc mừng: おめでとう (Chúc mừng). Chọn đáp án 2."
    
    "listen-m3-4" = "【Script】<br>４、バスで京都に行きます、切符を買います、何と言いますか<br>①京都にバスで行ってください<br>②京都で切符を買ってください<br>③京都まで一枚ください<br><br>【Giải thích】Tình huống: Đi xe buýt tới Kyoto, mua vé thì nói gì?<br>Yêu cầu: 京都まで一枚ください (Cho 1 vé tới Kyoto). Chọn đáp án 3."
    
    "listen-m3-5" = "【Script】<br>５、スプーンで食べたいです、店の人に何と言いますか<br>①スプーンはいかがですか<br>②スプーンはありませんか<br>③スプーンで食べましょうか<br><br>【Giải thích】Tình huống: Muốn ăn bằng thìa, nói gì với nhân viên quán?<br>Hỏi xin: スプーンはありませんか (Có thìa không ạ?). Chọn đáp án 2."
    
    "listen-m4-1" = "【Script】<br>１．行ってきまーす<br>①お帰りなさい<br>②ただいま<br>③いってらっしゃい<br><br>【Giải thích】Câu 1: Khi có người ra khỏi nhà nói 行ってきまーす (Tôi đi đây), người ở nhà đáp lại: いってらっしゃい (Đi cẩn thận nhé). Chọn đáp án 3."
    
    "listen-m4-2" = "【Script】<br>２、それはどこのカメラですか<br>①一階にあります<br>②日本のです<br>③そこで撮ります<br><br>【Giải thích】Câu 2: Hỏi máy ảnh của hãng nước nào (どこの), trả lời: 日本のです (Của Nhật Bản). Chọn đáp án 2."
    
    "listen-m4-3" = "【Script】<br>３、どんな鞄を忘れましたか<br>①電車の中です<br>②黒い鞄です<br>③私のです<br><br>【Giải thích】Câu 3: Hỏi quên chiếc cặp như thế nào (どんな), trả lời: 黒い鞄です (Chiếc cặp màu đen). Chọn đáp án 2."
    
    "listen-m4-4" = "【Script】<br>４、日曜日に行ったレストラン、美味しかったね<br>①何を食べる？<br>②日曜日、大丈夫だよ<br>③また行きたいね<br><br>【Giải thích】Câu 4: Khen nhà hàng chủ nhật đã đi ngon quá nhỉ, đồng tình bằng cách nói: また行きたいね (Lại muốn đi nữa nhỉ). Chọn đáp án 3."
    
    "listen-m4-5" = "【Script】<br>５、学生の時、何かスポーツをしていましたか<br>①何もしていませんでした<br>②サッカーをしましょう<br>③あの学生がしていました<br><br>【Giải thích】Câu 5: Hỏi hồi học sinh có chơi môn thể thao nào không, trả lời: 何もしていませんでした (Đã không chơi môn nào). Chọn đáp án 1."
    
    "listen-m4-6" = "【Script】<br>６、すみません、この駅から山川駅まで、電車でどのくらいかかりますか<br>①１０時１５分です<br>②あの電車です<br>③１０分か１５分です<br><br>【Giải thích】Câu 6: Hỏi đi tàu mất bao lâu (どのくらい), trả lời: １０分か１５分です (10 hoặc 15 phút). Chọn đáp án 3."
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
