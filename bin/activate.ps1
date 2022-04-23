$venv = $args[0]
$command = $args | Select-Object -Skip 1
Invoke-Expression "$venv/Scripts/activate"
Invoke-Expression "$command"