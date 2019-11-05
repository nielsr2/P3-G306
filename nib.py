(x_train) = glob.glob("/PICTURES/Eyes/small" + "*.j*")
(x_test) = glob.glob("/PICTURES/Eyes/smalltest" + "*.j*")

mnist.load_data()


(x_train, _), (x_test, _) = mnist.load_data()
inputImages = glob.glob("/PICTURES/Eyes/small" + "*.j*")
inputImages2 = glob.glob("/PICTURES/Eyes/smalltest" + "*.j*")
#(x_train2, _), (x_test2, _) = inputImages

bah  =  x_train[0]
bah.reshape(28, 28)
print(bah)
plt.imshow(x_train[5])
plt.gray()
plt.show()
plt.imshow(x_test[5])
plt.gray()
plt.show()

print(x_train[0])
