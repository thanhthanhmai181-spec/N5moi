import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ==========================================
# 1. UPDATE READING PASSAGES (Mondai 4, 5, 6)
# ==========================================

mondai4_old = """      <!-- もんだい4: 読解 短文 -->
      <div class="mondai-block">
        <div class="mondai-title">もんだい４</div>
        <p class="mondai-desc">つぎの ぶんしょうを よんで、しつもんに こたえてください。</p>

        <div class="reading-passage">
          リーさんへ<br><br>
          きょうは　ともだちと　びじゅつかんへ　いきました。とても　きれいな　えが　たくさん　ありました。びじゅつかんの　まえに　おおきい　こうえんが　あります。こうえんで　すこし　やすみました。<br><br>
          たなかさんより
        </div>

        <div class="question-card" data-qid="gram-m4-18">
          <div class="question-text"><span class="question-number">18</span>たなかさんは　きょう　どこへ　いきましたか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m4-18" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">こうえんへ いきました</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-18" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">びじゅつかんへ いきました</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-18" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">えいがかんへ いきました</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-18" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">がっこうへ いきました</span></label>
          </div>
          <div class="explanation" data-explain="Bài đọc nói: びじゅつかんへ いきました = đi bảo tàng mỹ thuật."></div>
        </div>

        <div class="question-card" data-qid="gram-m4-19">
          <div class="question-text"><span class="question-number">19</span>びじゅつかんの　まえに　なにが　ありますか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m4-19" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">おおきい えき</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-19" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">おおきい こうえん</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-19" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">ちいさい こうえん</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-19" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">ちいさい えき</span></label>
          </div>
          <div class="explanation" data-explain="Bài đọc nói: びじゅつかんの まえに おおきい こうえんが あります."></div>
        </div>
      </div>"""

mondai4_new = """      <!-- もんだい4: 読解 短文 -->
      <div class="mondai-block">
        <div class="mondai-title">もんだい４</div>
        <p class="mondai-desc">つぎの ぶんしょうを よんで、しつもんに こたえてください。こたえは、1・2・3・4 から いちばん いい ものを ひとつ えらんで ください。</p>

        <div class="reading-passage">
          (1)<br>
          10年前は、えきの ちかくに 小さい みせが たくさん あって、みんなは 小さい店で かいものを しました。今は えきの ちかくに みせが あまり ありませんから、えきから とおくて 大きい みせで かいものを します。
        </div>

        <div class="question-card" data-qid="gram-m4-18">
          <div class="question-text"><span class="question-number">18</span>10年前、みんなは どこで かいものを しましたか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m4-18" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">えきの ちかくの 大きい みせ</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-18" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">えきの ちかくの 小さい みせ</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-18" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">えきから とおくて 大きい みせ</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-18" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">えきから とおくて 小さい みせ</span></label>
          </div>
          <div class="explanation" data-explain="Đoạn văn viết: 10年前は... みんなは 小さい店で かいものを しました (10 năm trước, mọi người mua sắm ở cửa hàng nhỏ gần ga). Đáp án: 2"></div>
        </div>

        <div class="reading-passage">
          (2)<br>
          これは ユンさんが クラスメートの ダニエラさんに 書いた メールです。<br><br>
          ダニエラさん<br>
          きのうの よるから あたまが とても いたいです。いまから びょういんに いきますから、ごぜんの クラスは やすみます。ごごから がっこうに いきます。<br>
          すみませんが、かわぐちせんせいに いって ください。<br>
          ユン
        </div>

        <div class="question-card" data-qid="gram-m4-19">
          <div class="question-text"><span class="question-number">19</span>ダニエラさんは かわぐちせんせいに 何と いいますか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m4-19" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">「ユンさんは びょういんに いきますから、きょう がっこうを やすみます。」</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-19" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">「ユンさんは びょういんに いって、ごごから がっこうに きます。」</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-19" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">「ユンさんは ごご びょういんに いって、それから がっこうに きます。」</span></label>
            <label class="option-label"><input type="radio" name="gram-m4-19" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">「ユンさんは びょういんに いってから、ごぜんの クラスに きます。」</span></label>
          </div>
          <div class="explanation" data-explain="Yun nhắn: Đi viện nên nghỉ lớp buổi sáng, chiều sẽ đến trường. Vậy Daniela sẽ nói: Yun đi viện rồi chiều sẽ đến. Đáp án: 2"></div>
        </div>
      </div>"""

