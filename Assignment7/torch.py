import torch

# Create a 3x3 tensor with random values
tensor1 = torch.rand(3, 3)
print("Original Tensor:\n", tensor1)

# Add 10 to each element
tensor1 = tensor1 + 10
print("\nTensor after adding 10:\n", tensor1)

# Multiply each element by 2
tensor1 = tensor1 * 2
print("\nTensor after multiplying by 2:\n", tensor1)

# Calculate mean and standard deviation
mean = tensor1.mean()
std_dev = tensor1.std()
print("\nMean of the Tensor:", mean.item())
print("Standard Deviation of the Tensor:", std_dev.item())

# Problem 2: Element-wise addition and multiplication of two 3x3 tensors
tensor2 = torch.rand(3, 3)
tensor3 = torch.rand(3, 3)
sum_tensors = tensor2 + tensor3
product_tensors = tensor2 * tensor3
print("\nSum of Tensors:\n", sum_tensors)
print("\nProduct of Tensors:\n", product_tensors)

# Problem 3: Reshape tensor and extract sub-tensor
tensor4 = torch.arange(1, 17).reshape(4, 4)
print("\nOriginal 4x4 Tensor:\n", tensor4)
sub_tensor = tensor4[:2, -2:]
print("\nExtracted Sub-Tensor:\n", sub_tensor)


