from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import os

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
data = {}
res = wm.send_template(user_id, template_id, data)
print(res)
