def permutation(ss):
    if not ss:
        return
    if len(ss) == 1:
        return [ss]
    listing_ss = [_ for _ in ss]
    res = []

    # 从第n个数开始递归
    def permutation_core(listing_ss, n):
        if n > len(listing_ss)-1:
            return
        if n == len(listing_ss)-1:
            res.append(''.join(listing_ss))
            return
        for i in range(n, len(listing_ss)):
            if i != n and listing_ss[i] == listing_ss[n]:
                continue
            listing_ss[i], listing_ss[n] = listing_ss[n], listing_ss[i]
            permutation_core(listing_ss, n+1)
            listing_ss[i], listing_ss[n] = listing_ss[n], listing_ss[i]
    permutation_core(listing_ss, 0)
    return sorted(res)