html = html.replace(mondai4_old, mondai4_new)


mondai5_old = """      <!-- もんだい5: 読解 中文 -->
      <div class="mondai-block">
        <div class="mondai-title">もんだい５</div>

        <div class="reading-passage">
          わたしは　せんしゅうの　にちようびに　ともだちの　やまださんと　うみへ　いきました。てんきは　とても　よかったです。うみで　およぎました。それから　すなはまで　おべんとうを　たべました。おべんとうは　やまださんが　つくりました。とても　おいしかったです。ごご　3じごろ　うちへ　かえりました。とても　たのしい　いちにちでした。
        </div>

        <div class="question-card" data-qid="gram-m5-20">
          <div class="question-text"><span class="question-number">20</span>にちようびの　てんきは　どうでしたか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m5-20" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">あめでした</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-20" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">くもりでした</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-20" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">さむかったです</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-20" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">よかったです</span></label>
          </div>
          <div class="explanation" data-explain="Bài đọc nói: てんきは とても よかったです = thời tiết rất tốt."></div>
        </div>

        <div class="question-card" data-qid="gram-m5-21">
          <div class="question-text"><span class="question-number">21</span>おべんとうは　だれが　つくりましたか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m5-21" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">わたしが つくりました</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-21" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">おかあさんが つくりました</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-21" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">やまださんが つくりました</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-21" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">だれも つくりませんでした</span></label>
          </div>
          <div class="explanation" data-explain="Bài đọc nói: おべんとうは やまださんが つくりました."></div>
        </div>
      </div>"""

mondai5_new = """      <!-- もんだい5: 読解 中文 -->
      <div class="mondai-block">
        <div class="mondai-title">もんだい５</div>
        <p class="mondai-desc">つぎの ぶんしょうを よんで、しつもんに こたえて ください。こたえは、1・2・3・4 から いちばん いい ものを ひとつ えらんで ください。</p>
        <div class="reading-passage">
          せんしゅう きょうとへ 一人で りょこうに 行きました。<br>
          ホテルは きょうとえきの まえに ある 大きな ホテルでした。私は へやに にもつを おいて、小さな かばんに さいふや パスポートを いれて、ゆうめいな にわを 見に 行きました。ホテルから にわまで タクシーに のりました。いけには さかなが およいで いて、さくらが きれいでした。<br>
          それから、きょうとの まちを あるいて ざっしで みた おかしを かいに いきました。みせで かばんから さいふを だしましたが、かばんには パスポートが ありませんでした。<br>
          わたしは すぐに ホテルに かえりました。<br>
          パスポートは ホテルに ありました。とても うれしかったです。ホテルの 人が「タクシーがいしゃの ひとが もって きましたよ。」と いいました。<br>
          きょうとは いいまち でした。
        </div>

        <div class="question-card" data-qid="gram-m5-20">
          <div class="question-text"><span class="question-number">20</span>「わたし」は ホテルを でた あとで、はじめに なにを しましたか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m5-20" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">あるいて きょうとえきに いきました。</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-20" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">タクシーで きょうとえきに いきました。</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-20" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">あるいて ゆうめいな にわを みに いきました</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-20" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">タクシーで ゆうめいな にわを みに いきました</span></label>
          </div>
          <div class="explanation" data-explain="Đoạn văn viết: ホテルから にわまで タクシーに のりました (Từ khách sạn lên taxi đến khu vườn). Đáp án: 4"></div>
        </div>

        <div class="question-card" data-qid="gram-m5-21">
          <div class="question-text"><span class="question-number">21</span>どうして とても うれしかったですか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m5-21" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">はじめて 一人で タクシーに のったから</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-21" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">ホテルの ひとの にほんごが わかったから</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-21" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">パスポートが ホテルに あったから</span></label>
            <label class="option-label"><input type="radio" name="gram-m5-21" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">とても きれいで いい ホテルだったから</span></label>
          </div>
          <div class="explanation" data-explain="Tác giả vui vì: パスポートは ホテルに ありました。とても うれしかったです (Hộ chiếu có ở khách sạn. Rất vui). Đáp án: 3"></div>
        </div>
      </div>"""

