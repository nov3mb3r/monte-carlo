param(
[Parameter(Mandatory=$True)]
[String]$path,

[Parameter(Mandatory=$True)]
[String]$output

[string]$op = "UserLoggedIn"
)
New-Item -ItemType Directory -Force -Path $output

$ErrorActionPreference = 'SilentlyContinue'

$files=Get-ChildItem -Path $path *csv -Name

#CSV parsing
foreach ($audit_file in $files){
	#Get only Operations
	$ImportedData = Import-CSV -Path $path\$audit_file | Where-Object {$_.Operations -eq $op}
	write-output "Processing: $audit_file"
	$ImportedData.AuditData | ConvertFrom-JSON | Select CreationTime, UserID, ClientIP | Export-CSV -Path $output\exported$audit_file -NoTypeInformation 
	}