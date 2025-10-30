# 🎬 Movies Manager

Movies Manager is a Python-based application designed to manage and analyze movie data stored in CSV files. It features both a classic command-line interface and a modern interactive UI with rich styling.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 🚀 Features

### Core Features
* 📋 Load and display movie datasets
* ➕ Add new movies to your collection
* 🗑️ Remove movies from the catalog
* 🔍 Search movies by title
* ✅ Mark movies as seen/unseen
* 📊 View collection statistics

### v2.0 Enhancements
* 🎨 **Rich UI**: Beautiful tables and styled output with colors
* ⌨️ **Interactive Menus**: Arrow key navigation with `inquirer`
* 🎯 **Smart Prompts**: Input validation and confirmation dialogs
* 📈 **Statistics Dashboard**: Track watched vs unwatched movies
* 🎭 **Filter Options**: View movies by watch status
* ✨ **Better UX**: Clear success/error messages with emoji

---

## 🛠️ Technologies

* **Python 3.8+**: Core logic and data processing
* **CSV**: Lightweight data storage
* **inquirer**: Interactive command-line prompts
* **rich**: Terminal styling and formatting
* **tabulate**: Table display (v1.0 compatibility)

---

## 📁 Project Structure

```
movies-manager/
├── menu.py                  # Classic interface (v1.0)
├── menu_v2.py              # Modern interface (v2.0) ⭐ NEW
├── functions/
│   ├── display.py          # Display movies
│   ├── search.py           # Search functionality
│   ├── seen.py             # Mark as seen
│   ├── add.py              # Add movies
│   ├── remove.py           # Remove movies
│   └── ui/                 # UI components ⭐ NEW
│       ├── prompts.py      # Interactive prompts
│       └── display.py      # Rich styling
├── movies.csv              # Movie dataset
├── documentaries.csv       # Documentary dataset
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/adoudi-mondher/movies-manager.git
cd movies-manager
```

### 2. Create a virtual environment (recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application

**Option A: Modern UI (v2.0 - Recommended)**
```bash
python menu_v2.py
```

**Option B: Classic UI (v1.0 - Stable)**
```bash
python menu.py
```

---

## 🎮 Usage

### v2.0 Interface (menu_v2.py)

```
🎬 Movies Manager v2.0

What do you want to do?
❯ 🎬 Show all movies
  🔍 Search for a movie
  ✅ Mark a movie as seen
  ➕ Add a movie
  🗑️  Delete a movie
  👋 Exit
```

**Features:**
- Use ↑↓ arrow keys to navigate
- Press Enter to select
- Type to filter options
- Ctrl+C to cancel anytime

### v1.0 Interface (menu.py)

```
=== Main MENU ===
1. Show all movies
2. Search for a movie
3. Mark a movie as seen
4. Add a movie
5. Delete a movie
6. Exit

Choose an option between 1 and 6:
```

---

## 📸 Screenshots

### Movie Collection Display
```
╭─────────────────────── 🎬 Movie Collection ───────────────────────╮
│ Title          │ Genre   │ Premiere │ Runtime  │ Language │ Watch │
├────────────────┼─────────┼──────────┼──────────┼──────────┼───────┤
│ Inception      │ Sci-Fi  │ 2010     │ 148 min  │ English  │ ✓ Yes │
│ The Matrix     │ Action  │ 1999     │ 136 min  │ English  │ ✗ No  │
╰───────────────────────────────────────────────────────────────────╯
```

### Statistics Dashboard
```
╭─────────── 📊 Collection Statistics ───────────╮
│ Total Movies: 42                               │
│ ✓ Seen: 28 (66.7%)                            │
│ ✗ Unseen: 14 (33.3%)                          │
╰────────────────────────────────────────────────╯
```

---

## ✅ Commit Guidelines

This project follows **Conventional Commits**:

* `feat:` for new features
* `fix:` for bug fixes
* `docs:` for documentation updates
* `refactor:` for code improvements
* `style:` for formatting changes
* `test:` for adding tests

**Examples:**
```bash
git commit -m "feat: add interactive menu with inquirer"
git commit -m "fix: resolve CSV encoding issue"
git commit -m "docs: update README with v2.0 features"
```

---

## 🗺️ Roadmap

### v2.0.0 ✅ (Current)
- [x] Interactive UI with inquirer
- [x] Rich terminal styling
- [x] Statistics dashboard
- [x] Filter by watch status

### v2.1.0 (Planned)
- [ ] Advanced search engine with autocomplete
- [ ] Multi-criteria filtering (genre, year, language)
- [ ] Search with preview

### v3.0.0 (Future)
- [ ] Unit tests with pytest
- [ ] SQLite database integration
- [ ] Export to JSON/Excel
- [ ] Web interface (Flask)
- [ ] Movie ratings and reviews

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes using conventional commits
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Adoudi Mondher**
- GitHub: [@adoudi-mondher](https://github.com/adoudi-mondher)

---

## 📝 Changelog

### v2.0.0 (2024-XX-XX)
- **BREAKING CHANGE**: New UI requires `inquirer` and `rich` packages
- Added interactive menu with arrow key navigation
- Added rich terminal styling and colors
- Added statistics dashboard
- Added filter movies by watch status
- Improved error handling and user feedback
- Kept v1.0 interface for backward compatibility

### v1.0.0 (Initial Release)
- Basic menu-driven interface
- CRUD operations for movies
- CSV file storage
- Search functionality

---

## 🙏 Acknowledgments

- [inquirer](https://github.com/magmax/python-inquirer) - Interactive CLI prompts
- [rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- [tabulate](https://github.com/astanin/python-tabulate) - Table display

---

**⭐ If you find this project useful, please give it a star!**
