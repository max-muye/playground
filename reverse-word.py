# 对于属于的英文句子，翻转句子中的每一个单词
# e.g.
# a quick brown fox jump over a lazy dog
# a kciuq nworb xof pmuj revo a yzal god

arr = [x for x in "a kciuq nworb xof pmuj revo a yzal god"]

# 在这里完善你的算法，你应该直接对 arr 数组进行
arr.append(" ")
end = 0
start = 0

for i in arr:
    if i == " ":
        end = arr.index(i) - 1
        for j in range((end - start) // 2):
            arr[start + j], arr[end - j] = arr[end - j], arr[start + j]
        start = end + 2

print("".join(arr))
