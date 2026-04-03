if ((Get-Command "cunt").CommandType -eq "Function") {
	cunt @args;
	[Console]::ResetColor()
	exit
}

"First time use of cunt detected. "

if ((Get-Content $PROFILE -Raw -ErrorAction Ignore) -like "*cunt*") {
} else {
	"  - Adding cunt intialization to user `$PROFILE"
	$script = "`n`$env:PYTHONIOENCODING='utf-8' `niex `"`$(cunt --alias)`"";
	Write-Output $script | Add-Content $PROFILE
}

"  - Adding cunt() function to current session..."
$env:PYTHONIOENCODING='utf-8'
iex "$($(cunt --alias).Replace("function cunt", "function global:cunt"))"

"  - Invoking cunt()`n"
cunt @args;
[Console]::ResetColor()
