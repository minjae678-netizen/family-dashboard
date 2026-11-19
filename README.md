# 우리 가족 오늘 보드

날씨, 세부 가족 여행 D-day, 이번 주 가족 일정, 오늘의 할 일·저녁, 가족 메모를 한 화면에 모은 가족 대시보드입니다.
정적 HTML 한 장으로 동작하고, 적어 둔 내용은 그 브라우저의 `localStorage`(`familyBoard.v2`)에만 저장됩니다. 서버로 아무것도 보내지 않습니다.

- 주소: https://minjae678-netizen.github.io/family-dashboard/
- 휴대폰 Chrome에서 주소를 연 뒤 메뉴 → **홈 화면에 추가**를 누르면 앱처럼 전체 화면으로 열립니다.
- 날씨는 Open-Meteo(무료, 키 없음)에서 실시간으로 가져오고, 지역은 화면의 `📍 용인시 처인구`를 눌러 바꿀 수 있습니다.

## 파일

| 파일 | 설명 |
| --- | --- |
| `index.html` | 대시보드 본체 (기능·저장 방식 그대로) |
| `manifest.webmanifest` | 홈 화면 추가용 앱 정보 (이름, 아이콘, 테마색) |
| `icon-192.png` / `icon-512.png` / `icon-maskable-512.png` / `icon-180.png` | 앱 아이콘 |
| `icon.svg`, `favicon.svg` | 벡터 아이콘 · 파비콘 |
| `sw.js` | 마지막 화면을 오프라인에서도 열어 주는 최소 서비스 워커 |
| `tools/make_icons.py` | 아이콘 PNG를 다시 만들 때 쓰는 스크립트 |

## 수정하기

`index.html`을 고친 뒤 같은 저장소에 커밋·푸시하면 1분 안에 주소에 반영됩니다.
