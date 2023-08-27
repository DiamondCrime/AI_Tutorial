import math

# Sigmoid Activation Function
sigmoid = lambda x: 1 / (1 + math.exp(-x)) if x >= 0 else math.exp(x) / (1 + math.exp(x))

# Hyperbolic Tangent (Tanh) Activation Function
tanh = lambda x: math.tanh(x) if x < 20 else 1.0 if x >= 20 else -1.0

# Rectified Linear Unit (ReLU) Activation Function
relu = lambda x: x if x >= 0 else 0

# Leaky Rectified Linear Unit (Leaky ReLU) Activation Function
leaky_relu = lambda x, alpha: x if x >= 0 else alpha * x

# Exponential Linear Unit (ELU) Activation Function
elu = lambda x, alpha: x if x >= 0 else alpha * (math.exp(x) - 1)

# Softplus Activation Function
softplus = lambda x: math.log(1 + math.exp(x))

# Swish Activation Function
swish = lambda x: x * sigmoid(x)

# Parametric Rectified Linear Unit (PReLU) Activation Function
prelu = lambda x, alpha: x if x >= 0 else alpha * x

# Gaussian Activation Function
gaussian = lambda x: math.exp(-x**2)

# ArcTan Activation Function
arctan = lambda x: math.atan(x)

# Bent Identity Activation Function
bent_identity = lambda x: (math.sqrt(x**2 + 1) - 1) / 2 + x

# Softsign Activation Function
softsign = lambda x: x / (1 + abs(x))

# Rectified Linear Unit 6 (ReLU6) Activation Function
relu6 = lambda x: 0 if x < 0 else 6 if x > 6 else x
