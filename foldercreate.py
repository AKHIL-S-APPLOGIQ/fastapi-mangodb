import os

# Define the folder and file structure
structure = {
    "project": {
        "app": {
            "api": {
                "student": {
                    "router.py": "",
                    "controller.py": "",
                    "schemas.py": ""
                }
            },
            "config": {
                "database.py": ""
            },
            "main.py": ""
        },
        ".env": "",
        "requirements.txt": "",
        "README.md": ""
    }
}

def create_structure(base_path, tree):
    for name, content in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ FastAPI project structure created successfully.")
