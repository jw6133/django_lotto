from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import render, redirect

def index(request):
    lottos = GuessNumbers.objects.all()  # DB에 저장된 GuessNumbers 객체 모두를 가져온다.
    return render(request, 'lotto/default.html', {'lottos': lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")

# Create your views here.
def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)  # filled form
        if form.is_valid():
            # 사용자로부터 입력받은 form 데이터에서 추가로 수정해주려는 사항이 있을 경우 save를 보류함
            lotto = form.save(commit=False)  # 최종 DB 저장은 generate 함수 내부의 .save()로 처리
            lotto.generate()
            return redirect('index')  # urls.py의 name='index'에 해당
    else:
        form = PostForm()  # empty form

    return render(request, "lotto/form.html", {"form": form})

def detail(request, lottokey):
 lotto = GuessNumbers.objects.get(pk = lottokey) # primary key
 return render(request, "lotto/detail.html", {"lotto": lotto})
