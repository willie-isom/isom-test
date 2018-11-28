import os, re, time

#os.system('autoRun0.py')
#time.sleep(5)

		
if os.path.isfile('alarmNum.txt'): 
	with open('alarmNum.txt', 'r') as file :
		alarmNum = file.readline().strip()

		if os.path.isfile('alarmList.txt'): 
			with open('alarmList.txt', 'r') as file :
				alarmList = file.readline()
				
				while alarmList:
					if re.search(alarmNum, alarmList):
						alarmList = alarmList[7:]
						break						
					alarmList = file.readline()
					
				with open('alarmText.txt', 'w+') as file: 
					file.write(alarmList)

from PIL import ImageGrab
pic = ImageGrab.grab()
fn = time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'
pic.save('isom-test\\' + fn )

with open('imageFileName.txt', 'w+') as file :
	file.write(fn)


os.system('isom-test\autoRun.bat')
time.sleep(10)
					
os.system('MsgSend.py')

