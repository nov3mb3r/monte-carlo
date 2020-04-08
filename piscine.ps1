#Make excel speadsheets, according to csv
param(
[Parameter(Mandatory=$True)]
[String]$path
)

$excel = New-Object -ComObject excel.application
$excel.visible = $True
$workbook = $excel.Workbooks.add() 
#Adding Sheets 

$files=Get-ChildItem -Path $path -Name

    foreach($input_file in $files){ 
		#Name the sheet
        $s4 = $workbook.Sheets.add() 
		write-host $input_file
        $s4.name = ($input_file -split "\.")[0]
		
	}

# The default workbook has three sheets, remove them 
    ($s1 = $workbook.sheets | where {$_.name -eq "Sheet1"}).delete()  
 
#Saving File 
    "`n" 
    write-Host -for Yellow "Apolele"
    $workbook.SaveAs("C:\ExcelWorkbook.xlsx")
	$Excel.Quit() 