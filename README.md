# sth-like-Multipoint-OneButtonBTDeviceSwitch
Easily switch your bluetooth headphones between Android phone and Windows computer without multipoint

This Is mine try to make one button device switch, It's not super fast, but 5 seconds Isn't  much either
You can edit it, use it, it's free. If you have some questions or bug fixes, feel free to e-mail me at beniaminwawrzosek4@gmail.com

So mostly it's not mine work, I just combined a few packages together.
I used: Microdroid, BluetoothCLTools, win10-bluetooth-headphones githup repo from stanleyguevara and a Python code (mostly typed by Chat GPT)
	Microdroid: https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&gl=US
  BluetoothCLTools: https://bluetoothinstaller.com/bluetooth-command-line-tools
  stanleyguevara repo: https://github.com/stanleyguevara/win10-bluetooth-headphones
  some ideas are from: https://www.addictivetips.com/windows-tips/connect-a-bluetooth-device-with-a-hotkey-on-windows-10
  
# INSTRUCTIONS
	
	1. Install Macrodroid from playstore (or send me e-mail for apk)
	2. Download to your smarthone and import BT-Switch.macro by opening it in files manager and from there opening it in Macrodroid app.
	3. Edit triggers so quick tiles are turned on. Then add them to your quick tile list.
	4. Check your computers ip (there are plenty instructions in internet) and set it to static on your router (same thing. Ps. It's called DHCP IP reservation)
	5. Go back to Macrodroid and configure UDP Command so destination IP is you computer IP (there are two commands that need to be configured)
	6. Configure "Connect Audio Device" tile so your headphone device is chosen
	7. Save MacroDroid file and turn it on
	8. Install BluetoothCLTools by downloading it from: https://bluetoothinstaller.com/bluetooth-command-line-tools/BluetoothCLTools-1.2.0.56.exe and starting .exe file
	9. Edit mutipoint-hack.bat by replacing "your destination folder path" with folder path of repo folder
	10. Click WIN + R on keyboard, paste shell:startup and click ENTER, paste mutipoint-hack.bat file into that folder. This will allow the program to autostart when you turn on your computer
	11. Install python 3 from microsoft store https://www.microsoft.com/store/productId/9PJPW5LDXLZ5
	12. Edit BT-switch.py by replacing "your destination folder path" with folder path of repo folder
	13. Click WIN key and type "cmd" and run it, paste "btdiscovery" and click enter, copy mac adres of your device from step 6 (it's xx:xx:xx:xx:xx:xx code)
	14. Paste mac adres into \win10-bluetooth-headphones-master\mac.txt
	
	Now when you turn off quick settings tile BT device should disconnect from your phone and connect to your computer after 5 seconds
	Ps. instalation istructions were NOT tested so I may have missed something!
