# Secure Water Billing System using Homomorphic Encryption

## Overview
This project addresses traditional challenges in water resource management, particularly data integrity and privacy, by employing Homomorphic Encryption (HE) to maintain data confidentiality throughout its lifecycle. By utilizing the CKKS scheme implemented via the TenSEAL library, the system ensures secure handling and analysis of water bill data while allowing encrypted computations without decryption.

### Key Features:
- **Homomorphic Encryption (HE):** Implements the CKKS scheme through the TenSEAL library to securely process water billing data.
- **Data Confidentiality:** Ensures that sensitive information remains encrypted throughout computations.
- **Scalability & Dependability:** Comparative analysis demonstrates that the system outperforms existing methods in terms of security and efficiency.
- **Future Research Opportunities:** Opens avenues for further exploration of Fully Homomorphic Encryption (FHE) in environmental monitoring and secure data analytics.

## Execution Steps
Follow these steps to run the project:

1. **Generate the dataset:** Run the `dataset_generation.py` file to create synthetic water billing data.
   ```bash
   python dataset_generation.py
   ```
2. **Save the dataset:** The generated dataset will be stored in the same directory where the script is executed.
3. **Perform Homomorphic Calculations:** Use `main.py` to load the dataset, perform encrypted computations, and print the output.
   ```bash
   python main.py
   ```

## Dependencies
Ensure you have the following dependencies installed before executing the project:

```bash
pip install tenseal numpy pandas
```

## Future Scope
The innovative approach taken in this project creates opportunities for further research into Fully Homomorphic Encryption (FHE) in environmental monitoring, allowing secure computations on real-time sensor data while preserving privacy.

## License
This project is released under the MIT License.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request to enhance the functionality or security of the project.

