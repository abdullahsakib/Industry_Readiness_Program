
def set_contains(set, target):
    hash_value=calculate_hash(target)
    
    bucket_index=hash_value%set.total_buckets
    
    memory_slot=set.buckets[bucket_index]
    
    if target in memory_slot :
        return True
    else:
        return False