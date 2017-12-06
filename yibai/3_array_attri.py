import numpy as np

if __name__=='__main__':

    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(a.shape)
    a.shape = (3, 2)
    print(a)

    b = a.reshape(3,2)
    print(b)

    a1 = np.arange(24)
    print(a1.ndim)
    # 现在调整其大小
    b1 = a1.reshape(2, 4, 3)
    print(b1.flags)

    x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
    print(x.itemsize)
    print(a.flags)

    data = [[1,2],[3,4],[5,6]]
    y = np.array(data,order="F")
    z = y
    y[0][0] = 0
    print(y)
    y.resize((1,6))
    print(z)
    print(y.flags)