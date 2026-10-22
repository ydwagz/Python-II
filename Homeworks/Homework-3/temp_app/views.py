from django.shortcuts import render


def info(request):

    context = {
        'name': 'Luca Godadze',
        'Email': 'Godadzeluca@gmail.com',
        'number': '595 02 21 25'
    }

    return render(request, 'info.html', {'context': context})



def hobbies(request):

    grade = {
        'grade': 9
    }
    
    

    return render(request, 'hobbies.html', grade)
