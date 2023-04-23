from django.shortcuts import render, redirect
from students.models import User_name, User_birth, User_info, User_work
from students.forms import CreateNameForm, CreateBirthForm, CreateInfoForm, CreateWorkForm


def index_page(request):
    if request.user.is_authenticated:
        user_names = User_name.objects.filter(owner_id=request.user.id)
        return render(request, 'students/index.html', {'user_names': user_names, 'user': request.user})
    else:
        return redirect('/auth/login/')


def create_name(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateNameForm()
            return render(request, 'students/create-name.html', {'form': form})
        if request.method == 'POST':
            form = CreateNameForm(request.POST)
            if form.is_valid():
                firstname = form.data.get('firstname')
                secondname = form.data.get('secondname')
                user_name = User_name(firstname=firstname, secondname=secondname, owner_id=request.user.id)
                user_name.save()
                return redirect('/')
            else:
                return render(request, 'students/create-name.html', {'form': form})
    else:
        return redirect('/auth/login/')


def user_name_details(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        user_births = User_birth.objects.filter(user_name_id=pk).order_by('-created_at')
        user_infos = User_info.objects.filter(user_name_id=pk).order_by
        user_works = User_work.objects.filter(user_name_id=pk).order_by
        form = CreateBirthForm()
        form1 = CreateInfoForm()
        form2 = CreateWorkForm()
        return render(request, 'students/user-name-details.html', {'user_name': user_name, 'user_births':user_births, 'user_infos':user_infos, 'user_works':user_works,'form':form, 'form1':form1, 'form2':form2})
    else:
        return redirect('/auth/login/')
    
def user_names_user_birth_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateBirthForm(request.POST)
            if form.is_valid():
                date_of_birth = form.data.get('date_of_birth')
                place_of_birth = form.data.get('place_of_birth')
                user_birth = User_birth(date_of_birth=date_of_birth, place_of_birth=place_of_birth, id=user_name.id, user_name=user_name )
                user_birth.save()
                return redirect('/students/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def user_info_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateInfoForm(request.POST)
            if form.is_valid():
                specialization = form.data.get('specialization')
                orga_of_education = form.data.get('orga_of_education')
                year_of_graduation = form.data.get('year_of_graduation')
                user_info = User_info(
                    id=user_name.id,  # устанавливаем id равным id user_name
                    specialization=specialization,
                    orga_of_education=orga_of_education,
                    year_of_graduation=year_of_graduation,
                    user_name=user_name  # устанавливаем связь с user_name
                )
                user_info.save()
                return redirect('/students/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')



def delete_birth(request, pk):
    if request.user.is_authenticated:
        user_birth = User_birth.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_birth.user_name.id)
        if user_name.owner.id == request.user.id:
            user_birth.delete()
            return redirect('/students/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def delete_user_name(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if user_name.owner.id == request.user.id:
            user_name.delete()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_info(request, pk):
    if request.user.is_authenticated:
            user_info = User_info.objects.get(id=pk)
            user_name = User_name.objects.get(id=user_info.user_name.id)
            if user_name.owner.id == request.user.id:
                user_info.delete()
                return redirect('/students/' + str(user_name.id) + '/')
            else:
                return redirect('/')
    else:
        return redirect('/auth/login/')

    
def user_work_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateWorkForm(request.POST)
            if form.is_valid():
                address = form.data.get('address')
                organization = form.data.get('organization')
                user_work = User_work(address=address,organization=organization, id=user_name.id, user_name=user_name)
                user_work.save()
                return redirect('/students/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_work(request, pk):
    if request.user.is_authenticated:
        user_work = User_work.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_work.user_name.id)
        if user_name.owner.id == request.user.id:
            user_work.delete()
            return redirect('/students/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
