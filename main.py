import argparse
import hashlib
from collections import defaultdict
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    p = argparse.ArgumentParser(description='Liste les fichiers au contenu identique.')
    p.add_argument('folder', type=Path)
    args = p.parse_args()
    if not args.folder.is_dir():
        p.error('Le dossier est introuvable.')
    sizes = defaultdict(list)
    for path in args.folder.rglob('*'):
        if path.is_file() and not path.is_symlink():
            try:
                sizes[path.stat().st_size].append(path)
            except OSError as exc:
                print(f'Ignoré : {path} ({exc})')
    found = 0
    for size, paths in sorted(sizes.items()):
        if len(paths) < 2:
            continue
        groups = defaultdict(list)
        for path in paths:
            try:
                groups[digest(path)].append(path)
            except OSError as exc:
                print(f'Ignoré : {path} ({exc})')
        for matches in groups.values():
            if len(matches) > 1:
                found += 1
                print(f'\nGroupe {found} ({size} octets) :')
                for path in matches:
                    print(f'  {path}')
    if not found:
        print('Aucun doublon trouvé.')


if __name__ == '__main__':
    main()
