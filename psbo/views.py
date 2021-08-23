from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


def board(request):
    # 질문 목록 출력 함수
    # 입력인자
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 12)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'psbo/question_list.html', context)


def detail(request, question_id):
    # 질문 내용 출력 함수
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'psbo/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    # 글 등록 함수
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('psbo:board')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'psbo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    # 질문 수정함수
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('psbo:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('psbo:detail', question_id=question.id)

    else:
        form = QuestionForm(instance=question)

    context = {'form':form}
    return render(request, 'psbo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    # 질문 삭제 함수
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('psbo:detail', question_id=question.id)
    question.delete()
    return redirect('psbo:board')


@login_required(login_url='common:login')
def answer_create(request, question_id):
    # 답변 등록 함수
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('psbo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'psbo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    # 답변 수정 함수
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('psbo:detail', question_id=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('psbo:detail', question_id=answer.question.id), answer.id))
    else:
        form = AnswerForm(instance=answer)
    context = {'answer':answer, 'form':form}
    return render(request, 'psbo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    # 답변 삭제 함수
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('psbo:detail', question_id=answer.question.id)