# 🎟️ BookMyShow Backend (Singleton Ticket Booking System)

This project is a **Python backend simulation** of a **movie ticket booking system** inspired by **BookMyShow**.  
It mainly demonstrates the **Singleton Design Pattern** in Python, ensuring that only one instance of each movie exists across multiple platforms (BookMyShow and PayTM).  

This helps in maintaining a **consistent ticket count** no matter where the booking happens.

---

##  Introduction
Imagine you are booking tickets for a movie. Whether you book from **BookMyShow** or **PayTM**, the number of available tickets should remain the same.  

This project simulates such a system using Python.  
The **Singleton Pattern** ensures that each movie has only **one instance shared across platforms**.  

---

##  Key Concepts
- **`__init__` Method** → Initializes available tickets for each movie.  
- **Singleton Pattern** → Ensures only one instance per movie class exists.  
- **`Booking()` Method** → Handles booking logic (input, ticket update).  
- **Platform Functions** → `Bmys()` and `payTM()` simulate different apps but share the same ticket data.  

---

## 🎬 Features
✔️ Supports **three movies** with different initial ticket counts:  
   - Movie1 → 150 tickets  
   - Movie2 → 250 tickets  
   - Movie3 → 200 tickets  

✔️ **Two booking platforms**:  
   - BookMyShow (`Bmys()`)  
   - PayTM (`payTM()`)  

✔️ **Singleton Pattern applied** → ticket counts are shared across platforms.  

✔️ **Real-time ticket updates** → booking reduces the count immediately.  

✔️ **Input validation** → prevents invalid ticket requests (e.g., 0 or more than available).  

✔️ **Reusable design** → easily extendable to add more movies or platforms.  

✔️ Demonstrates **core OOP principles** (encapsulation, constructors, methods).  

---

##  Tech Stack
- **Language:** Python 3.x  
- **Concepts Covered:**  
  - Singleton Design Pattern  
  - Object-Oriented Programming (`__init__`, classes, methods)  
  - Functions & Decorators  
  - Input Handling & Validations  

---

## 🏗️ Architecture Flow
