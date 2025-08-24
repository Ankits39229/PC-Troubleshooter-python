@echo off
title PC Troubleshooter v1.0.0 (Administrator)
echo Starting PC Troubleshooter with Administrator privileges...
echo This may prompt for UAC confirmation.
powershell -Command "Start-Process 'PC_Troubleshooter.exe' -Verb RunAs"
