package practice.dp;

class Main {
    // given a array of items and its weight and the price. We have a bag in which
    // we can place these
    // items. The bag have a maximmum capacity and we have to maximise the profit.
    // wt : [10,5, 2,9]
    // val: [5, 20,1,80]
    // W : 20

    public int findMax(int[] wt, int[] val, int index, int maxCapacity) {
        if (maxCapacity < 0 || index == wt.length) {
            return 0;
        }
        System.out.println("max cap--->" + maxCapacity);
        System.out.println();
        if (wt[index] > maxCapacity) {
            return findMax(wt, val, index + 1, maxCapacity);
        } else {
            return Math.max(val[index] + findMax(wt, val, index + 1, maxCapacity - wt[index]),
                    findMax(wt, val, index + 1, maxCapacity));
        }

    }

    public int findMaxAlt(int[] wt, int[] val, int maxCapacity, int position) {
        System.out.println("max cap--->" + maxCapacity);

        if (maxCapacity <= 0 || position == 0) {
            return 0;
        }

        if (wt[position - 1] > maxCapacity) {
            return findMaxAlt(wt, val, maxCapacity, position - 1);
        } else {
            return Math.max(val[position - 1] + findMaxAlt(wt, val, maxCapacity - wt[position - 1], position - 1),
                    findMaxAlt(wt, val, maxCapacity, position - 1));
        }
    }

    public static void main(String[] args) {
        Main obj = new Main();
        int ans = obj.findMaxAlt(new int[] { 1, 3, 4 }, new int[] { 1, 4, 5 }, 7, 3);
        System.out.println(ans);
    }
}