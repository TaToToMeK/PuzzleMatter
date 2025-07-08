# PuzzleMatter
A playground of algorithms and puzzle-solving adventures for fun and learning — exploring clever solutions to intriguing problems, from timeless classics to brain teasers


# First Puzzle ♞ ChessKnightTour

![ChessKnightTour image](images/ChessKnightTour.png)


This project implements an **object-oriented Python algorithm** for solving the **Knight’s Tour problem** on an `N x N` chessboard.

The algorithm explores the movement of a chess knight across the board, attempting to visit every square exactly once.

---

## 🔍 Goals & Experiments

The algorithm was used to answer the following questions:

- ❓ **Is it possible** for the knight to visit all squares on a `4x4` chessboard?
- 🔢 **How many valid tours** exist on a `5x5` and a `6x6` board?
- ♻️ **What is the smallest board size** that allows a **closed tour** — meaning the knight ends one full path and can move directly to the starting square?

---

## 🧩 What is the Knight's Tour?

The **Knight’s Tour** is a classic chess puzzle in which a knight must visit every square on a chessboard **exactly once**, following the legal L-shaped moves.

There are two types of tours:

- **Open Tour** – the knight ends on a different square than where it started.
- **Closed Tour** – the knight ends on a square that is one legal move away from the starting square, forming a cycle.

---

## 🛠️ Getting Started

To run the algorithm:

```bash
python ChessKnightTourClassBased.py
