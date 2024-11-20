
# Analyzing Pre-Image Attacks on Step-Reduced MD5  

This repository is part of the **CS557 Term Project** titled **"Analyzing Pre-Image Attacks on Step-Reduced MD5"**, supervised by **Prof. Somnath Tripathy**. The project focuses on exploring preimage attacks on cryptographic hash functions, specifically step-reduced MD5, as inspired by Aumasson et al.'s foundational work.
([Aumasson et al. 2008](https://link.springer.com/chapter/10.1007/978-3-642-04159-4_8)).  

## Repository Contents  

The repository includes Python implementations of step-reduced MD5 variants and an attack algorithm:  

1. **`md5_32_step.py`**  
   - Implements the 32-step MD5 hash function.  

2. **`md5_45_step.py`**  
   - Implements the 45-step MD5 hash function.  

3. **`md5_47_step.py`**  
   - Implements the 47-step MD5 hash function.  

4. **`preimage_attack_32step.py`**  
   - Implements the preimage attack on the 32-step MD5 function based on the pseudocode in Aumasson et al.'s research.  
   - The attack can be extended to the other step-reduced MD5 variants.  

## Getting Started  

1. Clone this repository:  
   ```bash  
   git clone <repository_url>  
   cd <repository_folder>  
   ```  

2. Run individual files using Python:  
   ```bash  
   python md5_32_step.py  
   ```  

3. To test the preimage attack:  
   ```bash  
   python preimage_attack_32step.py  
   ```  


### Modifying the Message  

The message to be hashed in the step-reduced MD5 implementations can be modified by changing the `message` variable in the code to a string of your choice.  

For example:  

```python
if __name__ == '__main__':
    message = "hello"
    md5(message)
```  



### Purpose  

Our objectives for this project are as follows:  

1. To thoroughly understand Aumasson et al.'s research on pre-image attacks on step-reduced MD5.  
2. To address the lack of source code in the original paper by implementing step-reduced MD5 hashing functions and a generalized attack algorithm in Python.  

    Specifically, we have:  

    - Implemented the 32-step MD5 hash function in Python.  
    - Implemented the 45-step MD5 hash function in Python.  
    - Implemented the 47-step MD5 hash function in Python.  
    - Developed an attack on the 32-step MD5 function as described in the paper's pseudocode, which can be extended to the other step-reduced MD5 implementations; implemented in Python.  

3. To analyze the practicality of the theoretical attack in both classical and quantum computational settings.  


## Contributors:

Ponnada Sai Tulasi Kanishka (2101CS57)

Rishikant Chigrupaatii (2101CS66)