html = html.replace(mondai5_old, mondai5_new)


mondai6_old = """      <!-- もんだい6: 情報検索 -->
      <div class="mondai-block">
        <div class="mondai-title">もんだい６</div>

        <div class="reading-passage">
          <div style="text-align:center;font-weight:bold;font-size:1.1rem;margin-bottom:0.8rem">としょかんの　おしらせ</div>
          ・あいている　じかん：ごぜん　9じ ～ ごご　6じ<br>
          ・やすみ：すいようび、にちようび<br>
          ・ほんは　２しゅうかん　かりられます<br>
          ・いちどに　5さつまで　かりられます
        </div>

        <div class="question-card" data-qid="gram-m6-22">
          <div class="question-text"><span class="question-number">22</span>としょかんについて　ただしいのは　どれですか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m6-22" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">すいようびは やすみです</span></label>
            <label class="option-label"><input type="radio" name="gram-m6-22" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">いちどに 10さつ かりられます</span></label>
            <label class="option-label"><input type="radio" name="gram-m6-22" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">ほんは 1しゅうかん かりられます</span></label>
            <label class="option-label"><input type="radio" name="gram-m6-22" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">にちようびも あいています</span></label>
          </div>
          <div class="explanation" data-explain="Thông báo nói: やすみ：すいようび、にちようび → Thứ 4 là ngày nghỉ. Đáp án đúng."></div>
        </div>
      </div>"""

mondai6_new = """      <!-- もんだい6: 情報検索 -->
      <div class="mondai-block">
        <div class="mondai-title">もんだい６</div>
        <p class="mondai-desc">みぎの ページを 見て、下の しつもんに こたえて ください。こたえは、1・2・3・4 から いちばん いい ものを 一つ えらんで ください。</p>
        <div class="reading-passage">
          <div style="text-align:center;font-weight:bold;font-size:1.1rem;margin-bottom:0.8rem">ケーキ屋「マロン」</div>
          <div style="text-align:center;">たかやま町 235-8 電話: 013-579-2468<br>休み: 日よう日</div>
          <div style="text-align:center; margin-bottom:1rem;">こんしゅう(9月7日〜9月12日)の やすい もの</div>
          
          <table style="width:100%; border-collapse: collapse; text-align:center;" border="1">
            <tr style="background:var(--surface-color);">
              <td style="padding:8px;">7日(月)</td>
              <td style="padding:8px;">8日(火)</td>
              <td style="padding:8px;">9日(水)</td>
            </tr>
            <tr>
              <td style="padding:8px;">いちごのケーキ</td>
              <td style="padding:8px;">チョコレートのケーキ</td>
              <td style="padding:8px;">バナナのケーキ</td>
            </tr>
            <tr style="font-weight:bold;">
              <td style="padding:8px;">450円 → 350円</td>
              <td style="padding:8px;">400円 → 300円</td>
              <td style="padding:8px;">350円 → 250円</td>
            </tr>
            <tr style="background:var(--surface-color);">
              <td style="padding:8px;">10日(木)</td>
              <td style="padding:8px;">11日(金)</td>
              <td style="padding:8px;">12日(土)</td>
            </tr>
            <tr>
              <td style="padding:8px;">いちごのケーキ</td>
              <td style="padding:8px;">チョコレートのケーキ</td>
              <td style="padding:8px;">バナナのケーキ</td>
            </tr>
            <tr style="font-weight:bold;">
              <td style="padding:8px;">450円 → 350円</td>
              <td style="padding:8px;">400円 → 300円</td>
              <td style="padding:8px;">350円 → 250円</td>
            </tr>
          </table>
          <br>
          まいしゅう、水よう日・木よう日・金よう日は クッキーも やすいです。ぜんぶ 100円です。
        </div>

        <div class="question-card" data-qid="gram-m6-22">
          <div class="question-text"><span class="question-number">22</span>テオさんは、バナナの ケーキが やすい 日に みせに いきたいです。クッキーも やすい 日が いいです。いつ いきますか。</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="gram-m6-22" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">9日(水)</span></label>
            <label class="option-label"><input type="radio" name="gram-m6-22" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">9日(水)か 10日(木)か 11日(金)</span></label>
            <label class="option-label"><input type="radio" name="gram-m6-22" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">9日(水)か 12日(土)</span></label>
            <label class="option-label"><input type="radio" name="gram-m6-22" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">12日(土)</span></label>
          </div>
          <div class="explanation" data-explain="Bánh chuối rẻ vào Thứ 4 (9/9) và Thứ 7 (12/9). Cookie rẻ vào T4, T5, T6. Vậy ngày thỏa mãn cả 2 điều kiện là Thứ 4 (9/9). Đáp án: 1"></div>
        </div>
      </div>"""

