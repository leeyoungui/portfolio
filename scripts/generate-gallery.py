from pathlib import Path
from urllib.parse import quote
import json,re
root=Path(__file__).resolve().parents[1]
labels={'teaching':'교육 현장','projects':'프로젝트','activities':'기관 활동','training':'연수·연구','archive':'아카이브'}
rows=[]
for p in (root/'images').rglob('*'):
 if not p.is_file() or p.suffix.lower() not in {'.jpg','.jpeg','.png','.webp','.gif','.avif'}: continue
 parts=p.relative_to(root/'images').parts
 if parts[0] in {'profile','brand'} or any(x.startswith('.') for x in parts): continue
 date=re.search(r'(?<!\d)(20\d{2})[-_]?(\d{2})?[-_]?(\d{2})?(?!\d)',p.stem)
 year=date.group(1) if date else ''
 sort=''.join(x or '00' for x in date.groups()) if date else ''
 category=labels.get(parts[0],parts[0]) if len(parts)>1 else '기타'
 rows.append(dict(path=quote(p.relative_to(root).as_posix(),safe='/'),title=re.sub(r'[_-]+',' ',p.stem),category=category,year=year,sort=sort))
rows.sort(key=lambda x:(x['sort'],x['path']),reverse=True)
(root/'gallery.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
