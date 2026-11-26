# 이영의 개인 포트폴리오
## GitHub Pages 배포
ZIP을 풀고 내부 파일과 폴더를 저장소 main 브랜치 루트에 올립니다. 숨김 폴더 `.github`도 반드시 포함합니다. Settings → Pages → Source → GitHub Actions 선택 후 Actions에서 Build gallery and deploy Pages를 실행합니다. 이후 main 브랜치에 커밋하면 자동으로 갤러리 목록을 생성하고 배포합니다. 생성된 gallery.json은 배포 산출물에 들어가며 저장소 원본에는 자동 커밋되지 않습니다.
## 사진 추가
images/teaching, projects, activities, training, archive 또는 새 하위 폴더에 사진을 업로드하고 Commit changes를 누릅니다. Actions 완료 후 배포 주소에서 확인합니다. 삭제도 동일합니다. 날짜는 2026-11-26-활동명.jpg처럼 파일명 앞에 붙이세요. 날짜 없는 사진은 뒤쪽에 표시됩니다. 최상위 하위 폴더 기준 분류합니다. profile 및 brand 폴더는 갤러리에서 제외됩니다. 개인정보와 비공개 교육자료는 업로드하지 마세요. 공개 저장소 및 배포 파일은 누구나 접근할 수 있습니다.
## 수정
프로필은 images/profile/lee.jpg, 로고는 images/brand/onna1.jpg, 캐릭터는 images/brand/onna2.png를 같은 파일명으로 교체합니다. 프로젝트 설명은 js/data.js, 브랜드 색은 css/style.css의 CSS 변수에서 수정합니다. 색은 첨부 로고 기반 추정값입니다. 실제 프로필은 첨부 일러스트를 그대로 사용합니다.
## 로컬 확인
python3 scripts/generate-gallery.py 실행 후 python3 -m http.server 8000 을 실행하고 http://localhost:8000 접속합니다. 파일을 더블클릭하면 갤러리 fetch가 차단될 수 있습니다.