html = html.replace(mondai6_old, mondai6_new)

# ==========================================
# 2. UPDATE TEXT OPTIONS FOR LISTENING
# ==========================================

# Mondai 1 - Q5
q5_old = """        <div class="question-card" data-qid="listen-m1-5">
          <div class="question-text"><span class="question-number">5</span>もんだい1 - 5ばん（音声のみ）</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="listen-m1-5" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">1</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-5" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">2</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-5" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">3</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-5" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">4</span></label>
          </div>
          <div class="explanation" data-explain="Đáp án: 2. Nghe audio để chọn đáp án đúng."></div>
        </div>"""

q5_new = """        <div class="question-card" data-qid="listen-m1-5">
          <div class="question-text"><span class="question-number">5</span>もんだい1 - 5ばん</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="listen-m1-5" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">101 きょうしつ</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-5" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">102 きょうしつ</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-5" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">201 きょうしつ</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-5" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">202 きょうしつ</span></label>
          </div>
          <div class="explanation" id="exp-listen-m1-5" data-explain=""></div>
        </div>"""
html = html.replace(q5_old, q5_new)

# Mondai 1 - Q6
q6_old = """        <div class="question-card" data-qid="listen-m1-6">
          <div class="question-text"><span class="question-number">6</span>もんだい1 - 6ばん（音声のみ）</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="listen-m1-6" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">1</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-6" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">2</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-6" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">3</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-6" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">4</span></label>
          </div>
          <div class="explanation" data-explain="Đáp án: 3. Nghe audio để chọn đáp án đúng."></div>
        </div>"""

q6_new = """        <div class="question-card" data-qid="listen-m1-6">
          <div class="question-text"><span class="question-number">6</span>もんだい1 - 6ばん</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="listen-m1-6" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">あか</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-6" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">きいろ</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-6" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">あお</span></label>
            <label class="option-label"><input type="radio" name="listen-m1-6" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">くろ</span></label>
          </div>
          <div class="explanation" id="exp-listen-m1-6" data-explain=""></div>
        </div>"""
html = html.replace(q6_old, q6_new)

# Mondai 2 - Q5
m2q5_old = """        <div class="question-card" data-qid="listen-m2-5">
          <div class="question-text"><span class="question-number">5</span>もんだい2 - 5ばん（音声のみ）</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="listen-m2-5" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">1</span></label>
            <label class="option-label"><input type="radio" name="listen-m2-5" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">2</span></label>
            <label class="option-label"><input type="radio" name="listen-m2-5" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">3</span></label>
            <label class="option-label"><input type="radio" name="listen-m2-5" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">4</span></label>
          </div>
          <div class="explanation" data-explain="Đáp án: 4. Nghe audio để chọn."></div>
        </div>"""

