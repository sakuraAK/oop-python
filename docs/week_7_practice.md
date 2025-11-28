# 📘 **Week 7 — Collections of Objects & File I/O**

---

## **Overview**

Topics covered this week:

- Managing collections of objects (lists, dictionaries)
- Aggregation and association
- JSON serialization (save) and deserialization (load)
- Basic file I/O (read/write/append)

---

## **📌 Exercise 1 — Managing Many Objects in a List**

**Domain:** Library / Books

Create a `Book` class with attributes:

- `title`
- `author`
- `year`

Tasks:

1. Create at least **five Book objects**.
2. Store them in a **list**.
3. Write functions to:

   - print all books
   - filter books by author
   - find the oldest book

---

## **📌 Exercise 2 — Managing Objects in a Dictionary**

**Domain:** Employee Directory

Create an `Employee` class:

- `id`
- `name`
- `department`

Tasks:

1. Create several employees.
2. Store them in a dictionary keyed by `id`.
3. Implement functions to:

   - add an employee
   - remove an employee
   - find an employee by ID
   - list employees grouped by department

---

## **📌 Exercise 3 — Aggregation Example**

**Domain:** University Courses

Classes:

- `Student(name, major)`
- `Course(name)` → holds a list of `Student` objects

Tasks:

1. Add/remove students from a course.
2. Print all enrolled students.
3. Count how many students per major are enrolled.

---

## **📌 Exercise 4 — Association Example**

**Domain:** Doctor Appointment System

Classes:

- `Doctor(name, specialty)`
- `Patient(name)`
- `Appointment(doctor, patient, date)`

Tasks:

1. Create several doctors and patients.
2. Create appointment objects that **associate** doctors with patients.
3. Store appointments in a list.
4. Implement:

   - list appointments for a doctor
   - list appointments for a patient

---

## **📌 Exercise 5 — Saving Objects to JSON**

**Domain:** Task Manager

Create a `Task` class with:

- `title`
- `completed` (True/False)

Tasks:

1. Store Task objects in a list.
2. Convert them to dictionaries.
3. Save to `tasks.json`.
4. Load the file and reconstruct Task objects.

---

## **📌 Exercise 6 — JSON + Computation**

**Domain:** Product Inventory

Given JSON:

```json
[
  { "name": "Laptop", "price": 1200, "qty": 5 },
  { "name": "Mouse", "price": 25, "qty": 40 },
  { "name": "Monitor", "price": 300, "qty": 8 }
]
```

Tasks:

1. Load JSON from file.
2. Create a `Product` class.
3. Build a list of Product objects.
4. Compute:

   - total inventory value
   - most expensive product
   - product with the highest quantity

---

## **📌 Exercise 7 — Aggregation + JSON**

**Domain:** School Report Cards

Classes:

- `Student(name)`
- `Course(name)`
- `ReportCard(student, grades_dict)`

Example JSON:

```json
{
  "student": "Alice",
  "grades": { "Math": 89, "Physics": 92 }
}
```

Tasks:

1. Store courses → grade in a dictionary.
2. Save the entire ReportCard as JSON.
3. Load JSON and rebuild the object.

---

## **📌 Exercise 8 — File I/O: Logging**

**Domain:** Simple Text Logging System

Tasks:

1. Write a function `log(message)` that appends a timestamped entry to `log.txt`.
2. Write a function to read the **last N lines** of the log.
3. Write a function to **clear the log** (after confirmation).

---

## **📌 Exercise 9 — Association (Multiple Objects)**

**Domain:** Car Rental System

Classes:

- `Car(plate, brand)`
- `Customer(name)`
- `Rental(car, customer, days)`

Tasks:

1. Store rentals in a list.
2. Implement:

   - all cars rented by customer X
   - all customers who rented a given brand
   - total rental days for a given car

---

## **📌 Exercise 10 — Combined Scenario**

**Domain:** Contact Manager With Persistence

Create:

- `Contact(name, phone)`
- a list of contacts

Tasks:

1. Save all contacts to a JSON file.
2. Load them back into Contact objects.
3. Search by name or phone.
4. Delete a contact.
5. Export all contacts to a plain text file: `contacts.txt`.
