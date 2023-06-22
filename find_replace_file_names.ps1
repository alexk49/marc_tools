# use case .\find_replace_file_names.ps1 -old "old_pattern" -new "new_pattern" -path C:\users\files\location"
# not strictly for marcs but often useful when needing to make changes to files sorted via marc edit

param(
    [Parameter(Mandatory)]
    [String]$old,
    [String]$new,
    [Parameter(Mandatory)]
    [String]$path
    )

if (Test-Path -Path $path) {
    "Valid path given"
    "Old file name given: $old"
    "New file name given: $new"
} else {
    'Invalid file loc\nUse case: .\find_replace_file_names.ps1 -old "old_pattern" -new "new_pattern" -path "C:\users\files\location"'
}

# Getting all files that match $pattern in a folder.
# Add '-Recurse' switch to include files in subfolders.
# ! $_.PSIsContainer checks that something is not a folder
$search_results = Get-ChildItem -Path $path | Where-Object { ((! $_.PSIsContainer) -and ($_.Name -match $old))} 

foreach ($file in $search_results) {
    $new_name = $file.Name -replace $old, $new

    # test changes with: Rename-Item -WhatIf -Path $file.FullName -NewName $new_name
    # commit changes with:
    Rename-Item -Path $file.FullName -NewName $new_name
}

Write-Output "All files in given folder path renamed"
