# py_algorithm

# 백준 1316번 https://www.acmicpc.net/problem/1316

```py
num = int(input())
for i in range(num):
    word = input()
    for j in range(len(word)-1):
        if word[j]!=word[j+1]:
            if word[j] in word[j+1:]:
                num -=1
                break
print(num)
```

입력받은 단어를 비교한다

첫글자와 그다음 글자가 같으면 아무 수행을 하지않고

첫글자와 그다음 글자가 다르면

첫글자가 그다음글자를 포함해서 그뒤에 포함이 되는지 검사한다

만약 있으면 처음에 입력 받았던 숫자에서 1을 뺀다

주의할점은 4번째줄에 len(word)-1 인데 처음에 -1을 하지않고 코드를 돌리다가 범위밖의 for문을 돌린다는 경고문이 떴다.



> 처음에 구글링을 통해 찾아봤는데 코드분석이 힘들었다 그래서 설명을 해준 블로그를 보고 이해를 했는데 내가 조금더 이해하기 쉬운 방식으로 작성 했다
