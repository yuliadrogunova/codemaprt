import argparse
from .change_detector import read_changed_files
from .mapper import load_components_map, load_tests_map, map_files_to_components, tests_for_components
from .prioritizer import prioritize
# SAFETY_NET_PATCH
def select_safety_net(tests_map, impacted_keys, k=5):
    pool = []
    for tid, meta in tests_map.items():
        if tid in impacted_keys:
            continue
        comps = meta.get('components', []) or []
        crit = meta.get('criticality', 'low')
        prio = 3 if not comps else (2 if crit == 'low' else 1)
        pool.append((prio, tid, meta))
    # sort by priority (safety with empty comps first)
    pool.sort(key=lambda x: x[0], reverse=True)
    chosen = [(tid, meta) for _, tid, meta in pool[:k]]
    return dict((tid, meta) for tid, meta in chosen)

from .reporter import write_report
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--changed-files', default='.codemaprt/changed_files.txt')
    ap.add_argument('--components-map', default='.codemaprt/components_map.yaml')
    ap.add_argument('--tests-map', default='.codemaprt/tests_map.yaml')
    ap.add_argument('--report', default='reports/index.html')
    a=ap.parse_args()
    changed=read_changed_files(a.changed_files)
    comp_map=load_components_map(a.components_map)
    comps=map_files_to_components(changed, comp_map)
    tests_map=load_tests_map(a.tests_map)
    impacted=tests_for_components(tests_map, comps)
    # add safety-net tests
    safety = select_safety_net(tests_map, set(impacted.keys()), k=5)
    combined = {**impacted, **safety}
    rows=prioritize(combined)
    write_report(changed, rows, a.report)
    print(f"[CodeMapRT] Selected {len(rows)} tests (impacted={len(impacted)}, safety={len(safety)}). Report: {a.report}")
if __name__=='__main__': main()
