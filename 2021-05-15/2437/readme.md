# 저울
문제 링크: https://www.acmicpc.net/problem/2437

제출 날짜: 2021년 5월 15일

## 문제 설명
+ 주어진 무게 추로 측정할 수 없는 최소값 구하기

## 문제 풀이 (main.py)
+ 무게 추를 오름차순으로 정렬 후 차례대로 누적합을 구합니다.
+ 누적합 + 1보다 해당 무게추의 무게가 더 클 경우 측정할 수 없는 값이 됩니다.

## 시간 초과 문제 풀이 (main2.py)
+ 주어진 무게 추로 조합할 수 있는 모든 무게를 구한 후 없는 최소값을 구했습니다.
+ 시간 초과로 틀린 문제 풀이입니다.
