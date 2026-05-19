$pythonArgs = @("scripts/chrome_debug_helper.py", "open")

python @pythonArgs
exit $LASTEXITCODE
