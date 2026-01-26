# Ubuntu File and Folder Naming Best Practices

Proper naming conventions prevent issues with scripts, terminals, and cross-platform compatibility.

## 1. Avoid Spaces
Spaces in filenames require escaping in the terminal (`my\ file.txt`).
- **Bad**: `My Data Report.pdf`
- **Good**: `my-data-report.pdf` (kebab-case) or `my_data_report.pdf` (snake_case)

## 2. Use Lowecase
Linux is case-sensitive. `MyFile.txt` and `myfile.txt` are two different files. Using all lowercase prevents confusion and typos.

## 3. Be Descriptive but Short
- **Bad**: `f1.sh`, `stuff.zip`
- **Good**: `backup-db.sh`, `project-assets-2023.zip`

## 4. Include Dates (YYYY-MM-DD)
Starting names with dates allows for easy chronological sorting.
- `2023-10-27-log.txt`

## 5. Extensions Matter
Always include extensions (`.sh`, `.txt`, `.conf`) so that you and the system know the file type immediately.

---
*For more basics, see **[File Management](ubuntu-file-folder-management.md)**.*
