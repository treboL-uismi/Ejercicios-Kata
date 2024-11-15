def merge(*dicts):
    merged = {}

    for dict in dicts:
      for key, value in dict.items():
        if key not in merged:
          merged[key] = [value]
        else:
          merged[key].append(value)
    return merged

print(merge({'A': 2, 'B': 3}, {'E': 5, 'A': 2}))