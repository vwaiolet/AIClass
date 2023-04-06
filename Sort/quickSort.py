def quick_sort(a, p: int, r: int):
    if p < r:
        q = partition(a, p, r)  # 분할
        quick_sort(a, p, q - 1)  # 왼쪽 부분 리스트 정렬
        quick_sort(a, q + 1, r)  # 오른쪽 부분 리스트 정렬


def partition(a, p: int, r: int) -> int:
    x = a[r]  # x: 기준 원소
    i = p - 1  # i: 1구역의 끝 지점
    for j in range(p, r):  # j: 3구역의 시작 지점
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]  # 교환
    a[i + 1], a[r] = a[r], a[i + 1]  # 기준 원소와 2구역 첫 원소 교환
    return i + 1


arr = [3, 8, 2, 4, 8, 77, 1, 2, 0, 5, 56, 28]
quick_sort(arr, 0, len(arr)-1)
print(arr)
