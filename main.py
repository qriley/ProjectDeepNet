class NeuralNetwork:
    def _init_(self, input1, input2):
        self.input = input1
        self.weightA = np.random.rand(self.input.shape[1],4) 
        self.weightB = np.random.rand(4,1)
        self.y = input2
        self.out = np.zeros(y.shape)
        
    def forward (self):
        self.hiddenLayor1 = sigmoid(np.dot(self.input, self.weights1))
        self.out = sigmoid(np.dot(self.layer1, self.weights2))
        
    def back (self):
        #calculus stuff to detetmine derivative using chain rule to update weights using the slope of the loss#
        d_weightsB = np.dot(self.hiddenLayer1.T, (2*(self.y - self.out) * sigmoid_derivative(self.out)))
        d_weightsA = np.dot(self.input.T,  (np.dot(2*(self.y - self.out) * sigmoid_derivative(self.output), self.weightB.T) * sigmoid_derivative(self.hiddenLayer1)))
        
        self.weightA += d_weightA
        self.weightB += d_weightB