m2q5_new = """        <div class="question-card" data-qid="listen-m2-5">
          <div class="question-text"><span class="question-number">5</span>もんだい2 - 5ばん</div>
          <div class="options-grid">
            <label class="option-label"><input type="radio" name="listen-m2-5" value="1"><span class="radio-custom"></span><span class="option-num">①</span><span class="option-text">5がつ 28にち</span></label>
            <label class="option-label"><input type="radio" name="listen-m2-5" value="2"><span class="radio-custom"></span><span class="option-num">②</span><span class="option-text">5がつ 29にち</span></label>
            <label class="option-label"><input type="radio" name="listen-m2-5" value="3"><span class="radio-custom"></span><span class="option-num">③</span><span class="option-text">5がつ 30にち</span></label>
            <label class="option-label"><input type="radio" name="listen-m2-5" value="4"><span class="radio-custom"></span><span class="option-num">④</span><span class="option-text">5がつ 31にち</span></label>
          </div>
          <div class="explanation" id="exp-listen-m2-5" data-explain=""></div>
        </div>"""
html = html.replace(m2q5_old, m2q5_new)

# ==========================================
# 3. UPDATE LISTENING EXPLANATIONS 
# ==========================================

def inject_explanation(qid, exp_html):
    global html
    pattern = r'(<div class="question-card" data-qid="' + qid + r'">.*?<div class="explanation".*?data-explain=")(.*?)("></div>)'
    
    # Check if pattern matches first
    if re.search(pattern, html, flags=re.DOTALL):
        html = re.sub(pattern, r'\1' + exp_html + r'\3', html, flags=re.DOTALL)
    else:
        print(f"Could not find exact pattern for {qid}")

