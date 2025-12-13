#!/bin/bash
# Script để commit và push feature users-authentication
# Chạy script này: bash commit_feature.sh

echo "=== BlueMoon - Commit Feature Users Authentication ==="

# Kiểm tra git
if [ ! -d .git ]; then
    echo "Khoi tao git repository..."
    git init
fi

# Kiểm tra remote
if ! git remote | grep -q origin; then
    echo "Chua co remote repository!"
    echo "Hay them remote repository bang lenh:"
    echo "git remote add origin <URL_REPO>"
    exit 1
fi

# Tạo branch mới
echo ""
echo "Tao branch feature/users-authentication..."
git checkout -b feature/users-authentication 2>/dev/null || git checkout feature/users-authentication

# Hiển thị status
echo ""
echo "Trang thai cac file:"
git status

# Hỏi xác nhận
echo ""
read -p "Ban co muon add va commit cac thay doi? (y/n) " confirm
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "Huy bo."
    exit 0
fi

# Add files
echo ""
echo "Them cac file vao staging area..."
git add .

# Commit
echo "Commit cac thay doi..."
git commit -m "feat: Implement user authentication and authorization system

- Add User model with password hashing and role management
- Implement login/logout functionality
- Add user management (CRUD) for admin
- Create permission decorators (@admin_required, @canbo_required)
- Add login page template with Django forms
- Add user list and user form templates
- Protect views with authentication and authorization
- Add management command to create admin user"

if [ $? -eq 0 ]; then
    echo ""
    echo "Commit thanh cong!"
    
    # Hỏi có muốn push không
    echo ""
    read -p "Ban co muon push len remote repository? (y/n) " push
    if [ "$push" = "y" ] || [ "$push" = "Y" ]; then
        echo "Push len remote repository..."
        git push -u origin feature/users-authentication
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "=== HOAN TAT ==="
            echo "Da push feature len repository thanh cong!"
            echo "Hay tao Pull Request tren GitHub/GitLab de merge vao main branch."
        else
            echo ""
            echo "Loi khi push!"
            echo "Kiem tra lai remote repository URL."
        fi
    else
        echo ""
        echo "Chua push. Ban co the push sau bang lenh:"
        echo "git push -u origin feature/users-authentication"
    fi
else
    echo ""
    echo "Loi khi commit!"
fi

