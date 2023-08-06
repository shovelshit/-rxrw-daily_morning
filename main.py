from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage


if __name__ == '__main__':
    app_id = 'wx55df960f0cbfb4c8'
    app_secret = 'cdc86c244b30515880b081240da066c3'

    user_id = 'oxFGf6YLSO75rd2wDJG4o3VKrxTk'
    template_id = 'eu7AtjfedSGtIRED_k9NabiejmJBwv3Z7HW80lwajJU'

    client = WeChatClient(app_id, app_secret)

    wm = WeChatMessage(client)
    data = {}
    res = wm.send_template(user_id, template_id, data)
    print(res)