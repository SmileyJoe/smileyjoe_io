from utils import view


# Create your views here.
def index(request):
    return view.display_main(request, page='index.html')


def custom_404(request):
    return view.display_main(request, page='404.html')
