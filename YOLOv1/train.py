import numpy as np

class YoloV1:
    def __init__(self):
        pass

    def relu(self,a):
        return np.maximum(0,a)

    def conv2D(self,input,filters,bias=None,stride=1,padding=0):
        C_in,H,W = input.shape
        C_out, _, KH, KW = filters.shape

        if padding > 0:
            input = np.pad(input, ((0,0),(padding,padding),(padding,padding)),mode ="constant")

        H_out = (H + 2*padding - KH) // stride + 1
        W_out = (W + 2*padding - KW) // stride + 1

        output = np.zeros((C_out,H_out,W_out))

        for c_out in range(C_out):
            for h in range(H_out):
                for w in range(W_out):
                    h_start = h*stride
                    w_start = w*stride
                    region = input[:,h_start:h_start+KH,w_start:w_start+KW]
                    output[c_out,h,w] = np.sum(region * filters[c_out]) + (bias[c_out] if bias is not None else 0)
        
        return output
    
    def residual_block(self,input,w1,b1,w2,b2,stride = 1,padding = 1):
        h1 = self.conv2D(input,w1,b1,stride=stride,padding=padding)
        h2 = self.relu(h1)
        h3 = self.conv2D(h2,w2,b2,stride=stride,padding=padding)
        if input.shape != h3.shape:
            raise ValueError("input and output shapes do not match for skip connection!")
        
        y = self.relu(h3+input)
        return y

    def flatten(self,x):
        xflat = x.reshape(-1)
        return xflat
    
    def dense(self,x,w,b):
        return self.relu(np.dot(w,x)+b)



    # 3 kanallı 32x32 görüntü
x = np.random.randn(3, 32, 32)
w1 = np.random.randn(3, 3, 3, 3)
b1 = np.random.randn(3)
w2 = np.random.randn(3, 3, 3, 3)
b2 = np.random.randn(3)

model = YoloV1()
out = model.residual_block(x, w1, b1, w2, b2)
print(out.shape)  # Beklenen: (3, 32, 32)

x = np.random.randn(3,4,4)
w = np.random.randn(10,48)
b = np.random.randn(10)
out = model.dense(model.flatten(x),w,b)

print(out)