from django.db.models import Q
import django_filters as filters
from django_tables2 import SingleTableView
from .models import Product
import itertools

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        exclude = ()

class ProductFilterEx(filters.FilterSet):
    ex = filters.CharFilter(label='Filter Products', method='filter_ex')
    search_fields = ['product_name', 'category__category_name', ]

    def filter_ex(self, qs, name, value):
        if value:
            q_parts = value.split()

            q_totals = Q()

            combinatorics = itertools.product([True, False], repeat=len(q_parts) - 1)
            possibilities = []
            for combination in combinatorics:
                i = 0
                one_such_combination = [q_parts[i]]
                for slab in combination:
                    i += 1
                    if not slab: # there is a join
                        one_such_combination[-1] += ' ' + q_parts[i]
                    else:
                        one_such_combination += [q_parts[i]]
                possibilities.append(one_such_combination)

            for p in possibilities:
                list1=self.search_fields
                list2=p
                perms = [zip(x,list2) for x in itertools.permutations(list1,len(list2))]

                for perm in perms:
                    q_part = Q()
                    for p in perm:
                        q_part = q_part & Q(**{p[0]+'__icontains': p[1]})
                    q_totals = q_totals | q_part

            qs = qs.filter(q_totals)

        return qs

    class Meta:
        model = Product
        fields = ['ex']
