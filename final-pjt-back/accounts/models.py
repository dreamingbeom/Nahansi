from django.db import models
from django.contrib.auth.models import AbstractUser

# 11-17 10:56 경범 User 모델 내용 추가
# 주거래은행 , 저축목표, 직종 추가
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    ## 밑으로는 선택사항
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)                      # 연봉
    salary = models.IntegerField(blank=True, null=True)                     # 자산
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)            # 가입 상품
    primary_bank = models.CharField(max_length=50, blank=True, null=True)   # 주 거래은행
    savings_goal = models.CharField(max_length=50, blank=True, null=True)   # 저축 목표
    occupation = models.CharField(max_length=50, blank=True, null=True)     # 직종
    savings_term = models.IntegerField(blank=True, null=True)                # 저축 기간

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'



from allauth.account.utils import user_email, user_field, user_username
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = form.data.get("email")
        username = data.get("username")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        print( request.data)
        financial_product = request.data.get("financial_products")
        print(financial_product)
        primary_bank = data.get('primary_bank')
        savings_goal = data.get("savings_goal")
        occupation = data.get('occupation')
        savings_term = data.get('savings_term')

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if primary_bank:
            user.primary_bank = primary_bank
        if savings_goal:
            user.savings_goal = savings_goal
        if occupation:
            user.occupation = occupation
        if savings_term:
            user.savings_term = savings_term

        if financial_product:
            if user.financial_products:
                l = user.financial_products[1:len(user.financial_products)-1].split(',')
                l.append(financial_product)
                user.financial_products = '[' + ','.join(l) + ']'
            else:
                user.financial_products =  financial_product 
        #     # 리스트를 다시 문자열로 합침
        #     financial_products_str = ','.join(unique_financial_products)
            
        #     # 업데이트된 financial_products 값을 user 객체에 설정
        #     user_field(user, "financial_products", financial_products_str)


        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()

        return user