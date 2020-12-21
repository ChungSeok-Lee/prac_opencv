# 목적
- 동영상 속 오브젝트 디텍팅 학습
- **1차 목표:** 이미지를 불러와서 원하는 오브젝트 디텍션
- **2차 목표:** 동영상에서 움직이는 오브젝트 디텍션
- **3차 목표:** 동영상에서 움직이는 오브젝트를 디텍션하고 해당 오브젝트가 출현한 시간을 출력 

<br><br>

# 목차 
- [참고 자료](#참고-자료)
- [개발 환경](#개발-환경)

- [개발 이슈](#개발-이슈)
<br><br>

# 참고-자료
1. [Main_Study_Site](https://www.pyimagesearch.com/start-here/): pyimagesearch.com


# 개발 환경
1. Python 3.8.6 64bit
2. numpy 1.19.3


# 개발 이슈
## _2020/12/21_<br>
    이슈: opencv를 설치하니 library를 제대로 import하지 못하는 경우가 생겼다.
    해결: opencv 설치 시 설치되는 numpy 1.19.4 대신 1.19.3를 설치해주니 해결