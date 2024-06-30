import torch
from PIL import Image
from torchvision import transforms
from torchvision.transforms import functional as F

# Problem 1
# Load an image using PIL
image_path = 'path_to_your_image.jpg'  # Replace with your image path
image = Image.open(image_path)

# Convert the image to a PyTorch tensor
tensor_transform = transforms.ToTensor()
image_tensor = tensor_transform(image)

# Normalize the tensor
normalize_transform = transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
normalized_tensor = normalize_transform(image_tensor)

print("Image Tensor:\n", image_tensor)
print("\nNormalized Tensor:\n", normalized_tensor)

# Problem 2
# Custom transformation to rotate the image by 45 degrees
class RotateTransform:
    def _init_(self, angle):
        self.angle = angle

    def _call_(self, x):
        return F.rotate(x, self.angle)

# Compose the custom rotation transformation with a resize transformation
custom_transform = transforms.Compose([
    RotateTransform(45),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Apply the composed transformation to the image
transformed_image_tensor = custom_transform(image)

print("\nTransformed Image Tensor:\n", transformed_image_tensor)

# Problem 3
# Define the transformations
composed_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomCrop((100, 100)),
    transforms.Grayscale(),
    transforms.ToTensor()
])

# Apply the transformations to the image
transformed_image_tensor_multiple = composed_transform(image)

print("\nTransformed Image Tensor with Multiple Transformations:\n", transformed_image_tensor_multiple)