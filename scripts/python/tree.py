import os
from pathlib import Path

def show_tree(directory, prefix="", max_depth=3, current_depth=0):
    if current_depth > max_depth:
        return
    
    directory = Path(directory)
    
    # Get items and filter out noise
    try:
        items = [item for item in directory.iterdir() if should_include(item)]
        items = sorted(items)
    except PermissionError:
        return
    
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{item.name}")
        
        if item.is_dir() and current_depth < max_depth:
            next_prefix = prefix + ("    " if is_last else "│   ")
            show_tree(item, next_prefix, max_depth, current_depth + 1)

def should_include(item):
    """Filter out unwanted files and directories"""
    exclude_dirs = {
        'node_modules', '.venv', '__pycache__', '.git', 
        'dist', 'build', '.next', 'coverage', '.nyc_output'
    }
    
    exclude_files = {
        '.DS_Store', 'Thumbs.db', '*.log', '.env.local', 
        '.env.development.local', '.env.test.local', '.env.production.local'
    }
    
    # Skip hidden files except important ones
    if item.name.startswith('.') and item.name not in ['.env', '.gitignore', '.dockerignore']:
        return False
    
    # Skip excluded directories
    if item.is_dir() and item.name in exclude_dirs:
        return False
        
    # Skip excluded files
    if item.is_file() and item.name in exclude_files:
        return False
    
    return True

if __name__ == "__main__":
    project_root = input("Enter project path (or press Enter for current directory): ").strip()
    if not project_root:
        project_root = "."
    
    print(f"\nProject structure for: {os.path.abspath(project_root)}")
    print("=" * 50)
    show_tree(project_root)