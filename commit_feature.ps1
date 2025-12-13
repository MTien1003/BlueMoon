# Script để commit và push feature users-authentication
# Chạy script này trong PowerShell: .\commit_feature.ps1

Write-Host "=== BlueMoon - Commit Feature Users Authentication ===" -ForegroundColor Cyan

# Kiểm tra git
if (-not (Test-Path .git)) {
    Write-Host "Khoi tao git repository..." -ForegroundColor Yellow
    git init
}

# Kiểm tra remote
$remote = git remote -v
if (-not $remote) {
    Write-Host "Chua co remote repository!" -ForegroundColor Red
    Write-Host "Hay them remote repository bang lenh:" -ForegroundColor Yellow
    Write-Host "git remote add origin <URL_REPO>" -ForegroundColor Yellow
    exit
}

# Tạo branch mới
Write-Host "`nTao branch feature/users-authentication..." -ForegroundColor Yellow
git checkout -b feature/users-authentication 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Branch da ton tai, chuyen sang branch..." -ForegroundColor Yellow
    git checkout feature/users-authentication
}

# Hiển thị status
Write-Host "`nTrang thai cac file:" -ForegroundColor Cyan
git status

# Hỏi xác nhận
$confirm = Read-Host "`nBan co muon add va commit cac thay doi? (y/n)"
if ($confirm -ne "y" -and $confirm -ne "Y") {
    Write-Host "Huy bo." -ForegroundColor Red
    exit
}

# Add files
Write-Host "`nThem cac file vao staging area..." -ForegroundColor Yellow
git add .

# Commit
Write-Host "Commit cac thay doi..." -ForegroundColor Yellow
$commitMessage = @"
feat: Implement user authentication and authorization system

- Add User model with password hashing and role management
- Implement login/logout functionality
- Add user management (CRUD) for admin
- Create permission decorators (@admin_required, @canbo_required)
- Add login page template with Django forms
- Add user list and user form templates
- Protect views with authentication and authorization
- Add management command to create admin user
"@

git commit -m $commitMessage

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nCommit thanh cong!" -ForegroundColor Green
    
    # Hỏi có muốn push không
    $push = Read-Host "`nBan co muon push len remote repository? (y/n)"
    if ($push -eq "y" -or $push -eq "Y") {
        Write-Host "Push len remote repository..." -ForegroundColor Yellow
        git push -u origin feature/users-authentication
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n=== HOAN TAT ===" -ForegroundColor Green
            Write-Host "Da push feature len repository thanh cong!" -ForegroundColor Green
            Write-Host "Hay tao Pull Request tren GitHub/GitLab de merge vao main branch." -ForegroundColor Cyan
        } else {
            Write-Host "`nLoi khi push!" -ForegroundColor Red
            Write-Host "Kiem tra lai remote repository URL." -ForegroundColor Yellow
        }
    } else {
        Write-Host "`nChua push. Ban co the push sau bang lenh:" -ForegroundColor Yellow
        Write-Host "git push -u origin feature/users-authentication" -ForegroundColor Cyan
    }
} else {
    Write-Host "`nLoi khi commit!" -ForegroundColor Red
}

