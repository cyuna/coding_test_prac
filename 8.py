def print_baggage_items(*items, **items_with_count):
 print('# 단일 품목')
 for item in items:
 print(item)
 print('\n# 다중 품목')
 for item, count in items_with_count.items():
 print("{} {} 개".format(item, count))
print_baggage_items('laptop', 'camera', 'charger', socks=8, pants=2, shirts=4)
