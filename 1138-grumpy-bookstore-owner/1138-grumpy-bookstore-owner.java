import static java.lang.Math.max;
import static java.util.Arrays.stream;

public class Solution {
    public int maxSatisfied(int[] C, int[] G, int k) {
        int x = 0;

        for (int i = 0; i < C.length; i++)
            if (G[i] == 0) {
                x += C[i];
                C[i] = 0;
            }

        int y;

        for (int i = k, wSum = y = sum(C, k); i < C.length; i++) {
            wSum += C[i] - C[i - k];
            y = max(y, wSum);
        }

        return x + y;
    }

    private static int sum(int[] A, int k) {
        return stream(A).limit(k).sum();
    }
}