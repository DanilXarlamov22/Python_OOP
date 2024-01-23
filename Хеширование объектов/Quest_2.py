def limited_hash(left, right, hash_function=hash):
    def compute_hash(obj):
        h = hash_function(obj)
        result = (h - left) % (right - left + 1) + left
        return result
    return compute_hash