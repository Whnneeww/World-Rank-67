from http.server import BaseHTTPRequestHandler, HTTPServer 
import urllib.parse 
class MyHandler(BaseHTTPRequestHandler): 
    def <strong>init</strong>(self, <em>args, </em><em>kwargs): 
        super().<strong>init</strong>(</em>args, **kwargs) 
        self.stored_values = [0, 0, 0]  # 初期値を0に設定 
<pre><code>def do_GET(self): 
    # URLからパラメータを取得 
    parsed_url = urllib.parse.urlparse(self.path) 
    query_params = urllib.parse.parse_qs(parsed_url.query) 
 
    # 'value'パラメータを取得 
    value = query_params.get('value', [None])[0] 
    if value is None: 
        self.send_error(400, "URLパラメータ 'value' が指定されていません") 
        return 
 
    try: 
        value = int(value)  # 値を整数に変換 
    except ValueError: 
        self.send_error(400, "URLパラメータ 'value' は整数ではありません") 
        return 
 
    # 保存された値と比較して、最大値を更新 
    for i in range(3): 
        if value &gt; self.stored_values[i]: 
            self.stored_values[i] = value 
            break 
 
    # HTTPレスポンスを設定 
    self.send_response(200) 
    self.send_header('Content-type', 'text/plain') 
    self.end_headers() 
 
    # 保存された最大値を送信 
    response = f"保存された最大値: {self.stored_values}" 
    self.wfile.write(response.encode()) 
