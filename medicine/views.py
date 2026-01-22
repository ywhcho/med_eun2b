from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Medicine

def index(request):
    """의약정보 검색 메인 페이지"""
    # 통계 정보
    total_medicines = Medicine.objects.count()
    ingredients = Medicine.objects.values_list('ingredient', flat=True).distinct().count()
    companies = Medicine.objects.values_list('company', flat=True).distinct().count()
    
    context = {
        'total_medicines': total_medicines,
        'ingredients_count': ingredients,
        'companies_count': companies,
    }
    return render(request, 'medicine/index.html', context)

def ingredient_search(request):
    """성분별 검색"""
    ingredient_param = request.GET.get('ingredient', '')
    
    # 모든 고유한 성분명 가져오기
    all_ingredients = Medicine.objects.values_list('ingredient', flat=True).distinct().order_by('ingredient')
    
    medicines = None
    if ingredient_param:
        medicines = Medicine.objects.filter(ingredient__icontains=ingredient_param)
        paginator = Paginator(medicines, 10)
        page_number = request.GET.get('page')
        medicines = paginator.get_page(page_number)
    
    context = {
        'ingredients': all_ingredients,
        'selected_ingredient': ingredient_param,
        'medicines': medicines,
    }
    return render(request, 'medicine/ingredient.html', context)

def company_search(request):
    """회사별 검색"""
    company_param = request.GET.get('company', '')
    
    # 모든 고유한 회사명 가져오기
    all_companies = Medicine.objects.values_list('company', flat=True).distinct().order_by('company')
    
    medicines = None
    if company_param:
        medicines = Medicine.objects.filter(company__icontains=company_param)
        paginator = Paginator(medicines, 10)
        page_number = request.GET.get('page')
        medicines = paginator.get_page(page_number)
    
    context = {
        'companies': all_companies,
        'selected_company': company_param,
        'medicines': medicines,
    }
    return render(request, 'medicine/company.html', context)

def efficacy_search(request):
    """효능별 검색"""
    efficacy_param = request.GET.get('efficacy', '')
    
    # 모든 효능에서 키워드 추출 (간단히 고유한 효능 텍스트들)
    all_efficacies = Medicine.objects.values_list('efficacy', flat=True).distinct()
    
    # 효능 키워드 추출 (중복 제거)
    efficacy_keywords = set()
    for efficacy in all_efficacies:
        # 간단한 키워드 추출: 쉼표나 점으로 구분
        keywords = efficacy.replace('.', ',').split(',')
        for keyword in keywords:
            keyword = keyword.strip()
            if keyword and len(keyword) > 2:  # 2글자 이상만
                efficacy_keywords.add(keyword[:50])  # 최대 50자
    
    efficacy_keywords = sorted(list(efficacy_keywords))
    
    medicines = None
    if efficacy_param:
        medicines = Medicine.objects.filter(efficacy__icontains=efficacy_param)
        paginator = Paginator(medicines, 10)
        page_number = request.GET.get('page')
        medicines = paginator.get_page(page_number)
    
    context = {
        'efficacies': efficacy_keywords,
        'selected_efficacy': efficacy_param,
        'medicines': medicines,
    }
    return render(request, 'medicine/efficacy.html', context)

def medicine_detail(request, pk):
    """의약품 상세 정보"""
    medicine = get_object_or_404(Medicine, pk=pk)
    return render(request, 'medicine/detail.html', {'medicine': medicine})

