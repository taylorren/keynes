import json, base64, os, sys
nb_path = os.path.join(os.getcwd(), 'code', 'temp_executed.ipynb')
if not os.path.exists(nb_path):
    print('nb not found:', nb_path)
    sys.exit(2)
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)
count = 0
out_files = []
for cell in nb.get('cells', []):
    for out in cell.get('outputs', []):
        data = out.get('data', {})
        img = data.get('image/png')
        if img:
            count += 1
            fn = os.path.join(os.getcwd(), 'code', f'plot{count}.png')
            with open(fn, 'wb') as g:
                g.write(base64.b64decode(img.encode('utf-8') if isinstance(img, str) else img))
            out_files.append(fn)
print(count)
for p in out_files:
    print(p)
