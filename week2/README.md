앞쪽에 있던 단어들까지 다 저장해놓을 수 있는 순환모델에 대해 배웠다. 그걸 수치로 압축해놓으면 효율성이 많이 올라갔을 것 같다.gpt2언어모델을 사용해서 번역도 시도해보았다. 계속 시도를 해도 제대로 번역이잘 안되서 힘들었다. 그래도 대화형식으로 예시를 많이 나열해주니까 그나마 비슷하게 나왔던것 같다. 



ENGLISH -> FRENCH 괜찮았던 사례✅
PROMPT
"1️⃣Question: Translate 'Hello' from English to French. 
Answer: Sure. In French, 'Hello' is translated as 'Bonjour'. 

2️⃣Question: Translate 'Thank you' from English to French. 
Answer: Sure. In French, 'Thank you' is translated as 'Merci'. 

3️⃣Question: Translate 'Goodbye' from English to French. 
Answer: Sure. In French, 'Goodbye' is translated as 'Au revoir'.

 4️⃣Question: Translate 'Please.' from English to French. 
Answer: Sure. In French, 'Please.' is translated as ❓❓ "

출력
Question: Translate 'Please.' from English to French. 
Answer: Sure. In French, 'Please.' is translated as était à le toute


시도 사례들
입력

처음
" Translate the following sentence from English to Spanish: 'Hi'
" Translate 'hi' from English to Spanish"

대화문 형식
" Question: Translate 'Hi' from English to Spanish  
Answer: sure. In French, 'hi' is translated to French as"

예시 제공
" translate English to French : 
'hello'is 'Bonjour.'    'Thank you.'is 'Merci'  
'Goodbye.'is 'Au revoir' 
'Please.' is  "

출력: 실패
Hi' means 'Hi' and 'Hi' means 'Hi'. 'Hi' means 'Hi' ~~~~~~~~~~

is translated as 도오야아도
is translated as  ͡° ͜ʖ ͡°
