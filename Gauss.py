class Gauss:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def GaussMethod(self):
        n = len(self.A)
        M = self.A.copy()
        V = self.B.copy()
        for i in range(n):
            max_row = i
            for j in range(i + 1, n):
                if abs(M[j][i]) > abs(M[max_row][i]):
                    max_row = j
            M[i], M[max_row] = M[max_row], M[i]
            V[i], V[max_row] = V[max_row], V[i]

            if M[i][i] == 0:
                return None

            for j in range(i + 1, n):
                ratio = M[j][i] / M[i][i]
                V[j] -= ratio * V[i]
                for k in range(i, n):
                    M[j][k] -= ratio * M[i][k]
        X = [0]*n
        for i in range(n - 1, -1, -1):
            X[i] = V[i]
            for j in range(i + 1, n):
                X[i] -= M[i][j] * X[j]
            X[i] /= M[i][i]
        return X