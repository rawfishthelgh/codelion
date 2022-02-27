from django.shortcuts import render
import requests
import json
from .forms import SearchForm
#moviedb에서 받은 api 키
my_id = 'bd60a095ac065ce6b764fcdd4da18be0'
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        #post로 입력된 것 중 'search'로 입력된 값 가져오겠다.
        searchword = request.POST.get('search')
        if form.is_valid():
            url = "https://api.themoviedb.org/3/search/movie?api_key="+my_id+'&query='+searchword
            response = requests.get(url)
            resdata = response.text
            obj=json.loads(resdata)
            obj=obj['results']
            return render(request,'search.html',{'obj':obj})
        #입력된 내용을 바탕으로
        #"https://api.themoviedb.org/3/search/movie?api_key=bd60a095ac065ce6b764fcdd4da18be0&language=en-US&query=hello&page=1&include_adult=false"
        # 위 형태 url로 get 요청 보내기

    else:
        form = SearchForm()    
        #moviedb에서 임시로 생성한 url
        url ="https://api.themoviedb.org/3/trending/movie/week?api_key="+my_id
        #response 에 url로 get 요청 보낸것 받아옴
        response = requests.get(url)
        #응답 객체 텍스트로 json을 받아옴
        resdata = response.text
        #json 파일을 파이썬 객체로 반환
        obj=json.loads(resdata)
        #갖고오고자 하는 데이터가 존재하는 key를 통해 값 가져옴
        obj=obj['results']

    return render(request,'index.html',{'obj':obj,'form':form})

def detail(request,movie_id):
    url ="https://api.themoviedb.org/3/movie/"+ movie_id +"?api_key="+my_id
    # https://api.themoviedb.org/3/movie/300?api_key=bd60a095ac065ce6b764fcdd4da18be0&language=en-US
    # 이 url에 get 요청 보내기
    response = requests.get(url)
    resdata = response.text
    return render(request,'detail.html',{'resdata':resdata})