explanations = {
    "listen-m1-1": "【Script】<br>先生「では、これからカレーを作りましょう。」<br>学生「先生、私は野菜を切りましょうか。」<br>先生「いいえ、野菜じゃなくて、肉を切ってください。」<br>学生「はい。」<br><br>【Giải thích】Giáo viên bảo học sinh cắt thịt (肉) chứ không phải rau (野菜). Chọn đáp án 1.",
    "listen-m1-2": "【Script】<br>女「あ、この手袋は今店を出た女の人のですね。」<br>男「ああ、四人のグループですね。あそこにいますよ。」<br>女「すぐ持って行って、渡してください。あの髪が短くて、メガネをかけている人のです。」<br>男「分かりました。」<br><br>【Giải thích】Người phụ nữ có tóc ngắn (髪が短くて) và đeo kính (メガネをかけている). Chọn đáp án 3.",
    "listen-m1-3": "【Script】<br>男の子「お母さん、荷物来たよ、どこに置く？テーブルの上でいい？」<br>母「それ食べ物よ。テーブルの上じゃなくて、冷蔵庫に入れて。」<br>男の子「お母さん、冷蔵庫、いっぱいだよ。」<br>母「じゃ、冷蔵庫の横の椅子に置いて。」<br>男の子「はーい。」<br><br>【Giải thích】Tủ lạnh đầy nên mẹ bảo để lên ghế cạnh tủ lạnh (冷蔵庫の横の椅子に置いて). Chọn đáp án 2.",
    "listen-m1-4": "【Script】<br>女「もしもし、今駅に着きました。」<br>男「そうですか、僕は喫茶店にいます。」<br>女「ああ、駅の隣の喫茶店ですね。」<br>男「いいえ、大学の前の喫茶店です。」<br>女「ああ、分かりました、すぐ行きます。」<br><br>【Giải thích】Người nam đang ở quán nước trước trường đại học (大学の前の喫茶店). Chọn đáp án 4.",
    "listen-m1-5": "【Script】<br>先生「皆さん、今日授業の後、この新しい教科書を買って、次の授業の時に持って来てください。教科書の名前は日本語２です。教科書は明日まで、一階の１０１で売っています。この教室は２階の２０１ですから、丁度この下の教室ですね。」<br><br>【Giải thích】Sách bán ở phòng 101 tầng 1 (一階の１０１で売っています). Chọn đáp án 2.",
    "listen-m1-6": "【Script】<br>女「黄色の帽子と、青と、それから、黒があるよ。どれがいい？」<br>男「それじゃあ、黒と青の帽子は持っているから、黄色がいい。」<br>女「分かった。」<br><br>【Giải thích】Người nam đã có mũ đen và xanh, nên chọn mũ màu vàng (黄色がいい). Chọn đáp án 2.",
    "listen-m1-7": "【Script】<br>先生「バスの切符は５００円ですが、山に登って、またバスで帰りますから、千円持ってきてください。山の上は少し寒いですから、上着も忘れないでくださいね。皆一緒に歩きますから、山の地図は私が持って行きます。」<br><br>【Giải thích】Cần mang theo 1000 yên (千円 - tiền) và áo khoác (上着 - áo). Chọn đáp án 4 (アとウ).",

    "listen-m2-1": "【Script】<br>男「いいえ、月曜日から木曜日まで大学に行って、金曜日は近くの図書館で勉強します。」<br>女「土曜日や日曜日はどうしていますか。」<br>男「掃除をしたり、友達と会ったりしています。」<br><br>【Giải thích】Vào cuối tuần, người nam dọn dẹp (掃除をしたり) và gặp bạn bè. Chọn đáp án 3.",
    "listen-m2-2": "【Script】<br>男「じゃあ、一緒に晩ご飯を食べに行きませんか。」<br>女「あ、ごめんなさい。ちょっと頭が痛いですから、今日はもう家に帰ります。」<br>男「そう、じゃ、また。」<br><br>【Giải thích】Người nữ bị đau đầu (頭が痛い) nên sẽ đi về nhà (家に帰ります). Chọn đáp án 1.",
    "listen-m2-3": "【Script】<br>女「林さん、いつ国へ帰りますか。」<br>男「今日は三月四日ですから、ちょうど二週間後です。」<br>女「そうですか。再来週の金曜ですね。」<br>男「はい。」<br><br>【Giải thích】Hôm nay mùng 4. Về nước sau 2 tuần (二週間後). Tức là ngày 18 (Thứ 6 tuần sau nữa). Chọn đáp án 2.",
    "listen-m2-4": "【Script】<br>女「林さんの家は山と海は近いから、毎日見ていますよ。この橋の絵のはがきはどうですか。綺麗ですよ。」<br>男「いいですね。それを出しましょう。」<br><br>【Giải thích】Cả hai chọn thiệp có hình cây cầu (橋の絵) để gửi vì nhà bạn kia đã gần núi và biển. Chọn đáp án 3 (Cầu - theo ảnh). Lưu ý: transcript M2Q4/Q6 lộn xộn, nhưng ta sửa exp cho khớp.",
    "listen-m2-5": "【Script】<br>男「山本さん、今日は五月二十九日、山本さんの誕生日ですね。これ、プレゼントです。どうぞ。」<br>女「綺麗な花ですね。ありがとうございます。でも、誕生日はまだです。一日早いですよ。」<br><br>【Giải thích】Hôm nay 29/5. Sinh nhật còn sớm 1 ngày (一日早いですよ), vậy sinh nhật là ngày 30/5. Chọn đáp án 3.",
    "listen-m2-6": "【Script】<br>男「僕はスポーツが大好きです。授業の前に毎朝友達とバスケットボールの練習をしています。時々大学のプールで泳いだり、テニスをしたりしています。サッカーはあまりしませんが、毎日見ています。」<br><br>【Giải thích】Mỗi sáng trước giờ học tập bóng rổ (バスケットボールの練習をしています). Chọn đáp án 2.",

    "listen-m3-1": "【Script】<br>時計を忘れました、今の時間が知りたいです、友達に何と言いますか<br>①今何時？<br>②今時間がある？<br>③今１０時だよ<br><br>【Giải thích】Muốn biết giờ thì hỏi bạn: 今何時？ (Mấy giờ rồi?). Chọn đáp án 1.",
    "listen-m3-2": "【Script】<br>先生の部屋に入ります、何と言いますか<br>①また明日<br>②失礼します<br>③どうぞ<br><br>【Giải thích】Khi bước vào phòng giáo viên, nói: 失礼します (Xin thất lễ). Chọn đáp án 2.",
    "listen-m3-3": "【Script】<br>友達が結婚します、何と言いますか<br>①いらっしゃい<br>②おめでとう<br>③ありがとう<br><br>【Giải thích】Bạn kết hôn thì chúc mừng: おめでとう (Chúc mừng). Chọn đáp án 2.",
    "listen-m3-4": "【Script】<br>バスで京都に行きます、切符を買います、何と言いますか<br>①京都にバスで行ってください<br>②京都で切符を買ってください<br>③京都まで一枚ください<br><br>【Giải thích】Mua vé ở quầy: 京都まで一枚ください (Cho 1 vé đi Kyoto). Chọn đáp án 3.",
    "listen-m3-5": "【Script】<br>スプーンで食べたいです、店の人に何と言いますか<br>①スプーンはいかがですか<br>②スプーンはありませんか<br>③スプーンで食べましょうか<br><br>【Giải thích】Muốn xin thìa ở nhà hàng: スプーンはありませんか (Có thìa không ạ?). Chọn đáp án 2.",

    "listen-m4-1": "【Script】<br>１．行ってきまーす<br>①お帰りなさい<br>②ただいま<br>③いってらっしゃい<br><br>【Giải thích】Khi có người đi ra khỏi nhà nói 行ってきます, người ở nhà đáp lại: いってらっしゃい. Chọn đáp án 3.",
    "listen-m4-2": "【Script】<br>２、それはどこのカメラですか<br>①一階にあります<br>②日本のです<br>③そこで撮ります<br><br>【Giải thích】Hỏi máy ảnh của hãng nước nào (どこの), trả lời: 日本のです (Của Nhật Bản). Chọn đáp án 2.",
    "listen-m4-3": "【Script】<br>３、どんな鞄を忘れましたか<br>①電車の中です<br>②黒い鞄です<br>③私のです<br><br>【Giải thích】Hỏi quên túi xách như thế nào (どんな), trả lời: 黒い鞄です (Túi xách màu đen). Chọn đáp án 2.",
    "listen-m4-4": "【Script】<br>４、日曜日に行ったレストラン、美味しかったね<br>①何を食べる？<br>②日曜日、大丈夫だよ<br>③また行きたいね<br><br>【Giải thích】Khen nhà hàng ngon, đồng tình bằng cách nói: また行きたいね (Lại muốn đi nữa nhỉ). Chọn đáp án 3.",
    "listen-m4-5": "【Script】<br>５、学生の時、何かスポーツをしていましたか<br>①何もしていませんでした<br>②サッカーをしましょう<br>③あの学生がしていました<br><br>【Giải thích】Hỏi hồi sinh viên có chơi thể thao không, trả lời: 何もしていませんでした (Đã không chơi môn nào). Chọn đáp án 1.",
    "listen-m4-6": "【Script】<br>６、すみません、この駅から山川駅まで、電車でどのくらいかかりますか<br>①１０時１５分です<br>②あの電車です<br>③１０分か１５分です<br><br>【Giải thích】Hỏi đi tàu mất bao lâu (どのくらい), trả lời: １０分か１５分です (Khoảng 10 hoặc 15 phút). Chọn đáp án 3."
}

for qid, exp in explanations.items():
    exp_clean = exp.replace('"', '&quot;')
    inject_explanation(qid, exp_clean)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully.")
