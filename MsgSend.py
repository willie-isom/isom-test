from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError
from linebot.models import ImageSendMessage, LocationSendMessage, StickerSendMessage
import os, time


time.sleep(1)

CHANNEL_ACCESS_TOKEN = "gi2NdIngaDaOHkfhfBWR8zLH2OAgaTWE2+2lE/cO9qe99Bu0ssQdn7cwb6fkyv/+oHMWYgLueyuymUi6O6uDVzF0RUt4Hzyem3b6BrqaPoPC1KPue96tK5cuOFa/egyOIB69ZWrdJ2cDxwQFon2h1wdB04t89/1O/w1cDnyilFU="
to = "C53b5598030c8990ab7e2f525ecdf02e0"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

imageFileName = ''
if os.path.isfile('imageFileName.txt'): 
	with open('imageFileName.txt', 'r') as file :
		imageFileName = file.readline().strip()


#文字訊息
import os
alarmText = ''
if os.path.isfile('alarmText.txt'): 
	with open('alarmText.txt', 'r') as file :
		alarmText = file.readline().strip()
try:
	line_bot_api.push_message(to, TextSendMessage(text=alarmText))
except LineBotApiError as e:
	raise e
	
try:
	line_bot_api.push_message(to, TextSendMessage(text='https://github.com/willie-isom/isom-test/blob/master/1.xlsx?raw=true'))
except LineBotApiError as e:
	raise e

#圖片訊息
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
image_url = r"https://raw.githubusercontent.com/willie-isom/isom-test/master/" + imageFileName

try:
	line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
except LineBotApiError as e:
	raise e

#StickerSendMessage貼圖 https://devdocs.line.me/files/sticker_list.pdf
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
package_id = "4"
sticker_id = "263"
try:
	pass
    #line_bot_api.push_message(to, StickerSendMessage(package_id=package_id, sticker_id=sticker_id))
except LineBotApiError as e:
    raise e
	
	
	
#U25516cf66eedab6441c53476784f9a86 joe
#C6e3cfc20502321297930727884292a63  1紀
#U535bb22b1009cf68df522435b11cf407 willie