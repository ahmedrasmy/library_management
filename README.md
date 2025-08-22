Odoo Library Management Module

This repository contains a custom Odoo module for managing a simple **Library System**.  
The module is fully functional upon installation and provides book and rental management with security access controls.

---

## Module Structure
```
library_management/
│── models/
    |   __init__.py
│   ├── library_author.py  # Author model
    |   library_book.py    # Book model
│   └── library_rental.py  # Rental model
│── security/
│   ├── ir.model.access.csv
│   └── security.xml
│── views/
│   ├── base_menu.xml     
│   └── library_author_view.xml   # Author form & tree views
│   └── library_book_view.xml     # Book form & tree views
│   └── library_rental_view.xml   # Rental form & tree views
│── __init__.py
│── __manifest__.py
```

---

##  Installation Guide
1. **Clone the repository** into your Odoo `addons` directory:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/ahmedrasmy/library_management.git
   ```

2. **Restart Odoo server** and update the module list:
   ```bash
   ./odoo-bin -u library_management -d <your_database_name>
   ```

3. **Activate the module**:
   - Go to **Apps** in Odoo.
   - Search for **Library Management**.
   - Click **Install**.

---

##  Functionalities
- **Book Management**
  - Track books (title, author, category, etc.).
  - Computed field `is_available` indicates availability.
  - Smart button to view active rentals of a book.

- **Rental Management**
  - Rent and return books with state transitions.
  - Prevents renting a book that is already rented and not yet returned.

- **Security**
  - Security group **Librarian** with full access.
  - Access control rules defined in `ir.model.access.csv`.

---

## Security
- **Librarian Group**: Full Create, Read, Update, Delete access on all models.
- Record rules can be extended (e.g., restrict users to only see their own rentals).

---

## Testing the Module
1. Create a new **Book** from the **Library → Books** menu.
2. Create a **Rental** for that book.
3. Try creating another rental for the same book (it will be blocked if the book is still rented).
4. Return the book → availability updates automatically.

---

##  License
This module is provided under the MIT License.

---

 Developed by **Ahmed Rasmy**
