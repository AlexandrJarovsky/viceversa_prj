from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    revers_text = user_text[::-1]
    count_words = len(user_text.split())
    titl_text = f'Original Text for {count_words} words'
#    print(test1)
    return render(request, 'reverse.html', {'usertext': user_text, 'reverstext': revers_text,
                                            'origtext': titl_text})
