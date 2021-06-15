from django.contrib import admin
from .models import Category, Criteria, Subcriteria, House, HousePoints

# TODO: Do the above to the Category/Criteria and the Criteria/SubCriteria relationship

# TODO: Set the list_display for all registered models.


class SubcriteriaInline(admin.TabularInline):
    model = Subcriteria


class CriteriaAdmin(admin.ModelAdmin):
    inlines = [SubcriteriaInline]
    filter_by = ('category')
    list_display = ('name', 'max_points')


class HousePointsInline(admin.TabularInline):
    model = HousePoints


class HouseAdmin(admin.ModelAdmin):
    inlines = [HousePointsInline]
    # TODO: fill in with field to include in table.
    list_display = ('name', 'user')
    readonly_fields = ('total_points', )

    def total_points(self, obj):
        return obj.total_points()


admin.site.register(House, HouseAdmin)
admin.site.register(Category)
admin.site.register(Criteria, CriteriaAdmin)
