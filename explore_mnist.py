from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(y_train[:10]) 

#60.000 tane 28x28 piksellik grayscale görüntü var.
print(x_train.shape) # (60000, 28, 28)

#görselleştir
plt.imshow(x_train[0], cmap="gray")
plt.title(f"Label: {y_train[0]}")
plt.show()

#prepocessing data

# görüntüdeki pixel degerlerini 0-1 arasina indirelim
x_train, x_test = x_train / 255.0, x_test / 255.0