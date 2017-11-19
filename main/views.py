from utils import view


# Create your views here.
def index(request):
    return view.display(request, page='main/index.html')


def custom_404(request):
    return view.display(request, page='main/404.html')
