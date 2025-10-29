# 🎬 Movies Manager

Movies Manager is a Python-based application designed to manage and analyze movie data stored in CSV files. It features a menu-driven interface and is built for simplicity, extensibility, and educational purposes.

## 🚀 Features

- Load and display movie datasets
- Add, remove, search and mark seen movies
- Interactive menu interface
- Modular Python scripts for easy maintenance

## 🛠️ Technologies

- **Python**: Core logic and data processing
- **CSV**: Lightweight data storage
- *(Optional)* **Node.js**: Git hooks and commit conventions (if re-enabled later)

## 📁 Project Structure

```
movies-manager/
├── menu.py               # Main interactive interface
├── add-col.py            # Script to add columns to CSV files
├── movies.csv            # Movie dataset
├── documentaries.csv     # Documentary dataset
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
```

## 📦 Setup

```bash
# Clone the repository
git clone https://github.com/adoudi-mondher/movies-manager.git
cd movies-manager

# Run the Python interface
python menu.py
```

## ✅ Commit Guidelines

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) manually:

- `feat:` for new features  
- `fix:` for bug fixes  
- `docs:` for documentation updates  
- `refactor:` for code improvements without behavior change

Example:

```bash
git commit -m "feat: add search by title"
```

## 📌 Future Plans

- Add unit tests
- Integrate a database (e.g., SQLite)
- Optional GUI interface
- Re-enable Git hooks with Husky and Commitlint
