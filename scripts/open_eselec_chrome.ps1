$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$profileDirectory = "Profile 1"

if (-not (Test-Path -LiteralPath $chromePath)) {
    Write-Error "No encontre Chrome en: $chromePath"
    exit 1
}

Start-Process -FilePath $chromePath -ArgumentList @("--profile-directory=$profileDirectory")
Write-Output "Chrome E-SELEC abierto con profile-directory=$profileDirectory."
