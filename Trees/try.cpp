#include <bits/stdc++.h>
using namespace std;

int minDeliveryTime(int n, const vector<int>& orderCityList) {
    if (orderCityList.empty()) return 0;

    unordered_map<int, int> freq;
    for (int city : orderCityList) {
        freq[city]++;
    }

    int totalOrders = orderCityList.size();
    int maxFreq = 0;
    for (auto& [_, f] : freq) {
        maxFreq = max(maxFreq, f);
    }

    int low = 1;
    int high = max(2 * maxFreq, totalOrders);
    int ans = high;

    auto canFinish = [&](int days) {
        long long extra = 0, spare = 0;
        for (auto& [_, f] : freq) {
            if (f > days) {
                extra += f - days;
            } else {
                spare += (days - f) / 2;
            }
        }
        return spare >= extra;
    };

    while (low <= high) {
        int mid = (low + high) / 2;
        if (canFinish(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    return ans;
}
