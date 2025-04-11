## **Pseudo-Random Number Generators (PRNG) in Python**  

This project implements four different **pseudo-random number generators (PRNGs)** from scratch:  

1. **Middle Square Method**  
2. **Xorshift Algorithm**  
3. **Mersenne Twister (Simplified)**  
4. **Linear Congruential Generator (LCG)**  

Each PRNG is implemented in a separate file and can be tested using `main.py`.  


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


### **Comparison of PRNGs**  

| PRNG | Strengths | Weaknesses |
|------|----------|------------|
| **Middle Square** | Simple, easy to implement | Short cycles, low randomness |
| **Xorshift** | Fast, good randomness | Not cryptographically secure |
| **Mersenne Twister** | High-quality randomness, long period (2^19937-1) | Slower, more complex |
| **LCG** | Simple, fast | Poor randomness with bad parameters |


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

1. Middle Square Method
Birthday Spacings Test
Average Collisions: 164.33
Expected (Poisson λ): 2.00
The collision rate was significantly higher than expected. This suggests severe clustering and non-uniform spacing, indicative of poor randomness. The Middle Square method fails this test.
Runs Test
Observed Runs: 4800
Expected Runs: 6666.33
Z-score: -44.27
The number of runs was drastically lower than expected. A low run count implies overly predictable or patterned sequences. This confirms a lack of variation and fails the test.
Monobit Test
Ones: 500,318
Zeros: 499,682
Test Statistic: 0.64
The number of 1s and 0s was well-balanced, and the test statistic was within acceptable limits. This test was passed, but given failures elsewhere, this does not compensate for overall poor performance.
Overall:  The Middle Square method exhibits fundamental flaws in randomness and fails two of the three tests. It is not suitable for any serious random number generation application.

2. Xorshift
Birthday Spacings Test
Average Collisions: 1.83
Expected (Poisson λ): 2.00
The result was close to the expected mean, indicating good uniformity in spacing. The test was passed successfully.
Runs Test
Observed Runs: 5037
Expected Runs: 6666.33
Z-score: -38.65
The generator failed this test with a significantly low number of runs. This may suggest the presence of hidden patterns or insufficient entropy between successive outputs.
Monobit Test
Ones: 499,946
Zeros: 500,054
Test Statistic: -0.11
A near-perfect balance of 1s and 0s. The result falls well within the passing range. This indicates the bit-level distribution is uniform.
Overall: Xorshift shows promising results on bit-level and spacing tests but fails the sequence-level runs test. This suggests adequate randomness for casual or performance-sensitive applications, but further evaluation is needed before using it in critical contexts.

3. Mersenne Twister
Birthday Spacings Test
Average Collisions: 2.23
Expected (Poisson λ): 2.00
The observed value aligns closely with the expected mean, indicating a strong degree of uniformity. This test was passed.
Runs Test
Observed Runs: 5038
Expected Runs: 6666.33
Z-score: -38.62
Despite its reputation for quality, the Mersenne Twister failed this runs test. The result suggests potential oversmoothing or regularity in its sequence transitions.
Monobit Test
Ones: 500,518
Zeros: 499,482
Test Statistic: 1.04
The distribution of bits was well-balanced. The test passed comfortably, confirming a strong bit-level uniformity.
Overall:  The Mersenne Twister performs well on two out of three tests and remains a widely trusted general-purpose PRNG. The run test failure warrants closer inspection but is likely influenced by test conditions rather than fundamental flaws.

4. Linear Congruential Generator (LCG)
Birthday Spacings Test
Average Collisions: 2.13
Expected (Poisson λ): 2.00
The result falls within a reasonable tolerance range, indicating a sufficiently uniform output. This test is passed.
Runs Test
Observed Runs: 5000
Expected Runs: 6666.33
Z-score: -39.52
The LCG failed the runs test, reflecting structured or repetitive behavior in its sequences—a known drawback of simple LCGs.
Monobit Test
Ones: 500,111
Zeros: 499,889
Test Statistic: 0.22
A very balanced bit distribution. This test was passed successfully.
Overall: The LCG shows acceptable uniformity and bit distribution but fails in sequence unpredictability. While suitable for non-critical tasks, its simplicity makes it vulnerable to pattern detection.


