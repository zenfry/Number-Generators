Here’s a short **README** for your PRNG project:  

---

## **Pseudo-Random Number Generators (PRNG) in Python**  

This project implements four different **pseudo-random number generators (PRNGs)** from scratch:  

1. **Middle Square Method**  
2. **Xorshift Algorithm**  
3. **Mersenne Twister (Simplified)**  
4. **Linear Congruential Generator (LCG)**  

Each PRNG is implemented in a separate file and can be tested using `main.py`.  

---

### **Project Structure**  
```
/prng_project
    ├── middle_square.py        # Middle Square PRNG
    ├── xorshift.py             # Xorshift PRNG
    ├── mersenne_twister.py     # Mersenne Twister PRNG
    ├── lcg.py                  # Linear Congruential Generator (LCG) PRNG
    ├── main.py                 # Runs all PRNGs
    ├── README.md               # Project Documentation
```

---

### **How to Run**  

1. **Clone the repository** (or create the files manually).  
2. Navigate to the project directory:  
   ```sh
   cd prng_project
   ```
3. Run the main script to test all PRNGs:  
   ```sh
   python main.py
   ```
4. You should see output from all four PRNGs.

---

### **Comparison of PRNGs**  

| PRNG | Strengths | Weaknesses |
|------|----------|------------|
| **Middle Square** | Simple, easy to implement | Short cycles, low randomness |
| **Xorshift** | Fast, good randomness | Not cryptographically secure |
| **Mersenne Twister** | High-quality randomness, long period (2^19937-1) | Slower, more complex |
| **LCG** | Simple, fast | Poor randomness with bad parameters |

---

### **Details of Each PRNG**  

#### **Middle Square Method**  
- Squares the current state and extracts the middle digits.  
- Very simple but prone to short cycles.  

#### **Xorshift Algorithm**  
- Uses bitwise XOR and shifts for fast random number generation.  
- More efficient than Middle Square and LCG.  

#### **Mersenne Twister**  
- High-quality PRNG with an extremely long period (2^19937-1).  
- Used in many applications but slower than Xorshift.  

#### **Linear Congruential Generator (LCG)**  
- Uses the formula: `X(n+1) = (aXn + c) % m`  
- Fast and simple, but quality depends on `a`, `c`, and `m` values.  

