function clitools {
    param(
        [string]$command,
        [string]$arg
    )

    # Construct the Python command dynamically based on input
    if ($command -eq "add" -or $command -eq "remove" -or $command -eq "jump") {
        $output = $(python "C:\Users\ishha\OneDrive\Desktop\CSI_TASK\cli_tool\clitools.py" $command $arg).Trim()
    } elseif ($command -eq "query") {
        $output = $(python "C:\Users\ishha\OneDrive\Desktop\CSI_TASK\cli_tool\clitools.py" $command).Trim()
    } else {
        Write-Host "Usage: clitools {add|query|remove|jump} [directory/keyword]"
        return
    }

    # Handle the output based on command
    if ($command -eq "jump") {
        if ($output -and (Test-Path -Path $output -PathType Container)) {
            Write-Host "Changed directory to: $output"
            Set-Location -Path $output
        } else {
            Write-Host "No matching directory found. Consider adding the directory first."
        }
    } else {
        Write-Host $output
    }
}
