# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: SupplyList
import timeit, sys

def perf_report(items, suppliers, orders):
    t0 = time.perf_counter()
    for o in orders:
        for s in suppliers:
            if s['name'] in o['suppliers']:
                o['total'] = o.get('total', 0) + s['price'] * o['qty']
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    for o in orders:
        if o['qty'] <= o.get('stock', 0):
            o['status'] = 'OK'
    t3 = time.perf_counter()
    t4 = time.perf_counter()
    for o in orders:
        for s in suppliers:
            if s['name'] in o['suppliers']:
                s['orders'] = s.get('orders', 0) + 1
    t5 = time.perf_counter()
    print('SupplyList perf report')
    print('  total cost calc: %.4f s (%d x %d pairs)' % (t1 - t0, len(orders), len(suppliers)))
    print('  stock check    : %.4f s' % (t3 - t2))
    print('  supplier count  : %.4f s' % (t5 - t4))
    print('  sys: %s' % sys.version.split()[0])

if __name__ == '__main__':
    perf_report(
        items=[('wrench', 10, ['Acme', 'Global']) for _ in range(1000)],
        suppliers=[{'name': 'Acme', 'price': 12.5, 'orders': 0},
                   {'name': 'Global', 'price': 9.9, 'orders': 0}],
        orders=[{'qty': 5, 'stock': 2, 'suppliers': ['Acme'], 'total': 0} for _ in range(1000)],
    )
