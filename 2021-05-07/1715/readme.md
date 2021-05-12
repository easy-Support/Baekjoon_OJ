# 카드 정렬하기
문제 링크: https://www.acmicpc.net/problem/1715

제출 날짜: 2021년 5월 7일

## 문제 주제
+ 카드 묶음을 섞는 최소값

## 문제 풀이
+ 우선순위 큐(힙)에 카드 묶음을 저장합니다.
+ 두번째 인덱스부터 끝까지 첫번째 값과 두번째 값을 더한 뒤 힙에 다시 넣고 그 값은 섞는 개수에 더합니다.