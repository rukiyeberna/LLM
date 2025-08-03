#  Handwritten Digit Recognition

A beginner-friendly deep learning project using **TensorFlow** and the **MNIST** dataset to recognize handwritten digits (0-9). Includes an interactive **Gradio** interface to draw digits and see real-time predictions with confidence scores.

---

##  Features

-  MNIST dataset  
-  Draw digits in browser using Gradio  
-  Real-time predictions with confidence level  
-  Modular structure for training, testing, and inference  
-  Model is saved and loaded using `.h5` format  
---

##  Demo

<p align="center">

  <img width="1200" height="600" alt="Screenshot from 2025-08-03 14-13-25" src="https://github.com/user-attachments/assets/9eb1f1d5-8e74-4ecd-9ea4-2dc209a32b27" />

  
</p>


---

##  Project Structure

```
handwritten-digit-recognition/
├── explore_mnist.py                    # MNIST dataset exploration
├── mnist_model_train.ipynb            # Model training notebook
├── model_test.py                      # Model testing script
├── mnist_gradio_digit_classifier.ipynb # Gradio interface for prediction
├── LICENSE
└── README.md
```

---

##  Installation

1. **Clone the repository:**

```bash
git clone https://github.com/rukiyeberna/handwritten-digit-recognition.git
cd handwritten-digit-recognition
```

2. **Install dependencies:**

```bash
pip install tensorflow gradio numpy matplotlib
```

---

##  Train the Model

If you'd like to train the model yourself, open the notebook:

```bash
jupyter notebook mnist_model_train.ipynb
```

After training, the model is saved as:

```python
model.save("mnist_model.h5")
```

This `.h5` file includes:
- Model architecture
- Trained weights
- Optimizer state
- Training configuration


---

##  Run the Gradio App

Launch the web interface to draw digits:

```bash
jupyter notebook mnist_gradio_digit_classifier.ipynb
```

Then click the Gradio link to open the digit prediction UI in your browser.

---

##  Sample Output

> **Prediction**: `6`  
> **Confidence**: `80.1%`



---

##  License

This project is licensed under the [MIT License](./LICENSE).

---

##  Author

Developed by [rukiyeberna](https://github.com/rukiyeberna)
