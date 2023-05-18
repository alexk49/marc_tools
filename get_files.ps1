<# used for getting requested files out of a marc file that's been split by eisbn
this will work when requested files are supplied in a txt format containing the required eisbn, with a new line for each one
It is generally easiest to place your data file in the same location as the marcs.
use case: .\get_files.ps1 -file "data_file_name" -path "path_to_folder_containg_marcs" #>

param(
    [Parameter(Mandatory)]
    [String][$file],
    [String][$path]
    )

$files = Get-ChildItem -Path $path | Where-Object { ((! $_.PSIsContainer)) }

foreach($line in Get-Content $file) {
    $marc = $line + ".mrc"
    if ($marc -In $files.Name) {
        Write-Output "found $marc"
        Copy-Item $marc .\wanted
    }
}
