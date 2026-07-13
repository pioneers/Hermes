set last_three=%1

ssh ubuntu@192.168.8.%last_three% python3 connections/latencytest_recieve.py