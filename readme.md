오늘 점심 뭐 먹지 플젝 중 세부 프로젝트, 우체국 미니뷔페 메뉴를 매주 월요일마다 크롤링해서 팀즈로 알림 주는 프로그램입니다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<!-- <a href="https://github.com/Selenium/selenium"><img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=Selenium&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Chrome-4285F4?style=flat-square&logo=GoogleChrome&logoColor=white"/> -->

## **REQUIREMENTS**

> ---
>
> This module requires the following modules:

<!-- > - [Python 3.9.9](https://www.python.org/downloads/release/python-399/) -->

> Python 3.10.12
>
> ---

</br>
</br>

## **INSTALL**

## ubuntu, mac(intel), (windows)

### (optional) using virtual env

```sh
# generate venv
python -m venv 5.mho
```

```sh
# activate in linux
source 5.moh/bin/activate

# activate in windows
source 5.mho/Scripts/activate
```

> ---
>
> ## intel
>
> ### **requiremetns.txt** for intel
>
> ai pc : requirements_ubuntu_new.txt </br>
> ai pc : docker (requirements_intelmac_fixed.txt) </br>
> intel mac : requirement~s_intelmac_fixed.txt </br>
>
> ```shell
> pip install -r requirements.txt
> ```
>
> 새로운 패키지 설치 시
>
> ```shell
> $ pip freeze > requirements.txt
> $ pip list --format=freeze > requirements.txt
> ```
>
> ---
>
> ## m1 mac
>
> > ### **conda_requiremetns.yaml** for mac m1
> >
> > miniforge3 설치
> > https://github.com/conda-forge/miniforge/
> > 위 링크에서 본인 버전 맞춰서 다운로드 후
>
> ```bash
> bash ~/Miniforge3-MacOSX-arm64.sh -b -p $HOME/miniconda
> source ~/miniconda/bin/activate
> conda env create -f conda_requirements.txt
> ```
>
> how to run
>
> ```bash
> #모든 conda deactivate
> deactivate, conda deactivate, source deactivate 등등 반복
> conda info --envs
> conda activate {env}
> python3 -m conthemore_data_extraction --input_chat_bubble "보은 신항 40피트 수입정리합니다~코스코점보 22.4톤 현대신항상차 9시착(오늘만기)"
> ```
>
> 자세한 사항은
> https://app.clickup.com/25549628/v/dc/rbptw-6143/rbptw-14880
>
> 새로운 설치 시마다
>
> ```bash
> conda env export > conda_requirements.yaml
> ```
>
> how to run flask server
>
> ```bash
> python3 -m conthemore_api.app
> ```
>
> ---

</br>

</br>

## **RUN**

AI 서버에서 flask 서버 구동

> ```zsh
> cd ~/Sylvy_workspace/cargo-market-bert/chat_stereotyping
> source chatstereotyping/bin/activate
> python3 -m conthemore_api.app
> ```

## **DIRECTORY TREE**
