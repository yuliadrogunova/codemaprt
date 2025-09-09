import fnmatch, yaml
from pathlib import Path
def load_components_map(path): return (yaml.safe_load(Path(path).read_text()) or {}).get('map',{})
def load_tests_map(path): return (yaml.safe_load(Path(path).read_text()) or {}).get('tests',{})
def map_files_to_components(files, comp_map):
    out=set()
    for f in files:
        for pat, comps in comp_map.items():
            if fnmatch.fnmatch(f, pat): out.update(comps or [])
    return out
def tests_for_components(tests_map, comps):
    return {tid:meta for tid,meta in tests_map.items() if set(meta.get('components',[])) & set(comps)}
