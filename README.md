# election-software
WORKING ELECTION SOFTWARE ON A LOCAL SERVER

###--Main Computer[SERVER COMPUTER]--###

#Open CMD
  - type in cd /d [file location of the server folder]
  - once you are in the server folder run the python file as by typing [python svr.py] or [py svr.py]
  - YOU CAN CHANGE THE POSTS/CANDIDATES NAME

###--Program Running Computer--###

#install pillow
  - go to cmd and run "pip install pillow" or "py -m pip install pillow"

#Open [Main.py] 
  - press ctrl+f
  - search "Ipaddress" and Add IPADRESS of the Server Computer (the computer where the server is running and votes are being stored)
                  - [how to find ipaddress?] go to server computer run cmd, "ipconfig" and copy paste the IPv4 Address in "Ipaddress" for example - [192.168.xx.xxx]
  - Replace the File locations of the background and candidate's images
  - Replace name/posts if you want

#After the Server is run and votes are given a [votes.csv] file is automatically generated (if not existing) in the server folder where the number of votes are stored
