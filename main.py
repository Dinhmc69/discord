print("HI")
import requests
msg = "Auto send from auto download and run code"
webhook_url = "https://discord.com/api/webhooks/1376571321168691322/b1NBoB9TTySn-b4R-r6e_5lcvDqsVNSBfPQMgNoBJNXeIjjFl7reUOXX1U-6TT0vINgr"
payload = {"content": msg}
requests.post(webhook_url, data=payload, timeout=30)
