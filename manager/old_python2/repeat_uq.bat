:start
echo "Calling uploadqueue.py"
python uploadqueue.py
echo "Script has terminated"
echo "Sleeping for 30 seconds"
timeout /t 30
echo "Reiterating loop"
goto start