import webbrowser
import time

total_breaks=3
break_count=0
print("this program statred on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(10*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=VgQUwsUHdqc")
    break_count=break_count+1
    
