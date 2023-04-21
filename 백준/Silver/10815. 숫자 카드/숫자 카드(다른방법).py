import sys

# 이진탐색 함수 정의
def binary_search(cards, target):
    left, right = 0, len(cards) - 1  # 시작은 cards 리스트의 처음과 끝 인덱스
    while left <= right:  # 시작 인덱스가 끝 인덱스보다 작거나 같을 때까지
        mid = (left + right) // 2  # 중간 인덱스 찾기
        if cards[mid] == target:  # 중간 값과 찾고자 하는 값이 같으면
            return 1  # 1 반환
        elif cards[mid] > target:  # 중간 값이 찾고자 하는 값보다 크면
            right = mid - 1  # 오른쪽 범위를 중간 값 - 1로 바꿔서 다시 탐색
        else:  # 중간 값이 찾고자 하는 값보다 작으면
            left = mid + 1  # 왼쪽 범위를 중간 값 + 1로 바꿔서 다시 탐색
    return 0  # 리스트에 찾고자 하는 값이 없으면 0 반환

N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))  # 정렬된 카드 리스트 생성
M = int(sys.stdin.readline())
ch_cards = list(map(int, sys.stdin.readline().split()))

# 각각의 확인 카드마다 이진탐색으로 탐색하여 결과 출력
for i in ch_cards :
    print(binary_search(cards, i), end = ' ')
