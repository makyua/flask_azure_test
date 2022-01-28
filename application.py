from flask import Flask,render_template,request

app = Flask(__name__)

# エンドポイントの作成
# GETとPOSTの両方を使うことで動作を変える
@app.route("/", methods=["GET", "POST"])
def main_page():
    #デフォルトの表示
    if request.method == 'GET':
        text = "ここに結果が出力されます"
        return render_template("page.html", text=text)
    # ユーザからの入力後
    elif request.method == 'POST':
        name = request.form["name"]
        text = "こんにちは" + name + "さん"
        return render_template("page.html", text=text)

# 実行
if __name__ == "__main__":
    app.run(debug=True)