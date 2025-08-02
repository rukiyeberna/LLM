from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist


model = load_model("mnist_model.h5")


(_, _), (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0


def rastgele_tahmin_yap(model, x_test, y_test):
    i = np.random.randint(0, len(x_test)) 
    tahmin = model.predict(x_test[i].reshape(1, 28, 28)).argmax()

    plt.imshow(x_test[i], cmap="gray")
    plt.title(f"Gerçek: {y_test[i]} | Tahmin: {tahmin}")
    plt.axis("off")
    plt.show()

    if tahmin == y_test[i]:
        print("Doğru tahmin!")
    else:
        print(" Yanlış tahmin!")

for _ in range(5):
    rastgele_tahmin_yap(model, x_test, y_test)
