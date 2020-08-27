### `countletters_project2`

# 참고한 글자수 세기 페이지
![naver](../images/count_naver.png)

# Django로 만든 글자수 세기 페이지

### 1-(1) Home

![home](../images/count_home.png)

### 1-(2) Home에 글자 입력

![content](../images/count_home_content.png)

### 2. 결과 페이지

![image](https://user-images.githubusercontent.com/58651942/91447848-1c03f480-e8b4-11ea-9961-b471ba8fa4dc.png)


---

### 문제)

공백을 제외한 경우, 줄넘김을 할 때마다 글자수가 1씩 늘어남. 네이버는 안 늘어남.

### 해결)

replace('\n', '')로 줄넘김을 처리했는데, 줄넘김이 '\r\n'으로 처리되어서 \r이 세졌음.
<u>줄넘김을 \n 또는 \r\n으로 처리할 수 있으니 주의할 것</u>