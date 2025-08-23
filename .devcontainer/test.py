import os
import requests

# 環境変数から読み込み（Streamlit SecretsでもOK）
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_ENDPOINT")
deployment = os.getenv("OPENAI_DEPLOYMENT")
api_version = os.getenv("OPENAI_API_VERSION")

# URL構築
url = f"{endpoint}openai/deployments/{deployment}/chat/completions?api-version={api_version}"

# デバッグ出力
print("🔧 URL:", url)
print("📦 デプロイ名:", deployment)
print("🔑 APIキー:", api_key[:5], "...省略")

# テスト用リクエスト
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

data = {
    "messages": [{"role": "user", "content": "こんにちは"}],
    "max_tokens": 50
}

response = requests.post(url, headers=headers, json=data)

# 結果表示
print("📨 ステータスコード:", response.status_code)
print("🧾 応答内容:", response.json())
