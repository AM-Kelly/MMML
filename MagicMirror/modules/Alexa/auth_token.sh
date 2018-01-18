CLIENT_ID="amzn1.application-oa2-client.a55ec5f131ce4b448c33ceeb0489bc99"
CLIENT_SECRET="774616512f1f93f8568b47c0ab48299cf2f80ab89b5e93ff897ad5a76ffa3743"
CODE="ANKNpliysRKKoPfDtvGH"
GRANT_TYPE="authorization_code"
REDIRECT_URI="https://localhost:9745/authresponse"

curl -X POST --data "grant_type=${GRANT_TYPE}&code=${CODE}&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&redirect_uri=${REDIRECT_URI}" https://api.amazon.com/auth/o2/token
