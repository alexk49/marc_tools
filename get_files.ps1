<# used for getting requested files out of a marc file that's been split by eisbn
place data file, which should be a list of eisbns in a txt file on a new line for each in data folder
place split by eisbn marc file in source folder
#>

$DATA = '.\data'
$OUTPUT = '.\output'
$SOURCE = '.\source'

$files = Get-ChildItem -Path $SOURCE | Where-Object { ((! $_.PSIsContainer)) }

$source_files = Get-ChildItem -Path $DATA | Where-Object { ((! $_.PSIsContainer)) }

foreach($source_file in $source_files) {
    foreach($line in Get-Content $source_file.FullName) {
        $marc = $line + ".mrc"
        if ($marc -In $files.Name) {
            Write-Output "found $marc"
            $marc_file = $SOURCE, $MARC -join "/" 
            Copy-Item $marc_file $OUTPUT
        }
    }
}
