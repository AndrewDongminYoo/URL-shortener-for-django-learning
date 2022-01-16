## 프로젝트 아이템 선정 이유

- 이미 쟁쟁하고 유명한 업체가 많은 만큼, 수요가 있다.
  - Bitly for the best all-round URL shortener
  - Rebrandly for creating branded links
  - TinyURL for fast and anonymous short URLs
  - BL.INK for small business owners
  - URL Shortener by Zapier for automatically creating short links
  - Shorby for Instagram users
  - Short.io for sending different visitors different links
  - Sniply for adding a CTA to the links you share
- 요금 정책의 기준선이 비교적 정교해 비즈니스 로직으로 적합하다.
- 일반적인 게시판 프로젝트에 비해 마이너한 테크닉 습득이 가능하다.
- 단순하게 연결된 실제 주소로 리다이렉팅하는 것 뿐만 아니라, 실제 트래픽을 감지해 통계 쿼리를 작성해 볼 수 있다.
- 클라이언트 (사용자)의 정보를 취득하고 취합하는 과정을 체험해 볼 수 있다.

## 요금 정책

- 기본 (Basic Plan)
  - User 당 Shortened Url 50개 생성 가능
  - 60 day expiring (연장 가능)
  - 로그인 인증 절차 (이메일 인증) 후에 사용 가능
  - 1초에 같은 IP 에서 5회 이상 호출 불가
  - 방문 통계 제공
  - 302 상태 코드 리턴 (일시적 리디렉션)
- 프로 (Advanced Plan)
  - User 당 무제한 Url 생성 가능
  - 직접 삭제할 때까지 삭제되지 않음
  - 이메일 인증 절차 후에 사용 가능
  - 같은 IP 에서 1초에 20회 이상 호출 불가
  - 더 발전된 방문 통계 (유입 통계) 제공
  - 301 상태 코드 리턴 (반영구적 리디렉션)

## 프로젝트 구성 및 구현 계획

- Front-end ( Vue.JS )
  - 메인 랜딩 페이지
  - 로그인 / 회원가입 페이지
  - 비밀번호 찾기 페이지
  - 이메일 인증 페이지
  - 통계 페이지
  - 회원 프로필 설정 페이지
  - 사업자의 경우 회사 설정 페이지
- Back-end ( Django )
  - 요금 정책 반영
  - DB 모델링
  - 뷰 렌더링 (서버사이드 렌더링)
  - REST API
  - Cache
  - Django ORM
- Etc.
  - telegram bot
  - static file
  - github actions CI/CD