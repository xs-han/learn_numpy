import numpy as np

if __name__=='__main__':
    x = [[1,2,3],[4,5,6]]
    a = np.asarray(x, dtype=float)
    x[0] = -1
    print(a.flags)

    y = [1,2,3]
    b = np.asarray(a)
    a[0][0] = 0
    print(b.flags)

    s = b'Hello World'
    a = np.frombuffer(s, dtype='S1')
    s.replace(b'o', b'0')
    print(s)
    print(a)

    list = range(5)
    it = iter(list)
    # 使用迭代器创建 ndarray
    x = np.fromiter(list, dtype=float)
    print(x)