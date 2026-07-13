set last_three=%1
set ip=192.168.8.%last_three%

scp .\latencytest_recieve.py ubuntu@%ip%:\home\ubuntu\connections