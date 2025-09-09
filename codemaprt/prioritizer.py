def score(meta, w=None):
    if w is None: w={'criticality':0.4,'impact':0.3,'flakiness':0.2,'complexity':0.1}
    c={'high':5,'medium':3,'low':1}.get(meta.get('criticality','low'),1)
    i=5; f=int(meta.get('historical_failures',0)); x=3
    return (w['criticality']*c + w['impact']*i + w['flakiness']*f + w['complexity']*x)/2.0
def prioritize(tests_map):
    rows=[(tid, round(score(meta),2),
           f"components: {', '.join(meta.get('components',[]) or ['—'])}; criticality: {meta.get('criticality','low')}; history: {int(meta.get('historical_failures',0))}")
          for tid,meta in tests_map.items()]
    rows.sort(key=lambda r:r[1], reverse=True); return rows
